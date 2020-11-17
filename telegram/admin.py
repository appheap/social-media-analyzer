from django.contrib import admin

from . import models


# Register your models here.
class TelegramChannelInline(admin.TabularInline):
    model = models.TelegramChannel


class ChatsInline(admin.TabularInline):
    model = models.Chat


class AdminLogEventInline(admin.TabularInline):
    model = models.AdminLogEvent


class MessageViewInline(admin.TabularInline):
    model = models.MessageView


class MemberCountHistoryInline(admin.TabularInline):
    model = models.ChatMemberCount


class SharedMediaHistoryInline(admin.TabularInline):
    model = models.ChatSharedMedia


class TelegramAccountAdmin(admin.ModelAdmin):
    inlines = [
        TelegramChannelInline,
        ChatsInline,
        MemberCountHistoryInline,
        SharedMediaHistoryInline,
        MessageViewInline,
        AdminLogEventInline,
    ]
    list_display = ['first_name', 'username', 'created_at', 'modified_at']


#################################################################################

class TelegramAccountInline(admin.TabularInline):
    model = models.TelegramAccount


class ForwardedMessageInline(admin.TabularInline):
    model = models.Message
    fk_name = 'forward_from'
    verbose_name_plural = 'Forwarded Messages'


class SentMessageInline(admin.TabularInline):
    model = models.Message
    fk_name = 'from_user'
    verbose_name_plural = 'Sent Messages'


class ViaBotMessageInline(admin.TabularInline):
    model = models.Message
    fk_name = 'via_bot'
    verbose_name_plural = 'Inline Messages'


class InvitedParticipantInline(admin.TabularInline):
    model = models.ChannelParticipant
    fk_name = 'invited_by'
    verbose_name_plural = 'Invited Participants'


class PromotedParticipantInline(admin.TabularInline):
    model = models.ChannelParticipant
    fk_name = 'promoted_by'
    verbose_name_plural = 'Promoted Participants'


class DemotedParticipantInline(admin.TabularInline):
    model = models.ChannelParticipant
    fk_name = 'demoted_by'
    verbose_name_plural = 'Demoted Participants'


class KickedParticipantInline(admin.TabularInline):
    model = models.ChannelParticipant
    fk_name = 'kicked_by'
    verbose_name_plural = 'Kicked Participants'


class MentionedInline(admin.TabularInline):
    model = models.Entity
    fk_name = 'user'
    verbose_name_plural = 'Mentions'


class MembershipInline(admin.TabularInline):
    model = models.Membership


class UserAdmin(admin.ModelAdmin):
    inlines = [
        TelegramAccountInline,
        MembershipInline,
        # ForwardedMessageInline,
        # SentMessageInline,
        # ViaBotMessageInline,
        InvitedParticipantInline,
        PromotedParticipantInline,
        DemotedParticipantInline,
        KickedParticipantInline,
        # MentionedInline,
    ]


#################################################################################

class ChatMemberInline(admin.TabularInline):
    model = models.User.chats.through
    verbose_name_plural = 'Members'


class LinkedChatInline(admin.TabularInline):
    model = models.Chat
    verbose_name_plural = 'Linked Chats'


class MessageInline(admin.TabularInline):
    model = models.Message
    fk_name = 'chat'
    verbose_name_plural = 'Messages'


class ForwardedMessageChannelInline(admin.TabularInline):
    model = models.Message
    fk_name = 'forward_from_chat'
    verbose_name_plural = 'Forwarded Messages'


class ChatAdmin(admin.ModelAdmin):
    inlines = [
        TelegramChannelInline,
        ChatMemberInline,
        AdminLogEventInline,

        # MessageInline,
        # ForwardedMessageChannelInline,
        # LinkedChatInline,
        # MemberCountHistoryInline,
        # SharedMediaHistoryInline,
        # MessageViewInline,
    ]


#################################################################################


#################################################################################
#################################################################################
#################################################################################
#################################################################################

class SharedMediaAnalyzerMetaDataAdmin(admin.ModelAdmin):
    list_display = ('enabled',)


#################################################################################
#################################################################################

class EntityInline(admin.TabularInline):
    model = models.Entity


class EntityTypeInline(admin.TabularInline):
    model = models.EntityType


class MessageReplyInline(admin.TabularInline):
    model = models.Message
    verbose_name_plural = 'Replies'


