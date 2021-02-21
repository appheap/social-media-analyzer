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

WallPaper = Union[raw.types.WallPaper, raw.types.WallPaperNoFile]


# noinspection PyRedeclaration
class WallPaper:  # type: ignore
    """This base type has 2 constructors available.

    Constructors:
        .. hlist::
            :columns: 2

            - :obj:`WallPaper <pyrogram.raw.types.WallPaper>`
            - :obj:`WallPaperNoFile <pyrogram.raw.types.WallPaperNoFile>`

    See Also:
        This object can be returned by 3 methods:

        .. hlist::
            :columns: 2

            - :obj:`account.GetWallPaper <pyrogram.raw.functions.account.GetWallPaper>`
            - :obj:`account.UploadWallPaper <pyrogram.raw.functions.account.UploadWallPaper>`
            - :obj:`account.GetMultiWallPapers <pyrogram.raw.functions.account.GetMultiWallPapers>`
    """

    QUALNAME = "pyrogram.raw.base.WallPaper"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes: "
                        "you tried to use a base type instance as argument, "
                        "but you need to instantiate one of its constructors instead. "
                        "More info: https://docs.pyrogram.org/telegram/base/wall-paper")
