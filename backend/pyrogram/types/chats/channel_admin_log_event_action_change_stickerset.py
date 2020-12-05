import pyrogram
from pyrogram import raw, types
from .channel_admin_log_event_action import ChannelAdminLogEventAction


class ChannelAdminLogEventActionChangeStickerSet(ChannelAdminLogEventAction):

    def __init__(
            self,
            *,
            client: "pyrogram.Client" = None,

            prev_stickerset: str = None,
            new_stickerset: str = None,
    ):
        super().__init__(client=client)

        self.prev_stickerset = prev_stickerset
        self.new_stickerset = new_stickerset

    @staticmethod
    async def _parse(client: "pyrogram.Client", action: raw.base.ChannelAdminLogEventAction, users: dict, chats: dict):
        if action is None:
            return None

        return ChannelAdminLogEventActionChangeStickerSet(
            client=client,

            prev_stickerset=await types.StickerSet._parse_from_input_stickerset(client,
                                                                                getattr(action, 'prev_stickerset',
                                                                                        None)),
            new_stickerset=await types.StickerSet._parse_from_input_stickerset(client,
                                                                               getattr(action, 'new_stickerset', None)),
        )
