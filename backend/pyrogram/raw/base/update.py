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

Update = Union[
    raw.types.UpdateBotCallbackQuery, raw.types.UpdateBotInlineQuery, raw.types.UpdateBotInlineSend, raw.types.UpdateBotPrecheckoutQuery, raw.types.UpdateBotShippingQuery, raw.types.UpdateBotWebhookJSON, raw.types.UpdateBotWebhookJSONQuery, raw.types.UpdateChannel, raw.types.UpdateChannelAvailableMessages, raw.types.UpdateChannelMessageForwards, raw.types.UpdateChannelMessageViews, raw.types.UpdateChannelParticipant, raw.types.UpdateChannelReadMessagesContents, raw.types.UpdateChannelTooLong, raw.types.UpdateChannelUserTyping, raw.types.UpdateChannelWebPage, raw.types.UpdateChat, raw.types.UpdateChatDefaultBannedRights, raw.types.UpdateChatParticipantAdd, raw.types.UpdateChatParticipantAdmin, raw.types.UpdateChatParticipantDelete, raw.types.UpdateChatParticipants, raw.types.UpdateChatUserTyping, raw.types.UpdateConfig, raw.types.UpdateContactsReset, raw.types.UpdateDcOptions, raw.types.UpdateDeleteChannelMessages, raw.types.UpdateDeleteMessages, raw.types.UpdateDeleteScheduledMessages, raw.types.UpdateDialogFilter, raw.types.UpdateDialogFilterOrder, raw.types.UpdateDialogFilters, raw.types.UpdateDialogPinned, raw.types.UpdateDialogUnreadMark, raw.types.UpdateDraftMessage, raw.types.UpdateEditChannelMessage, raw.types.UpdateEditMessage, raw.types.UpdateEncryptedChatTyping, raw.types.UpdateEncryptedMessagesRead, raw.types.UpdateEncryption, raw.types.UpdateFavedStickers, raw.types.UpdateFolderPeers, raw.types.UpdateGeoLiveViewed, raw.types.UpdateGroupCall, raw.types.UpdateGroupCallParticipants, raw.types.UpdateInlineBotCallbackQuery, raw.types.UpdateLangPack, raw.types.UpdateLangPackTooLong, raw.types.UpdateLoginToken, raw.types.UpdateMessageID, raw.types.UpdateMessagePoll, raw.types.UpdateMessagePollVote, raw.types.UpdateNewChannelMessage, raw.types.UpdateNewEncryptedMessage, raw.types.UpdateNewMessage, raw.types.UpdateNewScheduledMessage, raw.types.UpdateNewStickerSet, raw.types.UpdateNotifySettings, raw.types.UpdatePeerBlocked, raw.types.UpdatePeerLocated, raw.types.UpdatePeerSettings, raw.types.UpdatePhoneCall, raw.types.UpdatePhoneCallSignalingData, raw.types.UpdatePinnedChannelMessages, raw.types.UpdatePinnedDialogs, raw.types.UpdatePinnedMessages, raw.types.UpdatePrivacy, raw.types.UpdatePtsChanged, raw.types.UpdateReadChannelDiscussionInbox, raw.types.UpdateReadChannelDiscussionOutbox, raw.types.UpdateReadChannelInbox, raw.types.UpdateReadChannelOutbox, raw.types.UpdateReadFeaturedStickers, raw.types.UpdateReadHistoryInbox, raw.types.UpdateReadHistoryOutbox, raw.types.UpdateReadMessagesContents, raw.types.UpdateRecentStickers, raw.types.UpdateSavedGifs, raw.types.UpdateServiceNotification, raw.types.UpdateStickerSets, raw.types.UpdateStickerSetsOrder, raw.types.UpdateTheme, raw.types.UpdateUserName, raw.types.UpdateUserPhone, raw.types.UpdateUserPhoto, raw.types.UpdateUserStatus, raw.types.UpdateUserTyping, raw.types.UpdateWebPage]


