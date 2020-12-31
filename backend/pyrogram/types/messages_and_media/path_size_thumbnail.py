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


class PathSizeThumbnail(Object):
    """A photo size thumbnail

    Parameters:
        data (``bytes``):
            Thumbnail data

        type (``str``):
            Thumbnail type
    """

    def __init__(
            self,
            *,
            client: "pyrogram.Client" = None,
            data: bytes,
            type: str
    ):
        super().__init__(client)

        self.data = data
        self.type = type

    @staticmethod
    def _parse(client, path_size_thumbnail: "raw.types.PhotoPathSize") -> "PathSizeThumbnail":
        return PathSizeThumbnail(
            data=path_size_thumbnail.bytes,
            type=path_size_thumbnail.type,
            client=client
        )
