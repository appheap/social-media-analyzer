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


class ChatBannedRights(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~pyrogram.raw.base.ChatBannedRights`.

    Details:
        - Layer: ``122``
        - ID: ``0x9f120418``

    Parameters:
        until_date: ``int`` ``32-bit``
        view_messages (optional): ``bool``
        send_messages (optional): ``bool``
        send_media (optional): ``bool``
        send_stickers (optional): ``bool``
        send_gifs (optional): ``bool``
        send_games (optional): ``bool``
        send_inline (optional): ``bool``
        embed_links (optional): ``bool``
        send_polls (optional): ``bool``
        change_info (optional): ``bool``
        invite_users (optional): ``bool``
        pin_messages (optional): ``bool``
    """

    __slots__: List[str] = ["until_date", "view_messages", "send_messages", "send_media", "send_stickers", "send_gifs",
                            "send_games", "send_inline", "embed_links", "send_polls", "change_info", "invite_users",
                            "pin_messages"]

    ID = 0x9f120418
    QUALNAME = "types.ChatBannedRights"

    def __init__(self, *, until_date: int, view_messages: Union[None, bool] = None,
                 send_messages: Union[None, bool] = None, send_media: Union[None, bool] = None,
                 send_stickers: Union[None, bool] = None, send_gifs: Union[None, bool] = None,
                 send_games: Union[None, bool] = None, send_inline: Union[None, bool] = None,
                 embed_links: Union[None, bool] = None, send_polls: Union[None, bool] = None,
                 change_info: Union[None, bool] = None, invite_users: Union[None, bool] = None,
                 pin_messages: Union[None, bool] = None) -> None:
        self.until_date = until_date  # int
        self.view_messages = view_messages  # flags.0?true
        self.send_messages = send_messages  # flags.1?true
        self.send_media = send_media  # flags.2?true
        self.send_stickers = send_stickers  # flags.3?true
        self.send_gifs = send_gifs  # flags.4?true
        self.send_games = send_games  # flags.5?true
        self.send_inline = send_inline  # flags.6?true
        self.embed_links = embed_links  # flags.7?true
        self.send_polls = send_polls  # flags.8?true
        self.change_info = change_info  # flags.10?true
        self.invite_users = invite_users  # flags.15?true
        self.pin_messages = pin_messages  # flags.17?true

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "ChatBannedRights":
        flags = Int.read(data)

        view_messages = True if flags & (1 << 0) else False
        send_messages = True if flags & (1 << 1) else False
        send_media = True if flags & (1 << 2) else False
        send_stickers = True if flags & (1 << 3) else False
        send_gifs = True if flags & (1 << 4) else False
        send_games = True if flags & (1 << 5) else False
        send_inline = True if flags & (1 << 6) else False
        embed_links = True if flags & (1 << 7) else False
        send_polls = True if flags & (1 << 8) else False
        change_info = True if flags & (1 << 10) else False
        invite_users = True if flags & (1 << 15) else False
        pin_messages = True if flags & (1 << 17) else False
        until_date = Int.read(data)

        return ChatBannedRights(until_date=until_date, view_messages=view_messages, send_messages=send_messages,
                                send_media=send_media, send_stickers=send_stickers, send_gifs=send_gifs,
                                send_games=send_games, send_inline=send_inline, embed_links=embed_links,
                                send_polls=send_polls, change_info=change_info, invite_users=invite_users,
                                pin_messages=pin_messages)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.view_messages else 0
        flags |= (1 << 1) if self.send_messages else 0
        flags |= (1 << 2) if self.send_media else 0
        flags |= (1 << 3) if self.send_stickers else 0
        flags |= (1 << 4) if self.send_gifs else 0
        flags |= (1 << 5) if self.send_games else 0
        flags |= (1 << 6) if self.send_inline else 0
        flags |= (1 << 7) if self.embed_links else 0
        flags |= (1 << 8) if self.send_polls else 0
        flags |= (1 << 10) if self.change_info else 0
        flags |= (1 << 15) if self.invite_users else 0
        flags |= (1 << 17) if self.pin_messages else 0
        data.write(Int(flags))

        data.write(Int(self.until_date))

        return data.getvalue()
