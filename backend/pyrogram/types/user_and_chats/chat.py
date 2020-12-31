from typing import Union, List, Generator, Optional

import pyrogram
from pyrogram import raw
from pyrogram import types
from pyrogram import utils

from ..object import Object


class Chat(Object):
    """A chat.

    Parameters:
        id (``int``):
            Unique identifier for this chat.

        type (``str``):
            Type of chat, can be either "private", "bot", "group", "supergroup" or "channel".
    """

    def __init__(
            self,
            *,
            client: "pyrogram.Client" = None,
            id: int,
            type: str,

            # added
            is_full_type: bool = None,
            full_user: "types.UserFull" = None,
            full_group: "types.GroupFull" = None,
            full_channel: "types.ChannelFull" = None,
            user: "types.User" = None,
            group: "types.Group" = None,
            channel: "types.Channel" = None,
    ):
        super().__init__(client)

        self.id = id
        self.type = type

        self.is_full_type = is_full_type
        self.full_user = full_user
        self.full_group = full_group
        self.full_channel = full_channel
        self.user = user
        self.group = group
        self.channel = channel

    @staticmethod
    def _parse_user_chat(client, user: raw.types.User) -> "Chat":
        if user is None:
            return None

        peer_id = user.id

        return Chat(
            client=client,

            id=peer_id,
            type="bot" if user.bot else "private",
            user=types.User._parse(client, user),
            is_full_type=False,
        )

    @staticmethod
    async def _parse_user_full_chat(client, user: raw.types.UserFull) -> "Chat":
        peer_id = user.user.id

        return Chat(
            client=client,

            id=peer_id,
            type="bot" if user.user.bot else "private",
            full_user=await types.UserFull._parse(client, user),
            is_full_type=True,
        )

    @staticmethod
    async def _parse_group_chat(client, chat: raw.types.Chat) -> "Chat":
        if chat is None:
            return None

        peer_id = -chat.id

        return Chat(
            client=client,

            id=peer_id,
            type="group",
            group=await types.Group._parse(client, chat),
            is_full_type=False,
        )

    @staticmethod
    async def _parse_group_full_chat(
            client,
            chat_full: "raw.types.messages.ChatFull",
            users: dict,
            chats: dict,
    ) -> "Chat":

        peer_id = -chat_full.full_chat.id
        return Chat(
            client=client,

            id=peer_id,
            type="group",
            full_group=await types.GroupFull._parse(client, chat_full.full_chat, users, chats),
            group=await types.Group._parse(client, chats[chat_full.full_chat.id]),
            is_full_type=True,
        )

    @property
    def username(self):
        username = None
        if self.group:
            username = None
        elif self.channel:
            username = self.channel.username
        elif self.user:
            username = self.user.username
        return username

    @staticmethod
    async def _parse_channel_full_chat(client, chat_full: raw.types.messages.ChatFull, users: dict,
                                       chats: dict) -> "Chat":
        peer_id = utils.get_channel_id(chat_full.full_chat.id)

        channel = chats[chat_full.full_chat.id]
        return Chat(
            client=client,

            id=peer_id,
            type="supergroup" if channel.megagroup else "channel",
            full_channel=await types.ChannelFull._parse(client, chat_full.full_chat, users, chats),
            channel=types.Channel._parse(client, channel),
            is_full_type=True,
        )

    @staticmethod
    def _parse_channel_chat(client, channel: raw.types.Channel) -> "Chat":
        if channel is None:
            return None

        peer_id = utils.get_channel_id(channel.id)
        return Chat(
            client=client,

            id=peer_id,
            type="supergroup" if channel.megagroup else "channel",
            channel=types.Channel._parse(client, channel),
            is_full_type=False,
        )

    @staticmethod
    async def _parse(client, message: raw.types.Message or raw.types.MessageService, users: dict,
                     chats: dict) -> "Chat":
        if isinstance(message.peer_id, raw.types.PeerUser):
            if message.out:
                _peer_id = message.peer_id.user_id
            else:
                if message.from_id:
                    _peer_id = message.from_id.user_id
                else:
                    if users[message.peer_id.user_id].is_self:
                        _peer_id = message.peer_id.user_id
                    else:
                        _peer_id = None
            return Chat._parse_user_chat(client,
                                         users[_peer_id])

        if isinstance(message.peer_id, raw.types.PeerChat):
            return await Chat._parse_group_chat(client, chats[message.peer_id.chat_id])

        return Chat._parse_channel_chat(client, chats[message.peer_id.channel_id])

    @staticmethod
    def _parse_dialog(client, peer, users: dict, chats: dict):
        if isinstance(peer, raw.types.PeerUser):
            return Chat._parse_user_chat(client, users[peer.user_id])
        elif isinstance(peer, raw.types.PeerChat):
            return Chat._parse_group_chat(client, chats[peer.chat_id])
        else:
            return Chat._parse_channel_chat(client, chats[peer.channel_id])

    @staticmethod
    async def _parse_full(client, chat_full: raw.types.messages.ChatFull or raw.types.UserFull) -> "Chat":
        if isinstance(chat_full, raw.types.UserFull):
            parsed_chat = await Chat._parse_user_full_chat(client, chat_full)
        else:
            users = {}
            chats = {}
            if chat_full.users:
                users = {_user.id: _user for _user in chat_full.users}

            if chat_full.chats:
                chats = {_chat.id: _chat for _chat in chat_full.chats}

            if isinstance(chat_full.full_chat, raw.types.ChatFull):
                # parsed_chat = Chat._parse_group_chat(client, chat)
                parsed_chat = await Chat._parse_group_full_chat(client, chat_full, users, chats)
            else:
                parsed_chat = await Chat._parse_channel_full_chat(client, chat_full, users, chats, )

        return parsed_chat

    @staticmethod
    async def _parse_chat(client, chat: Union[raw.types.Chat, raw.types.User, raw.types.Channel]) -> "Chat":
        if isinstance(chat, raw.types.Chat):
            return await Chat._parse_group_chat(client, chat)
        elif isinstance(chat, raw.types.User):
            return Chat._parse_user_chat(client, chat)
        else:
            return Chat._parse_channel_chat(client, chat)

    async def archive(self):
        """Bound method *archive* of :obj:`~pyrogram.types.Chat`.

        Use as a shortcut for:

        .. code-block:: python

            client.archive_chats(-100123456789)

        Example:
            .. code-block:: python

                chat.archive()

        Returns:
            True on success.

        Raises:
            RPCError: In case of a Telegram RPC error.
        """

        return await self._client.archive_chats(self.id)

    async def unarchive(self):
        """Bound method *unarchive* of :obj:`~pyrogram.types.Chat`.

        Use as a shortcut for:

        .. code-block:: python

            client.unarchive_chats(-100123456789)

        Example:
            .. code-block:: python

                chat.unarchive()

        Returns:
            True on success.

        Raises:
            RPCError: In case of a Telegram RPC error.
        """

        return await self._client.unarchive_chats(self.id)

    # TODO: Remove notes about "All Members Are Admins" for basic groups, the attribute doesn't exist anymore
    async def set_title(self, title: str) -> bool:
        """Bound method *set_title* of :obj:`~pyrogram.types.Chat`.

        Use as a shortcut for:

        .. code-block:: python

            client.set_chat_title(
                chat_id=chat_id,
                title=title
            )

        Example:
            .. code-block:: python

                chat.set_title("Lounge")

        Note:
            In regular groups (non-supergroups), this method will only work if the "All Members Are Admins"
            setting is off.

        Parameters:
            title (``str``):
                New chat title, 1-255 characters.

        Returns:
            ``bool``: True on success.

        Raises:
            RPCError: In case of Telegram RPC error.
            ValueError: In case a chat_id belongs to user.
        """

        return await self._client.set_chat_title(
            chat_id=self.id,
            title=title
        )

    async def set_description(self, description: str) -> bool:
        """Bound method *set_description* of :obj:`~pyrogram.types.Chat`.

        Use as a shortcut for:

        .. code-block:: python

            client.set_chat_description(
                chat_id=chat_id,
                description=description
            )

        Example:
            .. code-block:: python

                chat.set_chat_description("Don't spam!")

        Parameters:
            description (``str``):
                New chat description, 0-255 characters.

        Returns:
            ``bool``: True on success.

        Raises:
            RPCError: In case of Telegram RPC error.
            ValueError: If a chat_id doesn't belong to a supergroup or a channel.
        """

        return await self._client.set_chat_description(
            chat_id=self.id,
            description=description
        )

    async def set_photo(self, photo: str) -> bool:
        """Bound method *set_photo* of :obj:`~pyrogram.types.Chat`.

        Use as a shortcut for:

        .. code-block:: python

            client.set_chat_photo(
                chat_id=chat_id,
                photo=photo
            )

        Example:
            .. code-block:: python

                chat.set_photo("photo.png")

        Parameters:
            photo (``str``):
                New chat photo. You can pass a :obj:`~pyrogram.types.Photo` id or a file path to upload a new photo.

        Returns:
            ``bool``: True on success.

        Raises:
            RPCError: In case of a Telegram RPC error.
            ValueError: if a chat_id belongs to user.
        """

        return await self._client.set_chat_photo(
            chat_id=self.id,
            photo=photo
        )

    async def kick_member(
            self,
            user_id: Union[int, str],
            until_date: int = 0
    ) -> Union["types.Message", bool]:
        """Bound method *kick_member* of :obj:`~pyrogram.types.Chat`.

        Use as a shortcut for:

        .. code-block:: python

            client.kick_chat_member(
                chat_id=chat_id,
                user_id=user_id
            )

        Example:
            .. code-block:: python

                chat.kick_member(123456789)

        Note:
            In regular groups (non-supergroups), this method will only work if the "All Members Are Admins" setting is
            off in the target group. Otherwise members may only be removed by the group's creator or by the member
            that added them.

        Parameters:
            user_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the target user.
                For a contact that exists in your Telegram address book you can use his phone number (str).

            until_date (``int``, *optional*):
                Date when the user will be unbanned, unix time.
                If user is banned for more than 366 days or less than 30 seconds from the current time they are
                considered to be banned forever. Defaults to 0 (ban forever).

        Returns:
            :obj:`~pyrogram.types.Message` | ``bool``: On success, a service message will be returned (when applicable), otherwise, in
            case a message object couldn't be returned, True is returned.

        Raises:
            RPCError: In case of a Telegram RPC error.
        """

        return await self._client.kick_chat_member(
            chat_id=self.id,
            user_id=user_id,
            until_date=until_date
        )

    async def unban_member(
            self,
            user_id: Union[int, str]
    ) -> bool:
        """Bound method *unban_member* of :obj:`~pyrogram.types.Chat`.

        Use as a shortcut for:

        .. code-block:: python

            client.unban_chat_member(
                chat_id=chat_id,
                user_id=user_id
            )

        Example:
            .. code-block:: python

                chat.unban_member(123456789)

        Parameters:
            user_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the target user.
                For a contact that exists in your Telegram address book you can use his phone number (str).

        Returns:
            ``bool``: True on success.

        Raises:
            RPCError: In case of a Telegram RPC error.
        """

        return await self._client.unban_chat_member(
            chat_id=self.id,
            user_id=user_id,
        )

    async def restrict_member(
            self,
            user_id: Union[int, str],
            permissions: "types.ChatPermissions",
            until_date: int = 0,
    ) -> "types.Chat":
        """Bound method *unban_member* of :obj:`~pyrogram.types.Chat`.

        Use as a shortcut for:

        .. code-block:: python

            client.restrict_chat_member(
                chat_id=chat_id,
                user_id=user_id,
                permissions=ChatPermissions()
            )

        Example:
            .. code-block:: python

                chat.restrict_member(user_id, ChatPermissions())

        Parameters:
            user_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the target user.
                For a contact that exists in your Telegram address book you can use his phone number (str).

            permissions (:obj:`~pyrogram.types.ChatPermissions`):
                New user permissions.

            until_date (``int``, *optional*):
                Date when the user will be unbanned, unix time.
                If user is banned for more than 366 days or less than 30 seconds from the current time they are
                considered to be banned forever. Defaults to 0 (ban forever).

        Returns:
            :obj:`~pyrogram.types.Chat`: On success, a chat object is returned.

        Raises:
            RPCError: In case of a Telegram RPC error.
        """

        return await self._client.restrict_chat_member(
            chat_id=self.id,
            user_id=user_id,
            permissions=permissions,
            until_date=until_date,
        )

    async def promote_member(
            self,
            user_id: Union[int, str],
            can_change_info: bool = True,
            can_post_messages: bool = False,
            can_edit_messages: bool = False,
            can_delete_messages: bool = True,
            can_restrict_members: bool = True,
            can_invite_users: bool = True,
            can_pin_messages: bool = False,
            can_promote_members: bool = False
    ) -> bool:
        """Bound method *promote_member* of :obj:`~pyrogram.types.Chat`.

        Use as a shortcut for:

        .. code-block:: python

            client.promote_chat_member(
                chat_id=chat_id,
                user_id=user_id
            )

        Example:

            .. code-block:: python

                chat.promote_member(123456789)

        Parameters:
            user_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the target user.
                For a contact that exists in your Telegram address book you can use his phone number (str).

            can_change_info (``bool``, *optional*):
                Pass True, if the administrator can change chat title, photo and other settings.

            can_post_messages (``bool``, *optional*):
                Pass True, if the administrator can create channel posts, channels only.

            can_edit_messages (``bool``, *optional*):
                Pass True, if the administrator can edit messages of other users and can pin messages, channels only.

            can_delete_messages (``bool``, *optional*):
                Pass True, if the administrator can delete messages of other users.

            can_restrict_members (``bool``, *optional*):
                Pass True, if the administrator can restrict, ban or unban chat members.

            can_invite_users (``bool``, *optional*):
                Pass True, if the administrator can invite new users to the chat.

            can_pin_messages (``bool``, *optional*):
                Pass True, if the administrator can pin messages, supergroups only.

            can_promote_members (``bool``, *optional*):
                Pass True, if the administrator can add new administrators with a subset of his own privileges or
                demote administrators that he has promoted, directly or indirectly (promoted by administrators that
                were appointed by him).

        Returns:
            ``bool``: True on success.

        Raises:
            RPCError: In case of a Telegram RPC error.
        """

        return await self._client.promote_chat_member(
            chat_id=self.id,
            user_id=user_id,
            can_change_info=can_change_info,
            can_post_messages=can_post_messages,
            can_edit_messages=can_edit_messages,
            can_delete_messages=can_delete_messages,
            can_restrict_members=can_restrict_members,
            can_invite_users=can_invite_users,
            can_pin_messages=can_pin_messages,
            can_promote_members=can_promote_members
        )

    async def join(self):
        """Bound method *join* of :obj:`~pyrogram.types.Chat`.

        Use as a shortcut for:

        .. code-block:: python

            client.join_chat(123456789)

        Example:
            .. code-block:: python

                chat.join()

        Note:
            This only works for public groups, channels that have set a username or linked chats.

        Returns:
            :obj:`~pyrogram.types.Chat`: On success, a chat object is returned.

        Raises:
            RPCError: In case of a Telegram RPC error.
        """

        return await self._client.join_chat(self.username or self.id)

    async def leave(self):
        """Bound method *leave* of :obj:`~pyrogram.types.Chat`.

        Use as a shortcut for:

        .. code-block:: python

            client.leave_chat(123456789)

        Example:
            .. code-block:: python

                chat.leave()

        Raises:
            RPCError: In case of a Telegram RPC error.
        """

        return await self._client.leave_chat(self.id)

    async def export_invite_link(self):
        """Bound method *export_invite_link* of :obj:`~pyrogram.types.Chat`.

        Use as a shortcut for:

        .. code-block:: python

            client.export_chat_invite_link(123456789)

        Example:
            .. code-block:: python

                chat.export_invite_link()

        Returns:
            ``str``: On success, the exported invite link is returned.

        Raises:
            ValueError: In case the chat_id belongs to a user.
        """

        return await self._client.export_chat_invite_link(self.id)

    async def get_member(
            self,
            user_id: Union[int, str],
    ) -> "types.ChatMember":
        """Bound method *get_member* of :obj:`~pyrogram.types.Chat`.

        Use as a shortcut for:

        .. code-block:: python

            client.get_chat_member(
                chat_id=chat_id,
                user_id=user_id
            )

        Example:
            .. code-block:: python

                chat.get_member(user_id)

        Returns:
            :obj:`~pyrogram.types.ChatMember`: On success, a chat member is returned.
        """

        return await self._client.get_chat_member(
            self.id,
            user_id=user_id
        )

    async def get_members(
            self,
            offset: int = 0,
            limit: int = 200,
            query: str = "",
            filter: str = "all"
    ) -> List["types.ChatMember"]:
        """Bound method *get_members* of :obj:`~pyrogram.types.Chat`.

        Use as a shortcut for:

        .. code-block:: python

            client.get_chat_members(chat_id)

        Example:
            .. code-block:: python

                # Get first 200 recent members
                chat.get_members()

        Returns:
            List of :obj:`~pyrogram.types.ChatMember`: On success, a list of chat members is returned.
        """

        return await self._client.get_chat_members(
            self.id,
            offset=offset,
            limit=limit,
            query=query,
            filter=filter
        )

    def iter_members(
            self,
            limit: int = 0,
            query: str = "",
            filter: str = "all"
    ) -> Optional[Generator["types.ChatMember", None, None]]:
        """Bound method *iter_members* of :obj:`~pyrogram.types.Chat`.

        Use as a shortcut for:

        .. code-block:: python

            for member in client.iter_chat_members(chat_id):
                print(member.user.first_name)

        Example:
            .. code-block:: python

                for member in chat.iter_members():
                    print(member.user.first_name)

        Returns:
            ``Generator``: A generator yielding :obj:`~pyrogram.types.ChatMember` objects.
        """

        return self._client.iter_chat_members(
            self.id,
            limit=limit,
            query=query,
            filter=filter
        )

    async def add_members(
            self,
            user_ids: Union[Union[int, str], List[Union[int, str]]],
            forward_limit: int = 100
    ) -> bool:
        """Bound method *add_members* of :obj:`~pyrogram.types.Chat`.

        Use as a shortcut for:

        .. code-block:: python

            client.add_chat_members(chat_id, user_id)

        Example:
            .. code-block:: python

                chat.add_members(user_id)

        Returns:
            ``bool``: On success, True is returned.
        """

        return await self._client.add_chat_members(
            self.id,
            user_ids=user_ids,
            forward_limit=forward_limit
        )
