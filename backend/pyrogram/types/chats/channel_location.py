import pyrogram
from pyrogram import types, raw
from ..object import Object


class ChannelLocation(Object):
    def __init__(
            self,
            *,
            client: "pyrogram.Client" = None,
            geo_point: "types.GeoPoint" = None,
            address: str = None,
    ):
        super().__init__(client)

        self.geo_point = geo_point
        self.address = address

    @staticmethod
    def _parse(client, channel_location: "raw.base.ChannelLocation"):
        if channel_location is None:
            return None

        if isinstance(channel_location, raw.types.ChannelLocationEmpty):
            return None
        elif isinstance(channel_location, raw.types.ChannelLocation):
            return ChannelLocation(
                client=client,

                geo_point=types.GeoPoint._parse(client, getattr(channel_location, 'geo_point', None)),
                address=getattr(channel_location, 'address', None),
            )
        else:
            return None
