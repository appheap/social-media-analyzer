from pyrogram import raw

from ..object import Object
import telegram.client as tg


class PeerNotifySettings(Object):
    def __init__(
            self,
            *,
            client: "tg.Client" = None,
            show_previews: bool = None,
            silent: bool = None,
            mute_until: int = None,
            sound: str = None,
    ):
        super().__init__(client)

        self.show_previews = show_previews
        self.silent = silent
        self.mute_until = mute_until
        self.sound = sound

    @staticmethod
    def _parse(client, notify_settings: "raw.types.PeerNotifySettings"):
        if notify_settings is None:
            return None

        return PeerNotifySettings(
            client=client,
            show_previews=getattr(notify_settings, 'show_previews', None),
            silent=getattr(notify_settings, 'silent', None),
            mute_until=getattr(notify_settings, 'mute_until', None),
            sound=getattr(notify_settings, 'sound', None),
        )
