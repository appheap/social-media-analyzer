from pyrogram import raw

from ..object import Object
import telegram.client as tg


class PeerSettings(Object):
    def __init__(
            self,
            *,
            client: "tg.Client" = None,
            report_spam: bool = None,
            add_contact: bool = None,
            block_contact: bool = None,
            share_contact: bool = None,
            need_contacts_exception: bool = None,
            report_geo: bool = None,
            auto_archived: bool = None,
            geo_distance: int = None,
    ):
        super().__init__(client)

        self.report_spam = report_spam
        self.add_contact = add_contact
        self.block_contact = block_contact
        self.share_contact = share_contact
        self.need_contacts_exception = need_contacts_exception
        self.report_geo = report_geo
        self.auto_archived = auto_archived
        self.geo_distance = geo_distance

    @staticmethod
    def _parse(client, settings: "raw.types.PeerSettings"):
        if settings is None:
            return None

        return PeerSettings(
            client=client,
            report_spam=getattr(settings, 'report_spam', None),
            add_contact=getattr(settings, 'add_contact', None),
            block_contact=getattr(settings, 'block_contact', None),
            share_contact=getattr(settings, 'share_contact', None),
            need_contacts_exception=getattr(settings, 'need_contacts_exception', None),
            report_geo=getattr(settings, 'report_geo', None),
            auto_archived=getattr(settings, 'autoarchived', None),
            geo_distance=getattr(settings, 'geo_distance', None),
        )
