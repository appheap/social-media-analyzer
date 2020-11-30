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

KeyboardButton = Union[
    raw.types.InputKeyboardButtonUrlAuth, raw.types.KeyboardButton, raw.types.KeyboardButtonBuy, raw.types.KeyboardButtonCallback, raw.types.KeyboardButtonGame, raw.types.KeyboardButtonRequestGeoLocation, raw.types.KeyboardButtonRequestPhone, raw.types.KeyboardButtonRequestPoll, raw.types.KeyboardButtonSwitchInline, raw.types.KeyboardButtonUrl, raw.types.KeyboardButtonUrlAuth]


# noinspection PyRedeclaration
class KeyboardButton:  # type: ignore
    """This base type has 11 constructors available.

    Constructors:
        .. hlist::
            :columns: 2

            - :obj:`InputKeyboardButtonUrlAuth <pyrogram.raw.types.InputKeyboardButtonUrlAuth>`
            - :obj:`KeyboardButton <pyrogram.raw.types.KeyboardButton>`
            - :obj:`KeyboardButtonBuy <pyrogram.raw.types.KeyboardButtonBuy>`
            - :obj:`KeyboardButtonCallback <pyrogram.raw.types.KeyboardButtonCallback>`
            - :obj:`KeyboardButtonGame <pyrogram.raw.types.KeyboardButtonGame>`
            - :obj:`KeyboardButtonRequestGeoLocation <pyrogram.raw.types.KeyboardButtonRequestGeoLocation>`
            - :obj:`KeyboardButtonRequestPhone <pyrogram.raw.types.KeyboardButtonRequestPhone>`
            - :obj:`KeyboardButtonRequestPoll <pyrogram.raw.types.KeyboardButtonRequestPoll>`
            - :obj:`KeyboardButtonSwitchInline <pyrogram.raw.types.KeyboardButtonSwitchInline>`
            - :obj:`KeyboardButtonUrl <pyrogram.raw.types.KeyboardButtonUrl>`
            - :obj:`KeyboardButtonUrlAuth <pyrogram.raw.types.KeyboardButtonUrlAuth>`
    """

    QUALNAME = "pyrogram.raw.base.KeyboardButton"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes: "
                        "you tried to use a base type instance as argument, "
                        "but you need to instantiate one of its constructors instead. "
                        "More info: https://docs.pyrogram.org/telegram/base/keyboard-button")
