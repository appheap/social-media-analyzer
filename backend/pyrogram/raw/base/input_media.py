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

InputMedia = Union[
    raw.types.InputMediaContact, raw.types.InputMediaDice, raw.types.InputMediaDocument, raw.types.InputMediaDocumentExternal, raw.types.InputMediaEmpty, raw.types.InputMediaGame, raw.types.InputMediaGeoLive, raw.types.InputMediaGeoPoint, raw.types.InputMediaInvoice, raw.types.InputMediaPhoto, raw.types.InputMediaPhotoExternal, raw.types.InputMediaPoll, raw.types.InputMediaUploadedDocument, raw.types.InputMediaUploadedPhoto, raw.types.InputMediaVenue]


# noinspection PyRedeclaration
class InputMedia:  # type: ignore
    """This base type has 15 constructors available.

    Constructors:
        .. hlist::
            :columns: 2

            - :obj:`InputMediaContact <pyrogram.raw.types.InputMediaContact>`
            - :obj:`InputMediaDice <pyrogram.raw.types.InputMediaDice>`
            - :obj:`InputMediaDocument <pyrogram.raw.types.InputMediaDocument>`
            - :obj:`InputMediaDocumentExternal <pyrogram.raw.types.InputMediaDocumentExternal>`
            - :obj:`InputMediaEmpty <pyrogram.raw.types.InputMediaEmpty>`
            - :obj:`InputMediaGame <pyrogram.raw.types.InputMediaGame>`
            - :obj:`InputMediaGeoLive <pyrogram.raw.types.InputMediaGeoLive>`
            - :obj:`InputMediaGeoPoint <pyrogram.raw.types.InputMediaGeoPoint>`
            - :obj:`InputMediaInvoice <pyrogram.raw.types.InputMediaInvoice>`
            - :obj:`InputMediaPhoto <pyrogram.raw.types.InputMediaPhoto>`
            - :obj:`InputMediaPhotoExternal <pyrogram.raw.types.InputMediaPhotoExternal>`
            - :obj:`InputMediaPoll <pyrogram.raw.types.InputMediaPoll>`
            - :obj:`InputMediaUploadedDocument <pyrogram.raw.types.InputMediaUploadedDocument>`
            - :obj:`InputMediaUploadedPhoto <pyrogram.raw.types.InputMediaUploadedPhoto>`
            - :obj:`InputMediaVenue <pyrogram.raw.types.InputMediaVenue>`
    """

    QUALNAME = "pyrogram.raw.base.InputMedia"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes: "
                        "you tried to use a base type instance as argument, "
                        "but you need to instantiate one of its constructors instead. "
                        "More info: https://docs.pyrogram.org/telegram/base/input-media")
