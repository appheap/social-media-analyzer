from django.contrib import admin

from .models import *


# Register your models here.
class TelegramChannelInline(admin.TabularInline):
    model = TelegramChannel


class ChatsInline(admin.TabularInline):
    model = Chat


class AdminLogEventInline(admin.TabularInline):
    model = AdminLogEvent


class MessageViewInline(admin.TabularInline):
    model = MessageView


class MemberCountHistoryInline(admin.TabularInline):
    model = ChatMemberCount


class SharedMediaHistoryInline(admin.TabularInline):
    model = ChatSharedMedia


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
    model = TelegramAccount


class ForwardedMessageInline(admin.TabularInline):
    model = Message
    fk_name = 'forward_from'
    verbose_name_plural = 'Forwarded Messages'


class SentMessageInline(admin.TabularInline):
    model = Message
    fk_name = 'from_user'
    verbose_name_plural = 'Sent Messages'


class ViaBotMessageInline(admin.TabularInline):
    model = Message
    fk_name = 'via_bot'
    verbose_name_plural = 'Inline Messages'


class InvitedParticipantInline(admin.TabularInline):
    model = ChannelParticipant
    fk_name = 'invited_by'
    verbose_name_plural = 'Invited Participants'


class PromotedParticipantInline(admin.TabularInline):
    model = ChannelParticipant
    fk_name = 'promoted_by'
    verbose_name_plural = 'Promoted Participants'


class DemotedParticipantInline(admin.TabularInline):
    model = ChannelParticipant
    fk_name = 'demoted_by'
    verbose_name_plural = 'Demoted Participants'


class KickedParticipantInline(admin.TabularInline):
    model = ChannelParticipant
    fk_name = 'kicked_by'
    verbose_name_plural = 'Kicked Participants'


class MentionedInline(admin.TabularInline):
    model = Entity
    fk_name = 'user'
    verbose_name_plural = 'Mentions'


class MembershipInline(admin.TabularInline):
    model = Membership


class ProfilePhotoInline(admin.TabularInline):
    model = Photo
    verbose_name_plural = 'Profile Photos'


class UserAdmin(admin.ModelAdmin):
    inlines = [
        TelegramAccountInline,
        MembershipInline,
        ProfilePhotoInline,
        # ForwardedMessageInline,
        # SentMessageInline,
        # ViaBotMessageInline,
        # InvitedParticipantInline,
        # PromotedParticipantInline,
        # DemotedParticipantInline,
        # KickedParticipantInline,
        # MentionedInline,
    ]


#################################################################################

class ChatMemberInline(admin.TabularInline):
    model = User.chats.through
    verbose_name_plural = 'Members'


class LinkedChatInline(admin.TabularInline):
    model = Chat
    verbose_name_plural = 'Linked Chats'


class MessageInline(admin.TabularInline):
    model = Message
    fk_name = 'chat'
    verbose_name_plural = 'Messages'


class ForwardedMessageChannelInline(admin.TabularInline):
    model = Message
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
    model = Entity


class EntityTypeInline(admin.TabularInline):
    model = EntityType


class MessageReplyInline(admin.TabularInline):
    model = Message
    verbose_name_plural = 'Replies'


class ActionMessagePinnedInline(admin.TabularInline):
    model = AdminLogEventActionUpdatePinned
    verbose_name_plural = 'Pinned Actions'


class ActionMessageEditedPrevInline(admin.TabularInline):
    model = AdminLogEventActionEditMessage
    verbose_name_plural = 'Action Edit Prevs'
    fk_name = 'prev_message'


class ActionMessageEditedNewInline(admin.TabularInline):
    model = AdminLogEventActionEditMessage
    verbose_name_plural = 'Action Edit News'
    fk_name = 'new_message'


class ActionMessageStopPollInline(admin.TabularInline):
    model = AdminLogEventActionStopPoll
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
    model = ChannelParticipant
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

admin.site.register(TelegramAccount, TelegramAccountAdmin)
admin.site.register(TelegramChannel)
admin.site.register(AddChannelRequest)

admin.site.register(User, UserAdmin)
admin.site.register(Dialog)
admin.site.register(Chat, ChatAdmin)
admin.site.register(Membership, MembershipAdmin)
admin.site.register(Message, MessageAdmin)
admin.site.register(Photo)
admin.site.register(MessageView)
admin.site.register(Entity)
admin.site.register(EntityType)
admin.site.register(ChatMemberCount)
admin.site.register(ChatSharedMedia)
admin.site.register(Restriction)
admin.site.register(AdminLogEvent)
admin.site.register(AdminLogEventActionChangeTitle)
admin.site.register(AdminLogEventActionChangeAbout)
admin.site.register(AdminLogEventActionChangeUsername)
admin.site.register(AdminLogEventActionChangePhoto)
admin.site.register(AdminLogEventActionToggleInvites)
admin.site.register(AdminLogEventActionToggleSignatures)
admin.site.register(AdminLogEventActionUpdatePinned)
admin.site.register(AdminLogEventActionEditMessage)
admin.site.register(AdminLogEventActionDeleteMessage)
admin.site.register(AdminLogEventActionParticipantJoin)
admin.site.register(AdminLogEventActionParticipantLeave)
admin.site.register(AdminLogEventActionParticipantInvite)
admin.site.register(AdminLogEventActionToggleBan)
admin.site.register(AdminLogEventActionToggleAdmin)
admin.site.register(AdminLogEventActionChangeStickerSet)
admin.site.register(AdminLogEventActionTogglePreHistoryHidden)
admin.site.register(AdminLogEventActionDefaultBannedRights)
admin.site.register(AdminLogEventActionStopPoll)
admin.site.register(AdminLogEventActionChangeLinkedChat)
admin.site.register(AdminLogEventActionChangeLocation)
admin.site.register(AdminLogEventActionToggleSlowMode)
admin.site.register(ChannelParticipant)
admin.site.register(ChatBannedRight)
admin.site.register(ChatPermissions)
admin.site.register(AdminRights)
admin.site.register(SharedMediaAnalyzerMetaData)
admin.site.register(ChatMessageViewsAnalyzerMetaData)
admin.site.register(ChatMemberCountAnalyzerMetaData)
admin.site.register(ChatMembersAnalyzerMetaData)
admin.site.register(AdminLogAnalyzerMetaData)
