#  Pyrogram - Telegram MTProto API Client Library for Python
#  Copyright (C) 2017-2020 Dan <https://github.com/delivrance>
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


class Geo(Object):
    """A point on the map.

    Parameters:
        geo (``types.GeoPoint``):
            geoPoint.

    """

    def __init__(
            self,
            *,
            client: "pyrogram.Client" = None,
            geo: "types.GeoPoint",
    ):
        super().__init__(client)

        self.geo = geo

    @staticmethod
    def _parse(client, geo: "raw.types.MessageMediaGeo") -> "Geo":
        if isinstance(geo, raw.types.MessageMediaGeo):
            return Geo(
                client=client,

                geo=types.GeoPoint._parse(client, geo.geo)
            )
