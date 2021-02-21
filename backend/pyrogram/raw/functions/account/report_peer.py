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


class ReportPeer(TLObject):  # type: ignore
    """Telegram API method.

    Details:
        - Layer: ``123``
        - ID: ``0xae189d5f``

    Parameters:
        peer: :obj:`InputPeer <pyrogram.raw.base.InputPeer>`
        reason: :obj:`ReportReason <pyrogram.raw.base.ReportReason>`

    Returns:
        ``bool``
    """

    __slots__: List[str] = ["peer", "reason"]

    ID = 0xae189d5f
    QUALNAME = "functions.account.ReportPeer"

    def __init__(self, *, peer: "raw.base.InputPeer", reason: "raw.base.ReportReason") -> None:
        self.peer = peer  # InputPeer
        self.reason = reason  # ReportReason

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "ReportPeer":
        # No flags

        peer = TLObject.read(data)

        reason = TLObject.read(data)

        return ReportPeer(peer=peer, reason=reason)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        # No flags

        data.write(self.peer.write())

        data.write(self.reason.write())

        return data.getvalue()
