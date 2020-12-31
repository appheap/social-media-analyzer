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

SendMessageAction = Union[
    raw.types.SendMessageCancelAction, raw.types.SendMessageChooseContactAction, raw.types.SendMessageGamePlayAction, raw.types.SendMessageGeoLocationAction, raw.types.SendMessageRecordAudioAction, raw.types.SendMessageRecordRoundAction, raw.types.SendMessageRecordVideoAction, raw.types.SendMessageTypingAction, raw.types.SendMessageUploadAudioAction, raw.types.SendMessageUploadDocumentAction, raw.types.SendMessageUploadPhotoAction, raw.types.SendMessageUploadRoundAction, raw.types.SendMessageUploadVideoAction, raw.types.SpeakingInGroupCallAction]


# noinspection PyRedeclaration
class SendMessageAction:  # type: ignore
    """This base type has 14 constructors available.

    Constructors:
        .. hlist::
            :columns: 2

            - :obj:`SendMessageCancelAction <pyrogram.raw.types.SendMessageCancelAction>`
            - :obj:`SendMessageChooseContactAction <pyrogram.raw.types.SendMessageChooseContactAction>`
            - :obj:`SendMessageGamePlayAction <pyrogram.raw.types.SendMessageGamePlayAction>`
            - :obj:`SendMessageGeoLocationAction <pyrogram.raw.types.SendMessageGeoLocationAction>`
            - :obj:`SendMessageRecordAudioAction <pyrogram.raw.types.SendMessageRecordAudioAction>`
            - :obj:`SendMessageRecordRoundAction <pyrogram.raw.types.SendMessageRecordRoundAction>`
            - :obj:`SendMessageRecordVideoAction <pyrogram.raw.types.SendMessageRecordVideoAction>`
            - :obj:`SendMessageTypingAction <pyrogram.raw.types.SendMessageTypingAction>`
            - :obj:`SendMessageUploadAudioAction <pyrogram.raw.types.SendMessageUploadAudioAction>`
            - :obj:`SendMessageUploadDocumentAction <pyrogram.raw.types.SendMessageUploadDocumentAction>`
            - :obj:`SendMessageUploadPhotoAction <pyrogram.raw.types.SendMessageUploadPhotoAction>`
            - :obj:`SendMessageUploadRoundAction <pyrogram.raw.types.SendMessageUploadRoundAction>`
            - :obj:`SendMessageUploadVideoAction <pyrogram.raw.types.SendMessageUploadVideoAction>`
            - :obj:`SpeakingInGroupCallAction <pyrogram.raw.types.SpeakingInGroupCallAction>`
    """

    QUALNAME = "pyrogram.raw.base.SendMessageAction"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes: "
                        "you tried to use a base type instance as argument, "
                        "but you need to instantiate one of its constructors instead. "
                        "More info: https://docs.pyrogram.org/telegram/base/send-message-action")
