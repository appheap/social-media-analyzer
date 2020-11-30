from pyrogram import raw
from ..object import Object


class Restriction(Object):
    """A restriction applied to bots_and_keyboards or chats.

    Parameters:
        platform (``str``):
            The platform the restriction is applied to, e.g. "ios", "android"

        reason (``str``):
            The restriction reason, e.g. "porn", "copyright".

        text (``str``):
            The restriction text.
    """

    def __init__(self, *, platform: str, reason: str, text: str):
        super().__init__(None)

        self.platform = platform
        self.reason = reason
        self.text = text

    @staticmethod
    def _parse(restriction: "raw.types.RestrictionReason") -> "Restriction":
        return Restriction(
            platform=restriction.platform,
            reason=restriction.reason,
            text=restriction.text
        )