# noinspection PyRedeclaration
class Update:  # type: ignore
    """This base type has 88 constructors available.

    Constructors:
        .. hlist::
            :columns: 2

            - :obj:`UpdateBotCallbackQuery <pyrogram.raw.types.UpdateBotCallbackQuery>`
            - :obj:`UpdateBotInlineQuery <pyrogram.raw.types.UpdateBotInlineQuery>`
            - :obj:`UpdateBotInlineSend <pyrogram.raw.types.UpdateBotInlineSend>`
            - :obj:`UpdateBotPrecheckoutQuery <pyrogram.raw.types.UpdateBotPrecheckoutQuery>`
            - :obj:`UpdateBotShippingQuery <pyrogram.raw.types.UpdateBotShippingQuery>`
            - :obj:`UpdateBotWebhookJSON <pyrogram.raw.types.UpdateBotWebhookJSON>`
            - :obj:`UpdateBotWebhookJSONQuery <pyrogram.raw.types.UpdateBotWebhookJSONQuery>`
            - :obj:`UpdateChannel <pyrogram.raw.types.UpdateChannel>`
            - :obj:`UpdateChannelAvailableMessages <pyrogram.raw.types.UpdateChannelAvailableMessages>`
            - :obj:`UpdateChannelMessageForwards <pyrogram.raw.types.UpdateChannelMessageForwards>`
            - :obj:`UpdateChannelMessageViews <pyrogram.raw.types.UpdateChannelMessageViews>`
            - :obj:`UpdateChannelParticipant <pyrogram.raw.types.UpdateChannelParticipant>`
            - :obj:`UpdateChannelReadMessagesContents <pyrogram.raw.types.UpdateChannelReadMessagesContents>`
            - :obj:`UpdateChannelTooLong <pyrogram.raw.types.UpdateChannelTooLong>`
            - :obj:`UpdateChannelUserTyping <pyrogram.raw.types.UpdateChannelUserTyping>`
            - :obj:`UpdateChannelWebPage <pyrogram.raw.types.UpdateChannelWebPage>`
            - :obj:`UpdateChat <pyrogram.raw.types.UpdateChat>`
            - :obj:`UpdateChatDefaultBannedRights <pyrogram.raw.types.UpdateChatDefaultBannedRights>`
            - :obj:`UpdateChatParticipantAdd <pyrogram.raw.types.UpdateChatParticipantAdd>`
            - :obj:`UpdateChatParticipantAdmin <pyrogram.raw.types.UpdateChatParticipantAdmin>`
            - :obj:`UpdateChatParticipantDelete <pyrogram.raw.types.UpdateChatParticipantDelete>`
            - :obj:`UpdateChatParticipants <pyrogram.raw.types.UpdateChatParticipants>`
            - :obj:`UpdateChatUserTyping <pyrogram.raw.types.UpdateChatUserTyping>`
            - :obj:`UpdateConfig <pyrogram.raw.types.UpdateConfig>`
            - :obj:`UpdateContactsReset <pyrogram.raw.types.UpdateContactsReset>`
            - :obj:`UpdateDcOptions <pyrogram.raw.types.UpdateDcOptions>`
            - :obj:`UpdateDeleteChannelMessages <pyrogram.raw.types.UpdateDeleteChannelMessages>`
            - :obj:`UpdateDeleteMessages <pyrogram.raw.types.UpdateDeleteMessages>`
            - :obj:`UpdateDeleteScheduledMessages <pyrogram.raw.types.UpdateDeleteScheduledMessages>`
            - :obj:`UpdateDialogFilter <pyrogram.raw.types.UpdateDialogFilter>`
            - :obj:`UpdateDialogFilterOrder <pyrogram.raw.types.UpdateDialogFilterOrder>`
            - :obj:`UpdateDialogFilters <pyrogram.raw.types.UpdateDialogFilters>`
            - :obj:`UpdateDialogPinned <pyrogram.raw.types.UpdateDialogPinned>`
            - :obj:`UpdateDialogUnreadMark <pyrogram.raw.types.UpdateDialogUnreadMark>`
            - :obj:`UpdateDraftMessage <pyrogram.raw.types.UpdateDraftMessage>`
            - :obj:`UpdateEditChannelMessage <pyrogram.raw.types.UpdateEditChannelMessage>`
            - :obj:`UpdateEditMessage <pyrogram.raw.types.UpdateEditMessage>`
            - :obj:`UpdateEncryptedChatTyping <pyrogram.raw.types.UpdateEncryptedChatTyping>`
            - :obj:`UpdateEncryptedMessagesRead <pyrogram.raw.types.UpdateEncryptedMessagesRead>`
            - :obj:`UpdateEncryption <pyrogram.raw.types.UpdateEncryption>`
            - :obj:`UpdateFavedStickers <pyrogram.raw.types.UpdateFavedStickers>`
            - :obj:`UpdateFolderPeers <pyrogram.raw.types.UpdateFolderPeers>`
            - :obj:`UpdateGeoLiveViewed <pyrogram.raw.types.UpdateGeoLiveViewed>`
            - :obj:`UpdateGroupCall <pyrogram.raw.types.UpdateGroupCall>`
            - :obj:`UpdateGroupCallParticipants <pyrogram.raw.types.UpdateGroupCallParticipants>`
            - :obj:`UpdateInlineBotCallbackQuery <pyrogram.raw.types.UpdateInlineBotCallbackQuery>`
            - :obj:`UpdateLangPack <pyrogram.raw.types.UpdateLangPack>`
            - :obj:`UpdateLangPackTooLong <pyrogram.raw.types.UpdateLangPackTooLong>`
            - :obj:`UpdateLoginToken <pyrogram.raw.types.UpdateLoginToken>`
            - :obj:`UpdateMessageID <pyrogram.raw.types.UpdateMessageID>`
            - :obj:`UpdateMessagePoll <pyrogram.raw.types.UpdateMessagePoll>`
            - :obj:`UpdateMessagePollVote <pyrogram.raw.types.UpdateMessagePollVote>`
            - :obj:`UpdateNewChannelMessage <pyrogram.raw.types.UpdateNewChannelMessage>`
            - :obj:`UpdateNewEncryptedMessage <pyrogram.raw.types.UpdateNewEncryptedMessage>`
            - :obj:`UpdateNewMessage <pyrogram.raw.types.UpdateNewMessage>`
            - :obj:`UpdateNewScheduledMessage <pyrogram.raw.types.UpdateNewScheduledMessage>`
            - :obj:`UpdateNewStickerSet <pyrogram.raw.types.UpdateNewStickerSet>`
            - :obj:`UpdateNotifySettings <pyrogram.raw.types.UpdateNotifySettings>`
            - :obj:`UpdatePeerBlocked <pyrogram.raw.types.UpdatePeerBlocked>`
            - :obj:`UpdatePeerLocated <pyrogram.raw.types.UpdatePeerLocated>`
            - :obj:`UpdatePeerSettings <pyrogram.raw.types.UpdatePeerSettings>`
            - :obj:`UpdatePhoneCall <pyrogram.raw.types.UpdatePhoneCall>`
            - :obj:`UpdatePhoneCallSignalingData <pyrogram.raw.types.UpdatePhoneCallSignalingData>`
            - :obj:`UpdatePinnedChannelMessages <pyrogram.raw.types.UpdatePinnedChannelMessages>`
            - :obj:`UpdatePinnedDialogs <pyrogram.raw.types.UpdatePinnedDialogs>`
            - :obj:`UpdatePinnedMessages <pyrogram.raw.types.UpdatePinnedMessages>`
            - :obj:`UpdatePrivacy <pyrogram.raw.types.UpdatePrivacy>`
            - :obj:`UpdatePtsChanged <pyrogram.raw.types.UpdatePtsChanged>`
            - :obj:`UpdateReadChannelDiscussionInbox <pyrogram.raw.types.UpdateReadChannelDiscussionInbox>`
            - :obj:`UpdateReadChannelDiscussionOutbox <pyrogram.raw.types.UpdateReadChannelDiscussionOutbox>`
            - :obj:`UpdateReadChannelInbox <pyrogram.raw.types.UpdateReadChannelInbox>`
            - :obj:`UpdateReadChannelOutbox <pyrogram.raw.types.UpdateReadChannelOutbox>`
            - :obj:`UpdateReadFeaturedStickers <pyrogram.raw.types.UpdateReadFeaturedStickers>`
            - :obj:`UpdateReadHistoryInbox <pyrogram.raw.types.UpdateReadHistoryInbox>`
            - :obj:`UpdateReadHistoryOutbox <pyrogram.raw.types.UpdateReadHistoryOutbox>`
            - :obj:`UpdateReadMessagesContents <pyrogram.raw.types.UpdateReadMessagesContents>`
            - :obj:`UpdateRecentStickers <pyrogram.raw.types.UpdateRecentStickers>`
            - :obj:`UpdateSavedGifs <pyrogram.raw.types.UpdateSavedGifs>`
            - :obj:`UpdateServiceNotification <pyrogram.raw.types.UpdateServiceNotification>`
            - :obj:`UpdateStickerSets <pyrogram.raw.types.UpdateStickerSets>`
            - :obj:`UpdateStickerSetsOrder <pyrogram.raw.types.UpdateStickerSetsOrder>`
            - :obj:`UpdateTheme <pyrogram.raw.types.UpdateTheme>`
            - :obj:`UpdateUserName <pyrogram.raw.types.UpdateUserName>`
            - :obj:`UpdateUserPhone <pyrogram.raw.types.UpdateUserPhone>`
            - :obj:`UpdateUserPhoto <pyrogram.raw.types.UpdateUserPhoto>`
            - :obj:`UpdateUserStatus <pyrogram.raw.types.UpdateUserStatus>`
            - :obj:`UpdateUserTyping <pyrogram.raw.types.UpdateUserTyping>`
            - :obj:`UpdateWebPage <pyrogram.raw.types.UpdateWebPage>`
    """

    QUALNAME = "pyrogram.raw.base.Update"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes: "
                        "you tried to use a base type instance as argument, "
                        "but you need to instantiate one of its constructors instead. "
                        "More info: https://docs.pyrogram.org/telegram/base/update")
