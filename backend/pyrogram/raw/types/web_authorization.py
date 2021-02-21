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


class WebAuthorization(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~pyrogram.raw.base.WebAuthorization`.

    Details:
        - Layer: ``123``
        - ID: ``0xcac943f2``

    Parameters:
        hash: ``int`` ``64-bit``
        bot_id: ``int`` ``32-bit``
        domain: ``str``
        browser: ``str``
        platform: ``str``
        date_created: ``int`` ``32-bit``
        date_active: ``int`` ``32-bit``
        ip: ``str``
        region: ``str``
    """

    __slots__: List[str] = ["hash", "bot_id", "domain", "browser", "platform", "date_created", "date_active", "ip",
                            "region"]

    ID = 0xcac943f2
    QUALNAME = "types.WebAuthorization"

    def __init__(self, *, hash: int, bot_id: int, domain: str, browser: str, platform: str, date_created: int,
                 date_active: int, ip: str, region: str) -> None:
        self.hash = hash  # long
        self.bot_id = bot_id  # int
        self.domain = domain  # string
        self.browser = browser  # string
        self.platform = platform  # string
        self.date_created = date_created  # int
        self.date_active = date_active  # int
        self.ip = ip  # string
        self.region = region  # string

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "WebAuthorization":
        # No flags

        hash = Long.read(data)

        bot_id = Int.read(data)

        domain = String.read(data)

        browser = String.read(data)

        platform = String.read(data)

        date_created = Int.read(data)

        date_active = Int.read(data)

        ip = String.read(data)

        region = String.read(data)

        return WebAuthorization(hash=hash, bot_id=bot_id, domain=domain, browser=browser, platform=platform,
                                date_created=date_created, date_active=date_active, ip=ip, region=region)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        # No flags

        data.write(Long(self.hash))

        data.write(Int(self.bot_id))

        data.write(String(self.domain))

        data.write(String(self.browser))

        data.write(String(self.platform))

        data.write(Int(self.date_created))

        data.write(Int(self.date_active))

        data.write(String(self.ip))

        data.write(String(self.region))

        return data.getvalue()
