from ..object import Object
import pyrogram
from pyrogram import raw, types
from pyrogram import utils


class Group(Object):
    def __init__(
            self,
            *,
            client: "pyrogram.Client" = None,
            id: int = None,
            is_forbidden: bool = None,
            is_empty: bool = None,
            is_creator: bool = None,
            is_kicked: bool = None,
            left: bool = None,
            is_deactivated: bool = None,
            title: str = None,
            photo: "types.Photo" = None,
            members_count: int = None,
            create_date: int = None,
            migrated_to: "types.ChannelFull" = None,
            admin_rights: "types.ChatAdminRights" = None,
            default_banned_rights: "types.ChatPermissions" = None,
            version: int = None,

    ):
        super().__init__(client)

        self.id = id
        self.is_forbidden = is_forbidden
        self.is_empty = is_empty
        self.is_creator = is_creator
        self.is_kicked = is_kicked
        self.left = left
        self.is_deactivated = is_deactivated
        self.title = title
        self.photo = photo
        self.members_count = members_count
        self.create_date = create_date
        self.migrated_to = migrated_to
        self.admin_rights = admin_rights
        self.default_banned_rights = default_banned_rights
        self.version = version

    @staticmethod
    async def _parse(client, chat: "raw.base.Chat"):
        if chat is None:
            return None

        peer_id = -chat.id
        return Group(
            client=client,

            id=peer_id,
            is_forbidden=isinstance(chat, raw.types.ChatForbidden),
            is_empty=isinstance(chat, raw.types.ChatEmpty),
            is_creator=getattr(chat, 'creator', None),
            is_kicked=getattr(chat, 'kicked', None),
            left=getattr(chat, 'left', None),
            is_deactivated=getattr(chat, 'deactivated', None),
            title=getattr(chat, 'title', None),
            photo=types.ChatPhoto._parse(client, getattr(chat, "photo", None), peer_id, 0),
            members_count=getattr(chat, 'participants_count', None),
            create_date=getattr(chat, 'date', None),
            migrated_to=types.Channel._parse_input_channel(client, getattr(chat, 'migrated_to', None)),
            admin_rights=types.ChatAdminRights._parse(getattr(chat, 'admin_rights', None)),
            default_banned_rights=types.ChatPermissions._parse(getattr(chat, 'default_banned_rights', None)),
            version=getattr(chat, 'version', None),
        )
