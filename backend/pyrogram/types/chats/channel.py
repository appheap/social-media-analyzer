from typing import List

from ..object import Object
from pyrogram import raw, utils, types
import pyrogram


class Channel(Object):
    def __init__(
            self,
            *,
            client: "pyrogram.Client" = None,
            id: int = None,
            title: str = None,
            is_forbidden: bool = None,
            forbidden_until: int = None,
            username: str = None,
            photo: "types.ChatPhoto" = None,
            is_creator: bool = None,
            left: bool = None,
            is_broadcast: bool = None,
            is_verified: bool = None,
            is_supergroup: bool = None,
            is_restricted: bool = None,
            signatures_enabled: bool = None,
            min: bool = None,
            is_scam: bool = None,
            has_private_join_link: bool = None,
            has_geo: bool = None,
            slow_mode: bool = None,
            access_hash: int = None,
            date: int = None,
            version: int = None,
            restrictions: List["types.Restriction"] = None,
            admin_rights: "types.ChatAdminRights" = None,
            banned_rights: "types.ChatPermissions" = None,
            default_banned_rights: "types.ChatPermissions" = None,
            members_count: int = None,

    ):
        super().__init__(client)

        self.id = id
        self.title = title
        self.is_forbidden = is_forbidden
        self.forbidden_until = forbidden_until
        self.username = username
        self.photo = photo
        self.is_creator = is_creator
        self.left = left
        self.is_broadcast = is_broadcast
        self.is_verified = is_verified
        self.is_supergroup = is_supergroup
        self.is_restricted = is_restricted
        self.signatures_enabled = signatures_enabled
        self.min = min
        self.is_scam = is_scam
        self.has_private_join_link = has_private_join_link
        self.has_geo = has_geo
        self.slow_mode = slow_mode
        self.access_hash = access_hash
        self.date = date
        self.version = version
        self.restrictions = restrictions
        self.admin_rights = admin_rights
        self.banned_rights = banned_rights
        self.default_banned_rights = default_banned_rights
        self.members_count = members_count

    @staticmethod
    def _parse(client, channel):
        if channel is None:
            return None

        peer_id = utils.get_channel_id(channel.id)

        return Channel(
            client=client,

            id=peer_id,
            title=getattr(channel, 'title', None),
            is_forbidden=isinstance(channel, raw.types.ChannelForbidden),
            forbidden_until=getattr(channel, 'until_date', None),
            username=getattr(channel, 'username', None),
            photo=types.ChatPhoto._parse(client, getattr(channel, "photo", None), peer_id,
                                         getattr(channel, 'access_hash', 0)),
            is_creator=getattr(channel, 'creator', None),
            left=getattr(channel, 'left', None),
            is_broadcast=getattr(channel, 'broadcast', None),
            is_verified=getattr(channel, 'verified', None),
            is_supergroup=getattr(channel, 'megagroup', None),
            is_restricted=getattr(channel, 'restricted', None),
            signatures_enabled=getattr(channel, 'signatures', None),
            min=getattr(channel, 'min', None),
            is_scam=getattr(channel, 'scam', None),
            has_private_join_link=getattr(channel, 'has_link', None),
            has_geo=getattr(channel, 'has_geo', None),
            slow_mode=getattr(channel, 'slowmode_enabled', None),
            access_hash=getattr(channel, 'access_hash', None),
            date=getattr(channel, 'date', None),
            version=getattr(channel, 'version', None),
            restrictions=types.List(
                [types.Restriction._parse(r) for r in getattr(channel, 'restriction_reason', [])]) or None,
            admin_rights=types.ChatAdminRights._parse(getattr(channel, 'admin_rights', None)),
            banned_rights=types.ChatPermissions._parse(getattr(channel, 'banned_rights', None)),
            default_banned_rights=types.ChatPermissions._parse(getattr(channel, 'default_banned_rights', None)),
            members_count=getattr(channel, 'participants_count', None),

        )

    @staticmethod
    def _parse_input_channel(client: "pyrogram.Client", input_channel: raw.types.InputChannel):
        if input_channel is None:
            return None

        peer_id = utils.get_channel_id(input_channel.channel_id)

        return Channel(
            client=client,
            id=peer_id,
            access_hash=getattr(input_channel, 'access_hash', None),
        )
