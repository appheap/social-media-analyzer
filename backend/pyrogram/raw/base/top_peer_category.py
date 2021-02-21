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

# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

TopPeerCategory = Union[
    raw.types.TopPeerCategoryBotsInline, raw.types.TopPeerCategoryBotsPM, raw.types.TopPeerCategoryChannels, raw.types.TopPeerCategoryCorrespondents, raw.types.TopPeerCategoryForwardChats, raw.types.TopPeerCategoryForwardUsers, raw.types.TopPeerCategoryGroups, raw.types.TopPeerCategoryPhoneCalls]


# noinspection PyRedeclaration
class TopPeerCategory:  # type: ignore
    """This base type has 8 constructors available.

    Constructors:
        .. hlist::
            :columns: 2

            - :obj:`TopPeerCategoryBotsInline <pyrogram.raw.types.TopPeerCategoryBotsInline>`
            - :obj:`TopPeerCategoryBotsPM <pyrogram.raw.types.TopPeerCategoryBotsPM>`
            - :obj:`TopPeerCategoryChannels <pyrogram.raw.types.TopPeerCategoryChannels>`
            - :obj:`TopPeerCategoryCorrespondents <pyrogram.raw.types.TopPeerCategoryCorrespondents>`
            - :obj:`TopPeerCategoryForwardChats <pyrogram.raw.types.TopPeerCategoryForwardChats>`
            - :obj:`TopPeerCategoryForwardUsers <pyrogram.raw.types.TopPeerCategoryForwardUsers>`
            - :obj:`TopPeerCategoryGroups <pyrogram.raw.types.TopPeerCategoryGroups>`
            - :obj:`TopPeerCategoryPhoneCalls <pyrogram.raw.types.TopPeerCategoryPhoneCalls>`
    """

    QUALNAME = "pyrogram.raw.base.TopPeerCategory"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes: "
                        "you tried to use a base type instance as argument, "
                        "but you need to instantiate one of its constructors instead. "
                        "More info: https://docs.pyrogram.org/telegram/base/top-peer-category")
