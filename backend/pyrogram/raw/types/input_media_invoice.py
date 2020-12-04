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


class InputMediaInvoice(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~pyrogram.raw.base.InputMedia`.

    Details:
        - Layer: ``120``
        - ID: ``0xf4e096c3``

    Parameters:
        title: ``str``
        description: ``str``
        invoice: :obj:`Invoice <pyrogram.raw.base.Invoice>`
        payload: ``bytes``
        provider: ``str``
        provider_data: :obj:`DataJSON <pyrogram.raw.base.DataJSON>`
        start_param: ``str``
        photo (optional): :obj:`InputWebDocument <pyrogram.raw.base.InputWebDocument>`
    """

    __slots__: List[str] = ["title", "description", "invoice", "payload", "provider", "provider_data", "start_param",
                            "photo"]

    ID = 0xf4e096c3
    QUALNAME = "types.InputMediaInvoice"

    def __init__(self, *, title: str, description: str, invoice: "raw.base.Invoice", payload: bytes, provider: str,
                 provider_data: "raw.base.DataJSON", start_param: str,
                 photo: "raw.base.InputWebDocument" = None) -> None:
        self.title = title  # string
        self.description = description  # string
        self.invoice = invoice  # Invoice
        self.payload = payload  # bytes
        self.provider = provider  # string
        self.provider_data = provider_data  # DataJSON
        self.start_param = start_param  # string
        self.photo = photo  # flags.0?InputWebDocument

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "InputMediaInvoice":
        flags = Int.read(data)

        title = String.read(data)

        description = String.read(data)

        photo = TLObject.read(data) if flags & (1 << 0) else None

        invoice = TLObject.read(data)

        payload = Bytes.read(data)

        provider = String.read(data)

        provider_data = TLObject.read(data)

        start_param = String.read(data)

        return InputMediaInvoice(title=title, description=description, invoice=invoice, payload=payload,
                                 provider=provider, provider_data=provider_data, start_param=start_param, photo=photo)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.photo is not None else 0
        data.write(Int(flags))

        data.write(String(self.title))

        data.write(String(self.description))

        if self.photo is not None:
            data.write(self.photo.write())

        data.write(self.invoice.write())

        data.write(Bytes(self.payload))

        data.write(String(self.provider))

        data.write(self.provider_data.write())

        data.write(String(self.start_param))

        return data.getvalue()
