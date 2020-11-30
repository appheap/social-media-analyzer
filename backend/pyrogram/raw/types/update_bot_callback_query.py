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


class UpdateBotCallbackQuery(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~pyrogram.raw.base.Update`.

    Details:
        - Layer: ``117``
        - ID: ``0xe73547e1``

    Parameters:
        query_id: ``int`` ``64-bit``
        user_id: ``int`` ``32-bit``
        peer: :obj:`Peer <pyrogram.raw.base.Peer>`
        msg_id: ``int`` ``32-bit``
        chat_instance: ``int`` ``64-bit``
        data (optional): ``bytes``
        game_short_name (optional): ``str``
    """

    __slots__: List[str] = ["query_id", "user_id", "peer", "msg_id", "chat_instance", "data", "game_short_name"]

    ID = 0xe73547e1
    QUALNAME = "types.UpdateBotCallbackQuery"

    def __init__(self, *, query_id: int, user_id: int, peer: "raw.base.Peer", msg_id: int, chat_instance: int,
                 data: Union[None, bytes] = None, game_short_name: Union[None, str] = None) -> None:
        self.query_id = query_id  # long
        self.user_id = user_id  # int
        self.peer = peer  # Peer
        self.msg_id = msg_id  # int
        self.chat_instance = chat_instance  # long
        self.data = data  # flags.0?bytes
        self.game_short_name = game_short_name  # flags.1?string

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "UpdateBotCallbackQuery":
        flags = Int.read(data)

        query_id = Long.read(data)

        user_id = Int.read(data)

        peer = TLObject.read(data)

        msg_id = Int.read(data)

        chat_instance = Long.read(data)

        data = Bytes.read(data) if flags & (1 << 0) else None
        game_short_name = String.read(data) if flags & (1 << 1) else None
        return UpdateBotCallbackQuery(query_id=query_id, user_id=user_id, peer=peer, msg_id=msg_id,
                                      chat_instance=chat_instance, data=data, game_short_name=game_short_name)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.data is not None else 0
        flags |= (1 << 1) if self.game_short_name is not None else 0
        data.write(Int(flags))

        data.write(Long(self.query_id))

        data.write(Int(self.user_id))

        data.write(self.peer.write())

        data.write(Int(self.msg_id))

        data.write(Long(self.chat_instance))

        if self.data is not None:
            data.write(Bytes(self.data))

        if self.game_short_name is not None:
            data.write(String(self.game_short_name))

        return data.getvalue()
