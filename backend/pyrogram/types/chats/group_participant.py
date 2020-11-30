from ..object import Object


class GroupParticipant(Object):
    def __init__(
            self,
            *,
            client: "Client" = None,
            role: str = None,
            user: "User" = None,
            invited_by: "User" = None,
            date: int = None,
    ):
        super().__init__(client)

        self.role = role
        self.user = user
        self.invited_by = invited_by
        self.date = date
