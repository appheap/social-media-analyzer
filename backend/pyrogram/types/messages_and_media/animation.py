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

from struct import pack
from typing import List

import pyrogram
from pyrogram import raw
from pyrogram import types
from pyrogram.utils import encode_file_id, encode_file_ref
from ..object import Object


class Animation(Object):
    """An animation file (GIF or H.264/MPEG-4 AVC video without sound).

    Parameters:
        file_id (``str``):
            Unique identifier for this file.

        file_ref (``str``):
            Up to date file reference.

        width (``int``):
            Animation width as defined by sender.

        height (``int``):
            Animation height as defined by sender.

        duration (``int``):
            Duration of the animation in seconds as defined by sender.

        file_name (``str``, *optional*):
            Animation file name.

        mime_type (``str``, *optional*):
            Mime type of a file as defined by sender.

        file_size (``int``, *optional*):
            File size.

        date (``int``, *optional*):
            Date the animation was sent in Unix time.

        thumbs (List of :obj:`~pyrogram.types.Thumbnail`, *optional*):
            Animation thumbnails.
    """

    def __init__(
            self,
            *,
            client: "pyrogram.Client" = None,
            file_id: str,
            file_ref: str,
            width: int,
            height: int,
            duration: int,
            file_name: str = None,
            mime_type: str = None,
            file_size: int = None,
            date: int = None,
            thumbs: List["types.Thumbnail"] = None
    ):
        super().__init__(client)

        self.file_id = file_id
        self.file_ref = file_ref
        self.file_name = file_name
        self.mime_type = mime_type
        self.file_size = file_size
        self.date = date
        self.width = width
        self.height = height
        self.duration = duration
        self.thumbs = thumbs

    @staticmethod
    def _parse(
            client,
            animation: "raw.types.Document",
            video_attributes: "raw.types.DocumentAttributeVideo",
            file_name: str
    ) -> "Animation":
        return Animation(
            file_id=encode_file_id(
                pack(
                    "<iiqq",
                    10,
                    animation.dc_id,
                    animation.id,
                    animation.access_hash
                )
            ),
            file_ref=encode_file_ref(animation.file_reference),
            width=getattr(video_attributes, "w", 0),
            height=getattr(video_attributes, "h", 0),
            duration=getattr(video_attributes, "duration", 0),
            mime_type=animation.mime_type,
            file_size=animation.size,
            file_name=file_name,
            date=animation.date,
            thumbs=types.Thumbnail._parse(client, animation),
            client=client
        )
