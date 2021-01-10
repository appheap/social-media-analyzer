import pyrogram
from pyrogram import types, raw, utils
from ..object import Object

from typing import List, Union


class MessageAction(Object):
    """
    """

    def __init__(
            self,
            *,
            client: "pyrogram.Client" = None,
    ):
        super().__init__(client=client)

    @staticmethod
    async def _parse_action(client, message: raw.types.MessageService, users: dict, chats: dict):
        if message is None:
            return None

        action = message.action

        if isinstance(action, raw.types.MessageActionEmpty):
            return MessageActionEmpty._parse(client, action, users, chats)

        elif isinstance(action, raw.types.MessageActionChatCreate):
            return MessageActionChatCreate._parse(client, action, users, chats)

        elif isinstance(action, raw.types.MessageActionChatEditTitle):
            return MessageActionChatEditTitle._parse(client, action, users, chats)

        elif isinstance(action, raw.types.MessageActionChatEditPhoto):
            return MessageActionChatEditPhoto._parse(client, action, users, chats)

        elif isinstance(action, raw.types.MessageActionChatDeletePhoto):
            return MessageActionChatDeletePhoto._parse(client, action, users, chats)

        elif isinstance(action, raw.types.MessageActionChatAddUser):
            return MessageActionChatAddUser._parse(client, action, users, chats)

        elif isinstance(action, raw.types.MessageActionChatDeleteUser):
            return MessageActionChatDeleteUser._parse(client, action, users, chats)

        elif isinstance(action, raw.types.MessageActionChatJoinedByLink):
            return MessageActionChatJoinedByLink._parse(client, action, users, chats, message.from_id.user_id)

        elif isinstance(action, raw.types.MessageActionChannelCreate):
            return MessageActionChannelCreate._parse(client, action, users, chats)

        elif isinstance(action, raw.types.MessageActionChatMigrateTo):
            return MessageActionChatMigrateTo._parse(client, action, users, chats)

        elif isinstance(action, raw.types.MessageActionChannelMigrateFrom):
            return MessageActionChannelMigrateFrom._parse(client, action, users, chats)

        elif isinstance(action, raw.types.MessageActionPinMessage):
            return MessageActionPinMessage._parse(client, action, users, chats)

        elif isinstance(action, raw.types.MessageActionPinMessage):
            return MessageActionPinMessage._parse(client, action, users, chats)

        elif isinstance(action, raw.types.MessageActionHistoryClear):
            return MessageActionHistoryClear._parse(client, action, users, chats)

        elif isinstance(action, raw.types.MessageActionGameScore):
            return MessageActionGameScore._parse(client, action, users, chats)

        elif isinstance(action, raw.types.MessageActionPaymentSentMe):
            return MessageActionPaymentSentMe._parse(client, action, users, chats)

        elif isinstance(action, raw.types.MessageActionPaymentSent):
            return MessageActionPaymentSent._parse(client, action, users, chats)

        elif isinstance(action, raw.types.MessageActionPhoneCall):
            return MessageActionPhoneCall._parse(client, action, users, chats)

        elif isinstance(action, raw.types.MessageActionScreenshotTaken):
            return MessageActionScreenshotTaken._parse(client, action, users, chats)

        elif isinstance(action, raw.types.MessageActionCustomAction):
            return MessageActionCustomAction._parse(client, action, users, chats)

        elif isinstance(action, raw.types.MessageActionBotAllowed):
            return MessageActionBotAllowed._parse(client, action, users, chats)

        elif isinstance(action, raw.types.MessageActionSecureValuesSentMe):
            return MessageActionSecureValuesSentMe._parse(client, action, users, chats)

        elif isinstance(action, raw.types.MessageActionSecureValuesSent):
            return MessageActionSecureValuesSent._parse(client, action, users, chats)

        elif isinstance(action, raw.types.MessageActionContactSignUp):
            peer = message.from_id if message.from_id else message.peer_id
            return MessageActionContactSignUp._parse(client, action, users, chats, peer.user_id)

        elif isinstance(action, raw.types.MessageActionGeoProximityReached):
            return await MessageActionGeoProximityReached._parse(client, action, users, chats)

        # if isinstance(action, raw.types.MessageActionPinMessage):
        #     try:
        #         parsed_message.pinned_message = await
        #         client.get_messages(
        #             parsed_message.chat.id,
        #             reply_to_message_ids=message.id,
        #             replies=0
        #         )
        #     except MessageIdsEmpty:
        #         pass

        # if isinstance(action, raw.types.MessageActionGameScore):
        #     parsed_message.game_high_score = types.GameHighScore._parse_action(client, message, users)
        #
        #     if message.reply_to_msg_id and replies:
        #         try:
        #             parsed_message.reply_to_message = await
        #             client.get_messages(
        #                 parsed_message.chat.id,
        #                 reply_to_message_ids=message.id,
        #                 replies=0
        #             )
        #         except MessageIdsEmpty:
        #             pass


