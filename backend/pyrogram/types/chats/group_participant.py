from ..object import Object
from ... import raw, types
import pyrogram


class GroupParticipant(Object):
    def __init__(
            self,
            *,
            client: "pyrogram.Client" = None,
            role: str = None,
            user: "types.User" = None,
            invited_by: "types.User" = None,
            date: int = None,
    ):
        super().__init__(client)

        self.role = role
        self.user = user
        self.invited_by = invited_by
        self.date = date

    @staticmethod
    def _parse(client, chat_participant: "raw.base.ChatParticipant", users: dict):
        if chat_participant is None:
            return None

        if isinstance(chat_participant, raw.types.ChatParticipantCreator):
            role = 'creator'
        elif isinstance(chat_participant, raw.types.ChatParticipantAdmin):
            role = 'admin'
        else:
            role = 'user'
        return GroupParticipant(
            client=client,

            user=types.User._parse(client, users[chat_participant.user_id]),
            date=getattr(chat_participant, 'date', None),
            role=role,
            invited_by=types.User._parse(client, users[chat_participant.inviter_id]) if getattr(chat_participant,
                                                                                                'inviter_id',
                                                                                                None) else None,
        )
