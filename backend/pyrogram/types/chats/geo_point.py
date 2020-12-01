import pyrogram
from pyrogram import raw, types
from ..object import Object


class GeoPoint(Object):

    def __init__(
            self,
            *,
            client: "pyrogram.Client" = None,

            long: float = None,
            lat: float = None,
            access_hash: int = None,
            accuracy_radius: int = None,
    ):
        super().__init__(client)

        self.long = long
        self.lat = lat
        self.access_hash = access_hash
        self.accuracy_radius = accuracy_radius

    @staticmethod
    def _parse(client: "pyrogram.Client", geo_point: raw.base.GeoPoint):
        if geo_point is None:
            return None

        if isinstance(geo_point, raw.types.GeoPointEmpty):
            return None
        elif isinstance(geo_point, raw.types.GeoPoint):
            return GeoPoint(
                client=client,

                long=getattr(geo_point, 'long', None),
                lat=getattr(geo_point, 'lat', None),
                access_hash=getattr(geo_point, 'access_hash', None),
                accuracy_radius=getattr(geo_point, 'accuracy_radius', None),
            )
        else:
            return None
