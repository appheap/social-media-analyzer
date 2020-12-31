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


class InputChatUploadedPhoto(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~pyrogram.raw.base.InputChatPhoto`.

    Details:
        - Layer: ``122``
        - ID: ``0xc642724e``

    Parameters:
        file (optional): :obj:`InputFile <pyrogram.raw.base.InputFile>`
        video (optional): :obj:`InputFile <pyrogram.raw.base.InputFile>`
        video_start_ts (optional): ``float`` ``64-bit``
    """

    __slots__: List[str] = ["file", "video", "video_start_ts"]

    ID = 0xc642724e
    QUALNAME = "types.InputChatUploadedPhoto"

    def __init__(self, *, file: "raw.base.InputFile" = None, video: "raw.base.InputFile" = None,
                 video_start_ts: Union[None, float] = None) -> None:
        self.file = file  # flags.0?InputFile
        self.video = video  # flags.1?InputFile
        self.video_start_ts = video_start_ts  # flags.2?double

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "InputChatUploadedPhoto":
        flags = Int.read(data)

        file = TLObject.read(data) if flags & (1 << 0) else None

        video = TLObject.read(data) if flags & (1 << 1) else None

        video_start_ts = Double.read(data) if flags & (1 << 2) else None
        return InputChatUploadedPhoto(file=file, video=video, video_start_ts=video_start_ts)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.file is not None else 0
        flags |= (1 << 1) if self.video is not None else 0
        flags |= (1 << 2) if self.video_start_ts is not None else 0
        data.write(Int(flags))

        if self.file is not None:
            data.write(self.file.write())

        if self.video is not None:
            data.write(self.video.write())

        if self.video_start_ts is not None:
            data.write(Double(self.video_start_ts))

        return data.getvalue()