class MessageActionEmpty(MessageAction):
    """
    """

    def __init__(
            self,
            *,
            client: "pyrogram.Client" = None,
    ):
        super().__init__(client=client)

    @staticmethod
    def _parse(client, action, users: dict, chats: dict):
        if action is None:
            return None

        return MessageActionEmpty(
            client=client,
        )


class MessageActionChatCreate(MessageAction):
    """
    """

    def __init__(
            self,
            *,
            client: "pyrogram.Client" = None,

            title: str,
            users: List["types.User"]
    ):
        super().__init__(client=client)

        self.title = title
        self.users = users

    @staticmethod
    def _parse(client, action: raw.base.MessageAction, users: dict, chats: dict):
        if action is None:
            return None

        return MessageActionChatCreate(
            client=client,

            title=action.title,
            users=types.List([types.User._parse(client, users.get(user_id, None)) for user_id in action.users]) or None,
        )


class MessageActionChatEditTitle(MessageAction):
    """
    """

    def __init__(
            self,
            *,
            client: "pyrogram.Client" = None,

            title: str,
    ):
        super().__init__(client=client)

        self.title = title

    @staticmethod
    def _parse(client, action: raw.base.MessageAction, users: dict, chats: dict):
        if action is None:
            return None

        return MessageActionChatEditTitle(
            client=client,

            title=action.title,
        )


class MessageActionChatEditPhoto(MessageAction):
    """
    """

    def __init__(
            self,
            *,
            client: "pyrogram.Client" = None,

            photo: "types.Photo",
    ):
        super().__init__(client=client)

        self.photo = photo

    @staticmethod
    def _parse(client, action: raw.base.MessageAction, users: dict, chats: dict):
        if action is None:
            return None

        return MessageActionChatEditPhoto(
            client=client,

            photo=types.Photo._parse(client, action.photo),
        )


class MessageActionChatDeletePhoto(MessageAction):
    """
    """

    def __init__(
            self,
            *,
            client: "pyrogram.Client" = None,

    ):
        super().__init__(client=client)

    @staticmethod
    def _parse(client, action: raw.base.MessageAction, users: dict, chats: dict):
        if action is None:
            return None

        return MessageActionChatDeletePhoto(
            client=client,

        )


class MessageActionChatAddUser(MessageAction):
    """
    """

    def __init__(
            self,
            *,
            client: "pyrogram.Client" = None,

            users: List["types.User"]
    ):
        super().__init__(client=client)

        self.users = users

    @staticmethod
    def _parse(client, action: raw.base.MessageAction, users: dict, chats: dict):
        if action is None:
            return None

        return MessageActionChatAddUser(
            client=client,

            users=types.List([types.User._parse(client, users.get(user_id, None)) for user_id in action.users]) or None,
        )


class MessageActionChatDeleteUser(MessageAction):
    """
    """

    def __init__(
            self,
            *,
            client: "pyrogram.Client" = None,

            user: "types.User"
    ):
        super().__init__(client=client)

        self.user = user

    @staticmethod
    def _parse(client, action: raw.base.MessageAction, users: dict, chats: dict):
        if action is None:
            return None

        return MessageActionChatDeleteUser(
            client=client,

            user=types.User._parse(client, users.get(action.user_id, None))
        )


class MessageActionChatJoinedByLink(MessageAction):
    """
    """

    def __init__(
            self,
            *,
            client: "pyrogram.Client" = None,

            user: "types.User",
            invited_by: "types.User"
    ):
        super().__init__(client=client)

        self.user = user
        self.invited_by = invited_by

    @staticmethod
    def _parse(client, action: raw.base.MessageAction, users: dict, chats: dict, user_id: int):
        if action is None:
            return None

        return MessageActionChatJoinedByLink(
            client=client,

            user=types.User._parse(client, users.get(user_id, None)),
            invited_by=types.User._parse(client, users.get(action.inviter_id, None))
        )


