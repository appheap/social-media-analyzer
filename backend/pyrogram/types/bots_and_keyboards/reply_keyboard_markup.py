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

from typing import List, Union

from pyrogram import raw
from pyrogram import types
from ..object import Object


class ReplyKeyboardMarkup(Object):
    """A custom keyboard with reply options.

    Parameters:
        keyboard (List of List of :obj:`~pyrogram.types.KeyboardButton`):
            List of button rows, each represented by a List of KeyboardButton objects.

        resize_keyboard (``bool``, *optional*):
            Requests clients to resize the keyboard vertically for optimal fit (e.g., make the keyboard smaller if
            there are just two rows of buttons). Defaults to false, in which case the custom keyboard is always of
            the same height as the app's standard keyboard.

        one_time_keyboard (``bool``, *optional*):
            Requests clients to hide the keyboard as soon as it's been used. The keyboard will still be available,
            but clients will automatically display the usual letter-keyboard in the chat – the user can press a
            special button in the input field to see the custom keyboard again. Defaults to false.

        selective (``bool``, *optional*):
            Use this parameter if you want to show the keyboard to specific users only. Targets:
            1) users that are @mentioned in the text of the Message object;
            2) if the bot's message is a reply (has reply_to_message_id), sender of the original message.
            Example: A user requests to change the bot's language, bot replies to the request with a keyboard to
            select the new language. Other users in the group don't see the keyboard.
    """

    def __init__(
            self,
            keyboard: List[List[Union["types.KeyboardButton", str]]],
            resize_keyboard: bool = None,
            one_time_keyboard: bool = None,
            selective: bool = None
    ):
        super().__init__()

        self.keyboard = keyboard
        self.resize_keyboard = resize_keyboard
        self.one_time_keyboard = one_time_keyboard
        self.selective = selective

    @staticmethod
    def read(kb):
        keyboard = []

        for i in kb.rows:
            row = []

            for j in i.buttons:
                row.append(types.KeyboardButton.read(j))

            keyboard.append(row)

        return ReplyKeyboardMarkup(
            keyboard=keyboard,
            resize_keyboard=kb.resize,
            one_time_keyboard=kb.single_use,
            selective=kb.selective
        )

    def write(self):
        return raw.types.ReplyKeyboardMarkup(
            rows=[raw.types.KeyboardButtonRow(
                buttons=[
                    types.KeyboardButton(j).write()
                    if isinstance(j, str) else j.write()
                    for j in i
                ]
            ) for i in self.keyboard],
            resize=self.resize_keyboard or None,
            single_use=self.one_time_keyboard or None,
            selective=self.selective or None
        )
