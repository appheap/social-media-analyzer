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


class PeerSettings(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~pyrogram.raw.base.PeerSettings`.

    Details:
        - Layer: ``117``
        - ID: ``0x733f2961``

    Parameters:
        report_spam (optional): ``bool``
        add_contact (optional): ``bool``
        block_contact (optional): ``bool``
        share_contact (optional): ``bool``
        need_contacts_exception (optional): ``bool``
        report_geo (optional): ``bool``
        autoarchived (optional): ``bool``
        geo_distance (optional): ``int`` ``32-bit``

    See Also:
        This object can be returned by 1 method:

        .. hlist::
            :columns: 2

            - :obj:`messages.GetPeerSettings <pyrogram.raw.functions.messages.GetPeerSettings>`
    """

    __slots__: List[str] = ["report_spam", "add_contact", "block_contact", "share_contact", "need_contacts_exception",
                            "report_geo", "autoarchived", "geo_distance"]

    ID = 0x733f2961
    QUALNAME = "types.PeerSettings"

    def __init__(self, *, report_spam: Union[None, bool] = None, add_contact: Union[None, bool] = None,
                 block_contact: Union[None, bool] = None, share_contact: Union[None, bool] = None,
                 need_contacts_exception: Union[None, bool] = None, report_geo: Union[None, bool] = None,
                 autoarchived: Union[None, bool] = None, geo_distance: Union[None, int] = None) -> None:
        self.report_spam = report_spam  # flags.0?true
        self.add_contact = add_contact  # flags.1?true
        self.block_contact = block_contact  # flags.2?true
        self.share_contact = share_contact  # flags.3?true
        self.need_contacts_exception = need_contacts_exception  # flags.4?true
        self.report_geo = report_geo  # flags.5?true
        self.autoarchived = autoarchived  # flags.7?true
        self.geo_distance = geo_distance  # flags.6?int

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "PeerSettings":
        flags = Int.read(data)

        report_spam = True if flags & (1 << 0) else False
        add_contact = True if flags & (1 << 1) else False
        block_contact = True if flags & (1 << 2) else False
        share_contact = True if flags & (1 << 3) else False
        need_contacts_exception = True if flags & (1 << 4) else False
        report_geo = True if flags & (1 << 5) else False
        autoarchived = True if flags & (1 << 7) else False
        geo_distance = Int.read(data) if flags & (1 << 6) else None
        return PeerSettings(report_spam=report_spam, add_contact=add_contact, block_contact=block_contact,
                            share_contact=share_contact, need_contacts_exception=need_contacts_exception,
                            report_geo=report_geo, autoarchived=autoarchived, geo_distance=geo_distance)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.report_spam is not None else 0
        flags |= (1 << 1) if self.add_contact is not None else 0
        flags |= (1 << 2) if self.block_contact is not None else 0
        flags |= (1 << 3) if self.share_contact is not None else 0
        flags |= (1 << 4) if self.need_contacts_exception is not None else 0
        flags |= (1 << 5) if self.report_geo is not None else 0
        flags |= (1 << 7) if self.autoarchived is not None else 0
        flags |= (1 << 6) if self.geo_distance is not None else 0
        data.write(Int(flags))

        if self.geo_distance is not None:
            data.write(Int(self.geo_distance))

        return data.getvalue()
