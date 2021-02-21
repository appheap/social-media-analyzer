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


class PeerNotifySettings(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~pyrogram.raw.base.PeerNotifySettings`.

    Details:
        - Layer: ``123``
        - ID: ``0xaf509d20``

    Parameters:
        show_previews (optional): ``bool``
        silent (optional): ``bool``
        mute_until (optional): ``int`` ``32-bit``
        sound (optional): ``str``

    See Also:
        This object can be returned by 1 method:

        .. hlist::
            :columns: 2

            - :obj:`account.GetNotifySettings <pyrogram.raw.functions.account.GetNotifySettings>`
    """

    __slots__: List[str] = ["show_previews", "silent", "mute_until", "sound"]

    ID = 0xaf509d20
    QUALNAME = "types.PeerNotifySettings"

    def __init__(self, *, show_previews: Union[None, bool] = None, silent: Union[None, bool] = None,
                 mute_until: Union[None, int] = None, sound: Union[None, str] = None) -> None:
        self.show_previews = show_previews  # flags.0?Bool
        self.silent = silent  # flags.1?Bool
        self.mute_until = mute_until  # flags.2?int
        self.sound = sound  # flags.3?string

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "PeerNotifySettings":
        flags = Int.read(data)

        show_previews = Bool.read(data) if flags & (1 << 0) else None
        silent = Bool.read(data) if flags & (1 << 1) else None
        mute_until = Int.read(data) if flags & (1 << 2) else None
        sound = String.read(data) if flags & (1 << 3) else None
        return PeerNotifySettings(show_previews=show_previews, silent=silent, mute_until=mute_until, sound=sound)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.show_previews is not None else 0
        flags |= (1 << 1) if self.silent is not None else 0
        flags |= (1 << 2) if self.mute_until is not None else 0
        flags |= (1 << 3) if self.sound is not None else 0
        data.write(Int(flags))

        if self.show_previews is not None:
            data.write(Bool(self.show_previews))

        if self.silent is not None:
            data.write(Bool(self.silent))

        if self.mute_until is not None:
            data.write(Int(self.mute_until))

        if self.sound is not None:
            data.write(String(self.sound))

        return data.getvalue()
