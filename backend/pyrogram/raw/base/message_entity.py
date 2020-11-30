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

# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

MessageEntity = Union[
    raw.types.InputMessageEntityMentionName, raw.types.MessageEntityBankCard, raw.types.MessageEntityBlockquote, raw.types.MessageEntityBold, raw.types.MessageEntityBotCommand, raw.types.MessageEntityCashtag, raw.types.MessageEntityCode, raw.types.MessageEntityEmail, raw.types.MessageEntityHashtag, raw.types.MessageEntityItalic, raw.types.MessageEntityMention, raw.types.MessageEntityMentionName, raw.types.MessageEntityPhone, raw.types.MessageEntityPre, raw.types.MessageEntityStrike, raw.types.MessageEntityTextUrl, raw.types.MessageEntityUnderline, raw.types.MessageEntityUnknown, raw.types.MessageEntityUrl]


# noinspection PyRedeclaration
class MessageEntity:  # type: ignore
    """This base type has 19 constructors available.

    Constructors:
        .. hlist::
            :columns: 2

            - :obj:`InputMessageEntityMentionName <pyrogram.raw.types.InputMessageEntityMentionName>`
            - :obj:`MessageEntityBankCard <pyrogram.raw.types.MessageEntityBankCard>`
            - :obj:`MessageEntityBlockquote <pyrogram.raw.types.MessageEntityBlockquote>`
            - :obj:`MessageEntityBold <pyrogram.raw.types.MessageEntityBold>`
            - :obj:`MessageEntityBotCommand <pyrogram.raw.types.MessageEntityBotCommand>`
            - :obj:`MessageEntityCashtag <pyrogram.raw.types.MessageEntityCashtag>`
            - :obj:`MessageEntityCode <pyrogram.raw.types.MessageEntityCode>`
            - :obj:`MessageEntityEmail <pyrogram.raw.types.MessageEntityEmail>`
            - :obj:`MessageEntityHashtag <pyrogram.raw.types.MessageEntityHashtag>`
            - :obj:`MessageEntityItalic <pyrogram.raw.types.MessageEntityItalic>`
            - :obj:`MessageEntityMention <pyrogram.raw.types.MessageEntityMention>`
            - :obj:`MessageEntityMentionName <pyrogram.raw.types.MessageEntityMentionName>`
            - :obj:`MessageEntityPhone <pyrogram.raw.types.MessageEntityPhone>`
            - :obj:`MessageEntityPre <pyrogram.raw.types.MessageEntityPre>`
            - :obj:`MessageEntityStrike <pyrogram.raw.types.MessageEntityStrike>`
            - :obj:`MessageEntityTextUrl <pyrogram.raw.types.MessageEntityTextUrl>`
            - :obj:`MessageEntityUnderline <pyrogram.raw.types.MessageEntityUnderline>`
            - :obj:`MessageEntityUnknown <pyrogram.raw.types.MessageEntityUnknown>`
            - :obj:`MessageEntityUrl <pyrogram.raw.types.MessageEntityUrl>`
    """

    QUALNAME = "pyrogram.raw.base.MessageEntity"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes: "
                        "you tried to use a base type instance as argument, "
                        "but you need to instantiate one of its constructors instead. "
                        "More info: https://docs.pyrogram.org/telegram/base/message-entity")
