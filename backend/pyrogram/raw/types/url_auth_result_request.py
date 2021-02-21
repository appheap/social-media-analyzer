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


class UrlAuthResultRequest(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~pyrogram.raw.base.UrlAuthResult`.

    Details:
        - Layer: ``123``
        - ID: ``0x92d33a0e``

    Parameters:
        bot: :obj:`User <pyrogram.raw.base.User>`
        domain: ``str``
        request_write_access (optional): ``bool``

    See Also:
        This object can be returned by 2 methods:

        .. hlist::
            :columns: 2

            - :obj:`messages.RequestUrlAuth <pyrogram.raw.functions.messages.RequestUrlAuth>`
            - :obj:`messages.AcceptUrlAuth <pyrogram.raw.functions.messages.AcceptUrlAuth>`
    """

    __slots__: List[str] = ["bot", "domain", "request_write_access"]

    ID = 0x92d33a0e
    QUALNAME = "types.UrlAuthResultRequest"

    def __init__(self, *, bot: "raw.base.User", domain: str, request_write_access: Union[None, bool] = None) -> None:
        self.bot = bot  # User
        self.domain = domain  # string
        self.request_write_access = request_write_access  # flags.0?true

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "UrlAuthResultRequest":
        flags = Int.read(data)

        request_write_access = True if flags & (1 << 0) else False
        bot = TLObject.read(data)

        domain = String.read(data)

        return UrlAuthResultRequest(bot=bot, domain=domain, request_write_access=request_write_access)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.request_write_access else 0
        data.write(Int(flags))

        data.write(self.bot.write())

        data.write(String(self.domain))

        return data.getvalue()