class ActionMessagePinnedInline(admin.TabularInline):
    model = models.AdminLogEventActionUpdatePinned
    verbose_name_plural = 'Pinned Actions'


class ActionMessageEditedPrevInline(admin.TabularInline):
    model = models.AdminLogEventActionEditMessage
    verbose_name_plural = 'Action Edit Prevs'
    fk_name = 'prev_message'


class ActionMessageEditedNewInline(admin.TabularInline):
    model = models.AdminLogEventActionEditMessage
    verbose_name_plural = 'Action Edit News'
    fk_name = 'new_message'


class ActionMessageStopPollInline(admin.TabularInline):
    model = models.AdminLogEventActionStopPoll
    verbose_name_plural = 'Action Stop Polls'


class MessageAdmin(admin.ModelAdmin):
    inlines = [
        MessageReplyInline,
        EntityInline,
        EntityTypeInline,
        MessageViewInline,
        ActionMessagePinnedInline,
        ActionMessageEditedPrevInline,
        ActionMessageEditedNewInline,
        ActionMessageStopPollInline,
    ]


#################################################################################
class ChannelParticipantInline(admin.TabularInline):
    model = models.ChannelParticipant
    fk_name = 'membership'
    verbose_name_plural = 'participant history'
    fields = (
        'user', 'type', 'join_date', 'promoted_by',
        'invited_by', 'demoted_by', 'kicked_by',
        'admin_rights', 'banned_rights', 'can_edit',
    )


class MembershipAdmin(admin.ModelAdmin):
    inlines = [
        ChannelParticipantInline,
    ]


#################################################################################
#################################################################################

admin.site.register(models.TelegramAccount, TelegramAccountAdmin)
admin.site.register(models.TelegramChannel)
admin.site.register(models.AddChannelRequest)

admin.site.register(models.User, UserAdmin)
admin.site.register(models.Chat, ChatAdmin)
admin.site.register(models.Membership, MembershipAdmin)
admin.site.register(models.Message, MessageAdmin)
admin.site.register(models.MessageView)
admin.site.register(models.Entity)
admin.site.register(models.EntityType)
admin.site.register(models.ChatMemberCount)
admin.site.register(models.ChatSharedMedia)
admin.site.register(models.Restriction)
admin.site.register(models.AdminLogEvent)
admin.site.register(models.AdminLogEventActionChangeTitle)
admin.site.register(models.AdminLogEventActionChangeAbout)
admin.site.register(models.AdminLogEventActionChangeUsername)
admin.site.register(models.AdminLogEventActionChangePhoto)
admin.site.register(models.AdminLogEventActionToggleInvites)
admin.site.register(models.AdminLogEventActionToggleSignatures)
admin.site.register(models.AdminLogEventActionUpdatePinned)
admin.site.register(models.AdminLogEventActionEditMessage)
admin.site.register(models.AdminLogEventActionDeleteMessage)
admin.site.register(models.AdminLogEventActionParticipantJoin)
admin.site.register(models.AdminLogEventActionParticipantLeave)
admin.site.register(models.AdminLogEventActionParticipantInvite)
admin.site.register(models.AdminLogEventActionToggleBan)
admin.site.register(models.AdminLogEventActionToggleAdmin)
admin.site.register(models.AdminLogEventActionChangeStickerSet)
admin.site.register(models.AdminLogEventActionTogglePreHistoryHidden)
admin.site.register(models.AdminLogEventActionDefaultBannedRights)
admin.site.register(models.AdminLogEventActionStopPoll)
admin.site.register(models.AdminLogEventActionChangeLinkedChat)
admin.site.register(models.AdminLogEventActionChangeLocation)
admin.site.register(models.AdminLogEventActionToggleSlowMode)
admin.site.register(models.ChannelParticipant)
admin.site.register(models.ChatBannedRight)
admin.site.register(models.ChatPermissions)
admin.site.register(models.AdminRights)
admin.site.register(models.SharedMediaAnalyzerMetaData)
admin.site.register(models.ChatMessageViewsAnalyzerMetaData)
admin.site.register(models.ChatMemberCountAnalyzerMetaData)
admin.site.register(models.ChatMembersAnalyzerMetaData)
admin.site.register(models.AdminLogAnalyzerMetaData)
