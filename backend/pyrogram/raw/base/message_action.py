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

MessageAction = Union[
    raw.types.MessageActionBotAllowed, raw.types.MessageActionChannelCreate, raw.types.MessageActionChannelMigrateFrom, raw.types.MessageActionChatAddUser, raw.types.MessageActionChatCreate, raw.types.MessageActionChatDeletePhoto, raw.types.MessageActionChatDeleteUser, raw.types.MessageActionChatEditPhoto, raw.types.MessageActionChatEditTitle, raw.types.MessageActionChatJoinedByLink, raw.types.MessageActionChatMigrateTo, raw.types.MessageActionContactSignUp, raw.types.MessageActionCustomAction, raw.types.MessageActionEmpty, raw.types.MessageActionGameScore, raw.types.MessageActionHistoryClear, raw.types.MessageActionPaymentSent, raw.types.MessageActionPaymentSentMe, raw.types.MessageActionPhoneCall, raw.types.MessageActionPinMessage, raw.types.MessageActionScreenshotTaken, raw.types.MessageActionSecureValuesSent, raw.types.MessageActionSecureValuesSentMe]


# noinspection PyRedeclaration
class MessageAction:  # type: ignore
    """This base type has 23 constructors available.

    Constructors:
        .. hlist::
            :columns: 2

            - :obj:`MessageActionBotAllowed <pyrogram.raw.types.MessageActionBotAllowed>`
            - :obj:`MessageActionChannelCreate <pyrogram.raw.types.MessageActionChannelCreate>`
            - :obj:`MessageActionChannelMigrateFrom <pyrogram.raw.types.MessageActionChannelMigrateFrom>`
            - :obj:`MessageActionChatAddUser <pyrogram.raw.types.MessageActionChatAddUser>`
            - :obj:`MessageActionChatCreate <pyrogram.raw.types.MessageActionChatCreate>`
            - :obj:`MessageActionChatDeletePhoto <pyrogram.raw.types.MessageActionChatDeletePhoto>`
            - :obj:`MessageActionChatDeleteUser <pyrogram.raw.types.MessageActionChatDeleteUser>`
            - :obj:`MessageActionChatEditPhoto <pyrogram.raw.types.MessageActionChatEditPhoto>`
            - :obj:`MessageActionChatEditTitle <pyrogram.raw.types.MessageActionChatEditTitle>`
            - :obj:`MessageActionChatJoinedByLink <pyrogram.raw.types.MessageActionChatJoinedByLink>`
            - :obj:`MessageActionChatMigrateTo <pyrogram.raw.types.MessageActionChatMigrateTo>`
            - :obj:`MessageActionContactSignUp <pyrogram.raw.types.MessageActionContactSignUp>`
            - :obj:`MessageActionCustomAction <pyrogram.raw.types.MessageActionCustomAction>`
            - :obj:`MessageActionEmpty <pyrogram.raw.types.MessageActionEmpty>`
            - :obj:`MessageActionGameScore <pyrogram.raw.types.MessageActionGameScore>`
            - :obj:`MessageActionHistoryClear <pyrogram.raw.types.MessageActionHistoryClear>`
            - :obj:`MessageActionPaymentSent <pyrogram.raw.types.MessageActionPaymentSent>`
            - :obj:`MessageActionPaymentSentMe <pyrogram.raw.types.MessageActionPaymentSentMe>`
            - :obj:`MessageActionPhoneCall <pyrogram.raw.types.MessageActionPhoneCall>`
            - :obj:`MessageActionPinMessage <pyrogram.raw.types.MessageActionPinMessage>`
            - :obj:`MessageActionScreenshotTaken <pyrogram.raw.types.MessageActionScreenshotTaken>`
            - :obj:`MessageActionSecureValuesSent <pyrogram.raw.types.MessageActionSecureValuesSent>`
            - :obj:`MessageActionSecureValuesSentMe <pyrogram.raw.types.MessageActionSecureValuesSentMe>`
    """

    QUALNAME = "pyrogram.raw.base.MessageAction"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes: "
                        "you tried to use a base type instance as argument, "
                        "but you need to instantiate one of its constructors instead. "
                        "More info: https://docs.pyrogram.org/telegram/base/message-action")
