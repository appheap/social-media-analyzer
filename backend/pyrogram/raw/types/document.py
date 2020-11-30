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

from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Union, Any


# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #


class Document(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~pyrogram.raw.base.Document`.

    Details:
        - Layer: ``117``
        - ID: ``0x1e87342b``

    Parameters:
        id: ``int`` ``64-bit``
        access_hash: ``int`` ``64-bit``
        file_reference: ``bytes``
        date: ``int`` ``32-bit``
        mime_type: ``str``
        size: ``int`` ``32-bit``
        dc_id: ``int`` ``32-bit``
        attributes: List of :obj:`DocumentAttribute <pyrogram.raw.base.DocumentAttribute>`
        thumbs (optional): List of :obj:`PhotoSize <pyrogram.raw.base.PhotoSize>`
        video_thumbs (optional): List of :obj:`VideoSize <pyrogram.raw.base.VideoSize>`

    See Also:
        This object can be returned by 2 methods:

        .. hlist::
            :columns: 2

            - :obj:`account.UploadTheme <pyrogram.raw.functions.account.UploadTheme>`
            - :obj:`messages.GetDocumentByHash <pyrogram.raw.functions.messages.GetDocumentByHash>`
    """

    __slots__: List[str] = ["id", "access_hash", "file_reference", "date", "mime_type", "size", "dc_id", "attributes",
                            "thumbs", "video_thumbs"]

    ID = 0x1e87342b
    QUALNAME = "types.Document"

    def __init__(self, *, id: int, access_hash: int, file_reference: bytes, date: int, mime_type: str, size: int,
                 dc_id: int, attributes: List["raw.base.DocumentAttribute"],
                 thumbs: Union[None, List["raw.base.PhotoSize"]] = None,
                 video_thumbs: Union[None, List["raw.base.VideoSize"]] = None) -> None:
        self.id = id  # long
        self.access_hash = access_hash  # long
        self.file_reference = file_reference  # bytes
        self.date = date  # int
        self.mime_type = mime_type  # string
        self.size = size  # int
        self.dc_id = dc_id  # int
        self.attributes = attributes  # Vector<DocumentAttribute>
        self.thumbs = thumbs  # flags.0?Vector<PhotoSize>
        self.video_thumbs = video_thumbs  # flags.1?Vector<VideoSize>

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "Document":
        flags = Int.read(data)

        id = Long.read(data)

        access_hash = Long.read(data)

        file_reference = Bytes.read(data)

        date = Int.read(data)

        mime_type = String.read(data)

        size = Int.read(data)

        thumbs = TLObject.read(data) if flags & (1 << 0) else []

        video_thumbs = TLObject.read(data) if flags & (1 << 1) else []

        dc_id = Int.read(data)

        attributes = TLObject.read(data)

        return Document(id=id, access_hash=access_hash, file_reference=file_reference, date=date, mime_type=mime_type,
                        size=size, dc_id=dc_id, attributes=attributes, thumbs=thumbs, video_thumbs=video_thumbs)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.thumbs is not None else 0
        flags |= (1 << 1) if self.video_thumbs is not None else 0
        data.write(Int(flags))

        data.write(Long(self.id))

        data.write(Long(self.access_hash))

        data.write(Bytes(self.file_reference))

        data.write(Int(self.date))

        data.write(String(self.mime_type))

        data.write(Int(self.size))

        if self.thumbs is not None:
            data.write(Vector(self.thumbs))

        if self.video_thumbs is not None:
            data.write(Vector(self.video_thumbs))

        data.write(Int(self.dc_id))

        data.write(Vector(self.attributes))

        return data.getvalue()