class MessageActionChannelCreate(MessageAction):
    """
    """

    def __init__(
            self,
            *,
            client: "pyrogram.Client" = None,

            title: str,
    ):
        super().__init__(client=client)

        self.title = title

    @staticmethod
    def _parse(client, action: raw.base.MessageAction, users: dict, chats: dict):
        if action is None:
            return None

        return MessageActionChannelCreate(
            client=client,

            title=action.title,
        )


class MessageActionChatMigrateTo(MessageAction):
    """
    """

    def __init__(
            self,
            *,
            client: "pyrogram.Client" = None,

            channel_id: int,
    ):
        super().__init__(client=client)

        self.channel_id = channel_id

    @staticmethod
    def _parse(client, action: raw.base.MessageAction, users: dict, chats: dict):
        if action is None:
            return None

        return MessageActionChatMigrateTo(
            client=client,

            channel_id=utils.get_channel_id(action.channel_id),
        )


class MessageActionChannelMigrateFrom(MessageAction):
    """
    """

    def __init__(
            self,
            *,
            client: "pyrogram.Client" = None,

            title: str,
            chat_id: int,
    ):
        super().__init__(client=client)

        self.title = title
        self.chat_id = chat_id

    @staticmethod
    def _parse(client, action: raw.base.MessageAction, users: dict, chats: dict):
        if action is None:
            return None

        return MessageActionChannelMigrateFrom(
            client=client,

            title=action.title,
            chat_id=-action.chat_id,
        )


class MessageActionPinMessage(MessageAction):
    """
    """

    def __init__(
            self,
            *,
            client: "pyrogram.Client" = None,

    ):
        super().__init__(client=client)

    @staticmethod
    def _parse(client, action: raw.base.MessageAction, users: dict, chats: dict):
        if action is None:
            return None

        return MessageActionPinMessage(
            client=client,

        )


class MessageActionHistoryClear(MessageAction):
    """
    """

    def __init__(
            self,
            *,
            client: "pyrogram.Client" = None,

    ):
        super().__init__(client=client)

    @staticmethod
    def _parse(client, action: raw.base.MessageAction, users: dict, chats: dict):
        if action is None:
            return None

        return MessageActionHistoryClear(
            client=client,

        )


class MessageActionGameScore(MessageAction):
    """
    """

    def __init__(
            self,
            *,
            client: "pyrogram.Client" = None,

            game_id: int,
            score: int,
    ):
        super().__init__(client=client)

        self.game_id = game_id
        self.score = score

    @staticmethod
    def _parse(client, action: raw.base.MessageAction, users: dict, chats: dict):
        if action is None:
            return None

        return MessageActionGameScore(
            client=client,

            game_id=action.title,
            score=action.score,
        )


class MessageActionPaymentSentMe(MessageAction):
    """
    """

    # todo: add fields

    def __init__(
            self,
            *,
            client: "pyrogram.Client" = None,

    ):
        super().__init__(client=client)

    @staticmethod
    def _parse(client, action: raw.base.MessageAction, users: dict, chats: dict):
        if action is None:
            return None

        return MessageActionPaymentSentMe(
            client=client,

        )


class MessageActionPaymentSent(MessageAction):
    """
    """

    # todo: add fields

    def __init__(
            self,
            *,
            client: "pyrogram.Client" = None,

    ):
        super().__init__(client=client)

    @staticmethod
    def _parse(client, action: raw.base.MessageAction, users: dict, chats: dict):
        if action is None:
            return None

        return MessageActionPaymentSent(
            client=client,

        )


class MessageActionPhoneCall(MessageAction):
    """
    """

    # todo: add fields

    def __init__(
            self,
            *,
            client: "pyrogram.Client" = None,

    ):
        super().__init__(client=client)

    @staticmethod
    def _parse(client, action: raw.base.MessageAction, users: dict, chats: dict):
        if action is None:
            return None

        return MessageActionPhoneCall(
            client=client,

        )


