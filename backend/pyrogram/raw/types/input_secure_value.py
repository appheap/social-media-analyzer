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


class InputSecureValue(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~pyrogram.raw.base.InputSecureValue`.

    Details:
        - Layer: ``120``
        - ID: ``0xdb21d0a7``

    Parameters:
        type: :obj:`SecureValueType <pyrogram.raw.base.SecureValueType>`
        data (optional): :obj:`SecureData <pyrogram.raw.base.SecureData>`
        front_side (optional): :obj:`InputSecureFile <pyrogram.raw.base.InputSecureFile>`
        reverse_side (optional): :obj:`InputSecureFile <pyrogram.raw.base.InputSecureFile>`
        selfie (optional): :obj:`InputSecureFile <pyrogram.raw.base.InputSecureFile>`
        translation (optional): List of :obj:`InputSecureFile <pyrogram.raw.base.InputSecureFile>`
        files (optional): List of :obj:`InputSecureFile <pyrogram.raw.base.InputSecureFile>`
        plain_data (optional): :obj:`SecurePlainData <pyrogram.raw.base.SecurePlainData>`
    """

    __slots__: List[str] = ["type", "data", "front_side", "reverse_side", "selfie", "translation", "files",
                            "plain_data"]

    ID = 0xdb21d0a7
    QUALNAME = "types.InputSecureValue"

    def __init__(self, *, type: "raw.base.SecureValueType", data: "raw.base.SecureData" = None,
                 front_side: "raw.base.InputSecureFile" = None, reverse_side: "raw.base.InputSecureFile" = None,
                 selfie: "raw.base.InputSecureFile" = None,
                 translation: Union[None, List["raw.base.InputSecureFile"]] = None,
                 files: Union[None, List["raw.base.InputSecureFile"]] = None,
                 plain_data: "raw.base.SecurePlainData" = None) -> None:
        self.type = type  # SecureValueType
        self.data = data  # flags.0?SecureData
        self.front_side = front_side  # flags.1?InputSecureFile
        self.reverse_side = reverse_side  # flags.2?InputSecureFile
        self.selfie = selfie  # flags.3?InputSecureFile
        self.translation = translation  # flags.6?Vector<InputSecureFile>
        self.files = files  # flags.4?Vector<InputSecureFile>
        self.plain_data = plain_data  # flags.5?SecurePlainData

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "InputSecureValue":
        flags = Int.read(data)

        type = TLObject.read(data)

        data = TLObject.read(data) if flags & (1 << 0) else None

        front_side = TLObject.read(data) if flags & (1 << 1) else None

        reverse_side = TLObject.read(data) if flags & (1 << 2) else None

        selfie = TLObject.read(data) if flags & (1 << 3) else None

        translation = TLObject.read(data) if flags & (1 << 6) else []

        files = TLObject.read(data) if flags & (1 << 4) else []

        plain_data = TLObject.read(data) if flags & (1 << 5) else None

        return InputSecureValue(type=type, data=data, front_side=front_side, reverse_side=reverse_side, selfie=selfie,
                                translation=translation, files=files, plain_data=plain_data)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.data is not None else 0
        flags |= (1 << 1) if self.front_side is not None else 0
        flags |= (1 << 2) if self.reverse_side is not None else 0
        flags |= (1 << 3) if self.selfie is not None else 0
        flags |= (1 << 6) if self.translation is not None else 0
        flags |= (1 << 4) if self.files is not None else 0
        flags |= (1 << 5) if self.plain_data is not None else 0
        data.write(Int(flags))

        data.write(self.type.write())

        if self.data is not None:
            data.write(self.data.write())

        if self.front_side is not None:
            data.write(self.front_side.write())

        if self.reverse_side is not None:
            data.write(self.reverse_side.write())

        if self.selfie is not None:
            data.write(self.selfie.write())

        if self.translation is not None:
            data.write(Vector(self.translation))

        if self.files is not None:
            data.write(Vector(self.files))

        if self.plain_data is not None:
            data.write(self.plain_data.write())

        return data.getvalue()
