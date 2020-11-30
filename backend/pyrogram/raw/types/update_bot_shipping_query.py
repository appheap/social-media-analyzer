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


class UpdateBotShippingQuery(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~pyrogram.raw.base.Update`.

    Details:
        - Layer: ``117``
        - ID: ``0xe0cdc940``

    Parameters:
        query_id: ``int`` ``64-bit``
        user_id: ``int`` ``32-bit``
        payload: ``bytes``
        shipping_address: :obj:`PostAddress <pyrogram.raw.base.PostAddress>`
    """

    __slots__: List[str] = ["query_id", "user_id", "payload", "shipping_address"]

    ID = 0xe0cdc940
    QUALNAME = "types.UpdateBotShippingQuery"

    def __init__(self, *, query_id: int, user_id: int, payload: bytes,
                 shipping_address: "raw.base.PostAddress") -> None:
        self.query_id = query_id  # long
        self.user_id = user_id  # int
        self.payload = payload  # bytes
        self.shipping_address = shipping_address  # PostAddress

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "UpdateBotShippingQuery":
        # No flags

        query_id = Long.read(data)

        user_id = Int.read(data)

        payload = Bytes.read(data)

        shipping_address = TLObject.read(data)

        return UpdateBotShippingQuery(query_id=query_id, user_id=user_id, payload=payload,
                                      shipping_address=shipping_address)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        # No flags

        data.write(Long(self.query_id))

        data.write(Int(self.user_id))

        data.write(Bytes(self.payload))

        data.write(self.shipping_address.write())

        return data.getvalue()