class MessageActionScreenshotTaken(MessageAction):
    """
    """

    def __init__(
            self,
            *,
            client: "pyrogram.Client" = None,

    ):
        super().__init__(client=client)

    @staticmethod
    def _parse(client, action: raw.base.MessageAction, users: dict, chats: dict):
        if action is None:
            return None

        return MessageActionScreenshotTaken(
            client=client,

        )


class MessageActionCustomAction(MessageAction):
    """
    """

    def __init__(
            self,
            *,
            client: "pyrogram.Client" = None,

            message: str
    ):
        super().__init__(client=client)

        self.message = message

    @staticmethod
    def _parse(client, action: raw.base.MessageAction, users: dict, chats: dict):
        if action is None:
            return None

        return MessageActionCustomAction(
            client=client,

            message=action.message,
        )


class MessageActionBotAllowed(MessageAction):
    """
    """

    def __init__(
            self,
            *,
            client: "pyrogram.Client" = None,

            domain: str
    ):
        super().__init__(client=client)

        self.domain = domain

    @staticmethod
    def _parse(client, action: raw.base.MessageAction, users: dict, chats: dict):
        if action is None:
            return None

        return MessageActionBotAllowed(
            client=client,

            domain=action.domain,
        )


class MessageActionSecureValuesSentMe(MessageAction):
    """
    """

    # todo: add fields

    def __init__(
            self,
            *,
            client: "pyrogram.Client" = None,

    ):
        super().__init__(client=client)

    @staticmethod
    def _parse(client, action: raw.base.MessageAction, users: dict, chats: dict):
        if action is None:
            return None

        return MessageActionSecureValuesSentMe(
            client=client,

        )


class MessageActionSecureValuesSent(MessageAction):
    """
    """

    # todo: add fields

    def __init__(
            self,
            *,
            client: "pyrogram.Client" = None,

    ):
        super().__init__(client=client)

    @staticmethod
    def _parse(client, action: raw.base.MessageAction, users: dict, chats: dict):
        if action is None:
            return None

        return MessageActionSecureValuesSent(
            client=client,

        )


class MessageActionContactSignUp(MessageAction):
    """
    """

    def __init__(
            self,
            *,
            client: "pyrogram.Client" = None,

            user: "types.User" = None
    ):
        super().__init__(client=client)

        self.user = user

    @staticmethod
    def _parse(client, action: raw.base.MessageAction, users: dict, chats: dict, user_id):
        if action is None:
            return None

        return MessageActionContactSignUp(
            client=client,

            user=types.User._parse(client, users.get(user_id, None))
        )


class MessageActionGeoProximityReached(MessageAction):
    """
    """

    def __init__(
            self,
            *,
            client: "pyrogram.Client" = None,

            from_user: "types.User" = None,
            from_chat: "types.Chat" = None,
            to_user: "types.User" = None,
            to_chat: "types.Chat" = None,
            distance: int = None,
    ):
        super().__init__(client=client)

        self.from_user = from_user
        self.from_chat = from_chat
        self.to_user = to_user
        self.to_chat = to_chat
        self.distance = distance

    @staticmethod
    async def _parse(client, action: raw.base.MessageAction, users: dict, chats: dict):
        if action is None:
            return None

        from_id = getattr(action, 'from_id', None)
        from_user = None
        from_chat = None
        if from_id:
            if isinstance(from_id, raw.types.PeerUser):
                from_user = types.User._parse(client, users.get(from_id.user_id, None))
            else:
                if isinstance(from_id, raw.types.PeerChannel):
                    _peer_id = from_id.channel_id
                else:
                    _peer_id = from_id.chat_id

                from_chat = await types.Chat._parse_chat(client, chats.get(_peer_id, None))

        to_id = getattr(action, 'to_id', None)
        to_user = None
        to_chat = None
        if to_id:
            if isinstance(to_id, raw.types.PeerUser):
                to_user = types.User._parse(client, users.get(to_id.user_id, None))
            else:
                if isinstance(to_id, raw.types.PeerChannel):
                    _peer_id = to_id.channel_id
                else:
                    _peer_id = to_id.chat_id

                to_chat = await types.Chat._parse_chat(client, chats.get(_peer_id, None))

        return MessageActionGeoProximityReached(
            client=client,

            from_user=from_user,
            from_chat=from_chat,
            to_user=to_user,
            to_chat=to_chat,
            distance=action.distance
        )
