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


class SecureValue(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~pyrogram.raw.base.SecureValue`.

    Details:
        - Layer: ``117``
        - ID: ``0x187fa0ca``

    Parameters:
        type: :obj:`SecureValueType <pyrogram.raw.base.SecureValueType>`
        hash: ``bytes``
        data (optional): :obj:`SecureData <pyrogram.raw.base.SecureData>`
        front_side (optional): :obj:`SecureFile <pyrogram.raw.base.SecureFile>`
        reverse_side (optional): :obj:`SecureFile <pyrogram.raw.base.SecureFile>`
        selfie (optional): :obj:`SecureFile <pyrogram.raw.base.SecureFile>`
        translation (optional): List of :obj:`SecureFile <pyrogram.raw.base.SecureFile>`
        files (optional): List of :obj:`SecureFile <pyrogram.raw.base.SecureFile>`
        plain_data (optional): :obj:`SecurePlainData <pyrogram.raw.base.SecurePlainData>`

    See Also:
        This object can be returned by 3 methods:

        .. hlist::
            :columns: 2

            - :obj:`account.GetAllSecureValues <pyrogram.raw.functions.account.GetAllSecureValues>`
            - :obj:`account.GetSecureValue <pyrogram.raw.functions.account.GetSecureValue>`
            - :obj:`account.SaveSecureValue <pyrogram.raw.functions.account.SaveSecureValue>`
    """

    __slots__: List[str] = ["type", "hash", "data", "front_side", "reverse_side", "selfie", "translation", "files",
                            "plain_data"]

    ID = 0x187fa0ca
    QUALNAME = "types.SecureValue"

    def __init__(self, *, type: "raw.base.SecureValueType", hash: bytes, data: "raw.base.SecureData" = None,
                 front_side: "raw.base.SecureFile" = None, reverse_side: "raw.base.SecureFile" = None,
                 selfie: "raw.base.SecureFile" = None, translation: Union[None, List["raw.base.SecureFile"]] = None,
                 files: Union[None, List["raw.base.SecureFile"]] = None,
                 plain_data: "raw.base.SecurePlainData" = None) -> None:
        self.type = type  # SecureValueType
        self.hash = hash  # bytes
        self.data = data  # flags.0?SecureData
        self.front_side = front_side  # flags.1?SecureFile
        self.reverse_side = reverse_side  # flags.2?SecureFile
        self.selfie = selfie  # flags.3?SecureFile
        self.translation = translation  # flags.6?Vector<SecureFile>
        self.files = files  # flags.4?Vector<SecureFile>
        self.plain_data = plain_data  # flags.5?SecurePlainData

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "SecureValue":
        flags = Int.read(data)

        type = TLObject.read(data)

        data = TLObject.read(data) if flags & (1 << 0) else None

        front_side = TLObject.read(data) if flags & (1 << 1) else None

        reverse_side = TLObject.read(data) if flags & (1 << 2) else None

        selfie = TLObject.read(data) if flags & (1 << 3) else None

        translation = TLObject.read(data) if flags & (1 << 6) else []

        files = TLObject.read(data) if flags & (1 << 4) else []

        plain_data = TLObject.read(data) if flags & (1 << 5) else None

        hash = Bytes.read(data)

        return SecureValue(type=type, hash=hash, data=data, front_side=front_side, reverse_side=reverse_side,
                           selfie=selfie, translation=translation, files=files, plain_data=plain_data)

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

        data.write(Bytes(self.hash))

        return data.getvalue()
