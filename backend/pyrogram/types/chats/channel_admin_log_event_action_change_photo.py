import pyrogram
from pyrogram import raw, types
from .channel_admin_log_event_action import ChannelAdminLogEventAction


class ChannelAdminLogEventActionChangePhoto(ChannelAdminLogEventAction):

    def __init__(
            self,
            *,
            client: "pyrogram.Client" = None,

            prev_photo: "types.Photo" = None,
            new_photo: "types.Photo" = None,
    ):
        super().__init__(client=client)

        self.prev_photo = prev_photo
        self.new_photo = new_photo

    @staticmethod
    def _parse(client: "pyrogram.Client", action: raw.base.ChannelAdminLogEventAction, users: dict, chats: dict):
        if action is None:
            return None

        return ChannelAdminLogEventActionChangePhoto(
            client=client,

            prev_photo=types.Photo._parse(client, getattr(action, 'prev_photo', None)),
            new_photo=types.Photo._parse(client, getattr(action, 'new_photo', None)),
        )
