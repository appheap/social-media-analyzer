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

FileType = Union[
    raw.types.storage.FileGif, raw.types.storage.FileJpeg, raw.types.storage.FileMov, raw.types.storage.FileMp3, raw.types.storage.FileMp4, raw.types.storage.FilePartial, raw.types.storage.FilePdf, raw.types.storage.FilePng, raw.types.storage.FileUnknown, raw.types.storage.FileWebp]


# noinspection PyRedeclaration
class FileType:  # type: ignore
    """This base type has 10 constructors available.

    Constructors:
        .. hlist::
            :columns: 2

            - :obj:`storage.FileGif <pyrogram.raw.types.storage.FileGif>`
            - :obj:`storage.FileJpeg <pyrogram.raw.types.storage.FileJpeg>`
            - :obj:`storage.FileMov <pyrogram.raw.types.storage.FileMov>`
            - :obj:`storage.FileMp3 <pyrogram.raw.types.storage.FileMp3>`
            - :obj:`storage.FileMp4 <pyrogram.raw.types.storage.FileMp4>`
            - :obj:`storage.FilePartial <pyrogram.raw.types.storage.FilePartial>`
            - :obj:`storage.FilePdf <pyrogram.raw.types.storage.FilePdf>`
            - :obj:`storage.FilePng <pyrogram.raw.types.storage.FilePng>`
            - :obj:`storage.FileUnknown <pyrogram.raw.types.storage.FileUnknown>`
            - :obj:`storage.FileWebp <pyrogram.raw.types.storage.FileWebp>`
    """

    QUALNAME = "pyrogram.raw.base.storage.FileType"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes: "
                        "you tried to use a base type instance as argument, "
                        "but you need to instantiate one of its constructors instead. "
                        "More info: https://docs.pyrogram.org/telegram/base/file-type")
