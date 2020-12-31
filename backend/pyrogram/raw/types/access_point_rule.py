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


class AccessPointRule(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~pyrogram.raw.base.AccessPointRule`.

    Details:
        - Layer: ``122``
        - ID: ``0x4679b65f``

    Parameters:
        phone_prefix_rules: ``str``
        dc_id: ``int`` ``32-bit``
        ips: List of :obj:`IpPort <pyrogram.raw.base.IpPort>`
    """

    __slots__: List[str] = ["phone_prefix_rules", "dc_id", "ips"]

    ID = 0x4679b65f
    QUALNAME = "types.AccessPointRule"

    def __init__(self, *, phone_prefix_rules: str, dc_id: int, ips: List["raw.base.IpPort"]) -> None:
        self.phone_prefix_rules = phone_prefix_rules  # string
        self.dc_id = dc_id  # int
        self.ips = ips  # vector<IpPort>

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "AccessPointRule":
        # No flags

        phone_prefix_rules = String.read(data)

        dc_id = Int.read(data)

        ips = TLObject.read(data)

        return AccessPointRule(phone_prefix_rules=phone_prefix_rules, dc_id=dc_id, ips=ips)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        # No flags

        data.write(String(self.phone_prefix_rules))

        data.write(Int(self.dc_id))

        data.write(Vector(self.ips))

        return data.getvalue()
