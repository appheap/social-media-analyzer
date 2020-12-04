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

MessagesFilter = Union[
    raw.types.InputMessagesFilterChatPhotos, raw.types.InputMessagesFilterContacts, raw.types.InputMessagesFilterDocument, raw.types.InputMessagesFilterEmpty, raw.types.InputMessagesFilterGeo, raw.types.InputMessagesFilterGif, raw.types.InputMessagesFilterMusic, raw.types.InputMessagesFilterMyMentions, raw.types.InputMessagesFilterPhoneCalls, raw.types.InputMessagesFilterPhotoVideo, raw.types.InputMessagesFilterPhotos, raw.types.InputMessagesFilterPinned, raw.types.InputMessagesFilterRoundVideo, raw.types.InputMessagesFilterRoundVoice, raw.types.InputMessagesFilterUrl, raw.types.InputMessagesFilterVideo, raw.types.InputMessagesFilterVoice]


# noinspection PyRedeclaration
class MessagesFilter:  # type: ignore
    """This base type has 17 constructors available.

    Constructors:
        .. hlist::
            :columns: 2

            - :obj:`InputMessagesFilterChatPhotos <pyrogram.raw.types.InputMessagesFilterChatPhotos>`
            - :obj:`InputMessagesFilterContacts <pyrogram.raw.types.InputMessagesFilterContacts>`
            - :obj:`InputMessagesFilterDocument <pyrogram.raw.types.InputMessagesFilterDocument>`
            - :obj:`InputMessagesFilterEmpty <pyrogram.raw.types.InputMessagesFilterEmpty>`
            - :obj:`InputMessagesFilterGeo <pyrogram.raw.types.InputMessagesFilterGeo>`
            - :obj:`InputMessagesFilterGif <pyrogram.raw.types.InputMessagesFilterGif>`
            - :obj:`InputMessagesFilterMusic <pyrogram.raw.types.InputMessagesFilterMusic>`
            - :obj:`InputMessagesFilterMyMentions <pyrogram.raw.types.InputMessagesFilterMyMentions>`
            - :obj:`InputMessagesFilterPhoneCalls <pyrogram.raw.types.InputMessagesFilterPhoneCalls>`
            - :obj:`InputMessagesFilterPhotoVideo <pyrogram.raw.types.InputMessagesFilterPhotoVideo>`
            - :obj:`InputMessagesFilterPhotos <pyrogram.raw.types.InputMessagesFilterPhotos>`
            - :obj:`InputMessagesFilterPinned <pyrogram.raw.types.InputMessagesFilterPinned>`
            - :obj:`InputMessagesFilterRoundVideo <pyrogram.raw.types.InputMessagesFilterRoundVideo>`
            - :obj:`InputMessagesFilterRoundVoice <pyrogram.raw.types.InputMessagesFilterRoundVoice>`
            - :obj:`InputMessagesFilterUrl <pyrogram.raw.types.InputMessagesFilterUrl>`
            - :obj:`InputMessagesFilterVideo <pyrogram.raw.types.InputMessagesFilterVideo>`
            - :obj:`InputMessagesFilterVoice <pyrogram.raw.types.InputMessagesFilterVoice>`
    """

    QUALNAME = "pyrogram.raw.base.MessagesFilter"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes: "
                        "you tried to use a base type instance as argument, "
                        "but you need to instantiate one of its constructors instead. "
                        "More info: https://docs.pyrogram.org/telegram/base/messages-filter")
