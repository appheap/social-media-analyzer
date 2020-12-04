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


class SetBotShippingResults(TLObject):  # type: ignore
    """Telegram API method.

    Details:
        - Layer: ``120``
        - ID: ``0xe5f672fa``

    Parameters:
        query_id: ``int`` ``64-bit``
        error (optional): ``str``
        shipping_options (optional): List of :obj:`ShippingOption <pyrogram.raw.base.ShippingOption>`

    Returns:
        ``bool``
    """

    __slots__: List[str] = ["query_id", "error", "shipping_options"]

    ID = 0xe5f672fa
    QUALNAME = "functions.messages.SetBotShippingResults"

    def __init__(self, *, query_id: int, error: Union[None, str] = None,
                 shipping_options: Union[None, List["raw.base.ShippingOption"]] = None) -> None:
        self.query_id = query_id  # long
        self.error = error  # flags.0?string
        self.shipping_options = shipping_options  # flags.1?Vector<ShippingOption>

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "SetBotShippingResults":
        flags = Int.read(data)

        query_id = Long.read(data)

        error = String.read(data) if flags & (1 << 0) else None
        shipping_options = TLObject.read(data) if flags & (1 << 1) else []

        return SetBotShippingResults(query_id=query_id, error=error, shipping_options=shipping_options)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.error is not None else 0
        flags |= (1 << 1) if self.shipping_options is not None else 0
        data.write(Int(flags))

        data.write(Long(self.query_id))

        if self.error is not None:
            data.write(String(self.error))

        if self.shipping_options is not None:
            data.write(Vector(self.shipping_options))

        return data.getvalue()
