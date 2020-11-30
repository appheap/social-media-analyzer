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

ChannelAdminLogEventAction = Union[
    raw.types.ChannelAdminLogEventActionChangeAbout, raw.types.ChannelAdminLogEventActionChangeLinkedChat, raw.types.ChannelAdminLogEventActionChangeLocation, raw.types.ChannelAdminLogEventActionChangePhoto, raw.types.ChannelAdminLogEventActionChangeStickerSet, raw.types.ChannelAdminLogEventActionChangeTitle, raw.types.ChannelAdminLogEventActionChangeUsername, raw.types.ChannelAdminLogEventActionDefaultBannedRights, raw.types.ChannelAdminLogEventActionDeleteMessage, raw.types.ChannelAdminLogEventActionEditMessage, raw.types.ChannelAdminLogEventActionParticipantInvite, raw.types.ChannelAdminLogEventActionParticipantJoin, raw.types.ChannelAdminLogEventActionParticipantLeave, raw.types.ChannelAdminLogEventActionParticipantToggleAdmin, raw.types.ChannelAdminLogEventActionParticipantToggleBan, raw.types.ChannelAdminLogEventActionStopPoll, raw.types.ChannelAdminLogEventActionToggleInvites, raw.types.ChannelAdminLogEventActionTogglePreHistoryHidden, raw.types.ChannelAdminLogEventActionToggleSignatures, raw.types.ChannelAdminLogEventActionToggleSlowMode, raw.types.ChannelAdminLogEventActionUpdatePinned]


# noinspection PyRedeclaration
class ChannelAdminLogEventAction:  # type: ignore
    """This base type has 21 constructors available.

    Constructors:
        .. hlist::
            :columns: 2

            - :obj:`ChannelAdminLogEventActionChangeAbout <pyrogram.raw.types.ChannelAdminLogEventActionChangeAbout>`
            - :obj:`ChannelAdminLogEventActionChangeLinkedChat <pyrogram.raw.types.ChannelAdminLogEventActionChangeLinkedChat>`
            - :obj:`ChannelAdminLogEventActionChangeLocation <pyrogram.raw.types.ChannelAdminLogEventActionChangeLocation>`
            - :obj:`ChannelAdminLogEventActionChangePhoto <pyrogram.raw.types.ChannelAdminLogEventActionChangePhoto>`
            - :obj:`ChannelAdminLogEventActionChangeStickerSet <pyrogram.raw.types.ChannelAdminLogEventActionChangeStickerSet>`
            - :obj:`ChannelAdminLogEventActionChangeTitle <pyrogram.raw.types.ChannelAdminLogEventActionChangeTitle>`
            - :obj:`ChannelAdminLogEventActionChangeUsername <pyrogram.raw.types.ChannelAdminLogEventActionChangeUsername>`
            - :obj:`ChannelAdminLogEventActionDefaultBannedRights <pyrogram.raw.types.ChannelAdminLogEventActionDefaultBannedRights>`
            - :obj:`ChannelAdminLogEventActionDeleteMessage <pyrogram.raw.types.ChannelAdminLogEventActionDeleteMessage>`
            - :obj:`ChannelAdminLogEventActionEditMessage <pyrogram.raw.types.ChannelAdminLogEventActionEditMessage>`
            - :obj:`ChannelAdminLogEventActionParticipantInvite <pyrogram.raw.types.ChannelAdminLogEventActionParticipantInvite>`
            - :obj:`ChannelAdminLogEventActionParticipantJoin <pyrogram.raw.types.ChannelAdminLogEventActionParticipantJoin>`
            - :obj:`ChannelAdminLogEventActionParticipantLeave <pyrogram.raw.types.ChannelAdminLogEventActionParticipantLeave>`
            - :obj:`ChannelAdminLogEventActionParticipantToggleAdmin <pyrogram.raw.types.ChannelAdminLogEventActionParticipantToggleAdmin>`
            - :obj:`ChannelAdminLogEventActionParticipantToggleBan <pyrogram.raw.types.ChannelAdminLogEventActionParticipantToggleBan>`
            - :obj:`ChannelAdminLogEventActionStopPoll <pyrogram.raw.types.ChannelAdminLogEventActionStopPoll>`
            - :obj:`ChannelAdminLogEventActionToggleInvites <pyrogram.raw.types.ChannelAdminLogEventActionToggleInvites>`
            - :obj:`ChannelAdminLogEventActionTogglePreHistoryHidden <pyrogram.raw.types.ChannelAdminLogEventActionTogglePreHistoryHidden>`
            - :obj:`ChannelAdminLogEventActionToggleSignatures <pyrogram.raw.types.ChannelAdminLogEventActionToggleSignatures>`
            - :obj:`ChannelAdminLogEventActionToggleSlowMode <pyrogram.raw.types.ChannelAdminLogEventActionToggleSlowMode>`
            - :obj:`ChannelAdminLogEventActionUpdatePinned <pyrogram.raw.types.ChannelAdminLogEventActionUpdatePinned>`
    """

    QUALNAME = "pyrogram.raw.base.ChannelAdminLogEventAction"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes: "
                        "you tried to use a base type instance as argument, "
                        "but you need to instantiate one of its constructors instead. "
                        "More info: https://docs.pyrogram.org/telegram/base/channel-admin-log-event-action")
