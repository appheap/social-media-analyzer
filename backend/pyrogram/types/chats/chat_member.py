from typing import Union

import pyrogram
from ..object import Object
from pyrogram import raw, types


class ChatMember(Object):
    def __init__(
            self,
            *,
            client: "pyrogram.Client" = None,

            user: "types.User" = None,
            join_date: int = None,
            invited_by: "types.User" = None,
            status: str = None,
            admin_rights: "types.ChatAdminRights" = None,

            can_promote_admins: bool = None,
            is_current_user: bool = None,
            promoted_by: "types.User" = None,

            is_member: bool = None,
            kicked_by: "types.User" = None,
            banned_rights: "types.ChatPermissions" = None,
    ):
        super().__init__(client=client)

        self.user = user
        self.join_date = join_date
        self.invited_by = invited_by
        self.status = status
        self.admin_rights = admin_rights

        self.can_promote_admins = can_promote_admins
        self.is_current_user = is_current_user
        self.promoted_by = promoted_by

        self.is_member = is_member
        self.kicked_by = kicked_by
        self.banned_rights = banned_rights

    @staticmethod
    def _parse(
            client: "pyrogram.Client",
            participant: Union[raw.base.ChannelParticipant, raw.base.ChatParticipant],
            users: dict,
    ) -> "ChatMember":

        if participant is None:
            return None

        status = 'member'
        if isinstance(participant, (raw.types.ChannelParticipant,
                                    raw.types.ChannelParticipantSelf,
                                    raw.types.ChatParticipant,)):
            status = 'member'
        elif isinstance(participant, (raw.types.ChannelParticipantCreator, raw.types.ChatParticipantCreator)):
            status = 'creator'

        elif isinstance(participant, (raw.types.ChatParticipantAdmin, raw.types.ChannelParticipantAdmin)):
            status = 'administrator'
        elif isinstance(participant, raw.types.ChannelParticipantBanned):
            status = "kicked" if participant.banned_rights.view_messages else "restricted",

        return ChatMember(
            client=client,

            user=types.User._parse(client, users.get(getattr(participant, 'user_id', None), None)),
            join_date=getattr(participant, 'date', None),
            invited_by=types.User._parse(client, users.get(participant.inviter_id, None)) if getattr(
                participant, 'inviter_id', None) else None,
            status=status,
            admin_rights=types.ChatAdminRights._parse(getattr(participant, 'admin_rights', None)),

            can_promote_admins=getattr(participant, 'can_edit', None),
            is_current_user=getattr(participant, 'is_self', None),
            promoted_by=types.User._parse(client, users.get(participant.promoted_by, None)) if getattr(
                participant, 'promoted_by', None) else None,

            is_member=getattr(participant, 'left', None),
            kicked_by=types.User._parse(client, users.get(participant.kicked_by, None)) if getattr(
                participant, 'kicked_by', None) else None,
            banned_rights=types.ChatPermissions._parse(getattr(participant, 'banned_rights', None)),
        )
