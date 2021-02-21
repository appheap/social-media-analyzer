#  Pyrogram - Telegram MTProto API Client Library for Python
#  Copyright (C) 2017-2021 Dan <https://github.com/delivrance>
#
#  This file is part of Pyrogram.
#
#  Pyrogram is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Lesser General Public License as published
#  by the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  Pyrogram is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public License
#  along with Pyrogram.  If not, see <http://www.gnu.org/licenses/>.

import pyrogram

from pyrogram import raw
from ..object import Object
from pyrogram import types


class GeoLive(Object):
    """Indicates a live geolocation

    Parameters:
        geo (``types.GeoPoint``):
            geoPoint.

        period (``int``):
            Validity period of provided geolocation.

        heading (``int``):
            For live locations, a direction in which the location moves, in degrees; 1-360

        proximity_notification_radius (``int``):
            For live locations, a maximum distance to another chat member for proximity alerts, in meters (0-100000).

    """

    def __init__(
            self,
            *,
            client: "pyrogram.Client" = None,

            geo: "types.GeoPoint",
            period: int,
            heading: int = None,
            proximity_notification_radius: int = None,
    ):
        super().__init__(client)

        self.geo = geo
        self.period = period
        self.heading = heading
        self.proximity_notification_radius = proximity_notification_radius

    @staticmethod
    def _parse(client, geo_live: "raw.types.MessageMediaGeoLive") -> "GeoLive":
        if isinstance(geo_live, raw.types.MessageMediaGeoLive):
            return GeoLive(
                client=client,

                geo=types.GeoPoint._parse(client, geo_live.geo),
                period=geo_live.period,
                heading=getattr(geo_live, 'heading', None),
                proximity_notification_radius=getattr(geo_live, 'proximity_notification_radius', None),
            )
