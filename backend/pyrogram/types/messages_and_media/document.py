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


class Document(Object):
    """A generic file (as opposed to photos, voice messages, audio files, ...).

    Parameters:
        file_id (``str``):
            Unique file identifier.

        file_ref (``str``):
            Up to date file reference.

        file_name (``str``, *optional*):
            Original filename as defined by sender.

        mime_type (``str``, *optional*):
            MIME type of the file as defined by sender.

        file_size (``int``, *optional*):
            File size.

        date (``int``, *optional*):
            Date the document was sent in Unix time.

        thumbs (List of :obj:`~pyrogram.types.Thumbnail`, *optional*):
            Document thumbnails as defined by sender.
    """

    def __init__(
            self,
            *,
            client: "pyrogram.Client" = None,
            file_id: str,
            file_ref: str,
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
        self.thumbs = thumbs

    @staticmethod
    def _parse(client, document: "raw.types.Document", file_name: str) -> "Document":
        return Document(
            file_id=encode_file_id(
                pack(
                    "<iiqq",
                    5,
                    document.dc_id,
                    document.id,
                    document.access_hash
                )
            ),
            file_ref=encode_file_ref(document.file_reference),
            file_name=file_name,
            mime_type=document.mime_type,
            file_size=document.size,
            date=document.date,
            thumbs=types.Thumbnail._parse(client, document),
            client=client
        )
