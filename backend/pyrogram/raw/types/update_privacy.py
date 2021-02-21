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


class UpdatePrivacy(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~pyrogram.raw.base.Update`.

    Details:
        - Layer: ``123``
        - ID: ``0xee3b272a``

    Parameters:
        key: :obj:`PrivacyKey <pyrogram.raw.base.PrivacyKey>`
        rules: List of :obj:`PrivacyRule <pyrogram.raw.base.PrivacyRule>`
    """

    __slots__: List[str] = ["key", "rules"]

    ID = 0xee3b272a
    QUALNAME = "types.UpdatePrivacy"

    def __init__(self, *, key: "raw.base.PrivacyKey", rules: List["raw.base.PrivacyRule"]) -> None:
        self.key = key  # PrivacyKey
        self.rules = rules  # Vector<PrivacyRule>

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "UpdatePrivacy":
        # No flags

        key = TLObject.read(data)

        rules = TLObject.read(data)

        return UpdatePrivacy(key=key, rules=rules)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        # No flags

        data.write(self.key.write())

        data.write(Vector(self.rules))

        return data.getvalue()
