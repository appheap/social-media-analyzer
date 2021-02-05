from django.contrib import admin

from .models import *
from django.core.paginator import Paginator


class NoCountPaginator(Paginator):
    @property
    def count(self):
        return 999999999  # Some arbitrarily large number,
        # so we can still get our page tab.


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
        # ChatsInline,
        MemberCountHistoryInline,
        SharedMediaHistoryInline,
        MessageViewInline,
        AdminLogEventInline,
    ]
    list_display = ['first_name', 'username', 'created_ts', 'modified_ts']


class TelegramChannelAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_select_related = ()
    raw_id_fields = (
        'site_user',
        'telegram_account',
        'chat',
        'blockage',
    )


#################################################################################

class TelegramAccountInline(admin.TabularInline):
    model = TelegramAccount


class ForwardedMessageInline(admin.TabularInline):
    model = Message
    fk_name = 'forward_from'
    verbose_name_plural = 'Forwarded Messages'


class SentMessageInline(admin.TabularInline):
    model = Message
    fk_name = 'user'
    verbose_name_plural = 'Sent Messages'


class ViaBotMessageInline(admin.TabularInline):
    model = Message
    fk_name = 'via_bot'
    verbose_name_plural = 'Inline Messages'


class InvitedParticipantInline(admin.TabularInline):
    model = ChatMember
    fk_name = 'invited_by'
    verbose_name_plural = 'Invited Participants'


class PromotedParticipantInline(admin.TabularInline):
    model = ChatMember
    fk_name = 'promoted_by'
    verbose_name_plural = 'Promoted Participants'


class DemotedParticipantInline(admin.TabularInline):
    model = ChatMember
    fk_name = 'demoted_by'
    verbose_name_plural = 'Demoted Participants'


class KickedParticipantInline(admin.TabularInline):
    model = ChatMember
    fk_name = 'kicked_by'
    verbose_name_plural = 'Kicked Participants'


class MentionedInline(admin.TabularInline):
    model = Entity
    fk_name = 'user'
    verbose_name_plural = 'Mentions'


class MembershipInline(admin.TabularInline):
    model = Membership


class ProfilePhotoInline(admin.TabularInline):
    model = ProfilePhoto
    verbose_name_plural = 'Profile Photos'


class UserAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_select_related = ()
    raw_id_fields = (
        'message_view',
    )
    fields = (
        'user_id',
        'first_name',
        'last_name',
        'username',
        'language_code',
        'dc_id',
        'phone_number',
        'can_we_pin_message',
        'about',
        'common_chats_count',
        'is_empty',
        'is_mutual_contact',
        'is_deleted',
        'is_bot',
        'is_verified',
        'is_restricted',
        'is_scam',
        'is_blocked',
        'is_support',
        'bot_inline_placeholder',
        'bot_can_see_history',
        'bot_can_request_geo',
    )

    inlines = [
        # TelegramAccountInline,
        # MembershipInline,
        # ProfilePhotoInline,
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
    list_per_page = 20
    list_select_related = ()
    raw_id_fields = (
        'channel',
        'group',
        'user',
        'shared_media_analyzer',
        'member_count_analyzer',
        'message_view_analyzer',
        'members_analyzer',
        'admin_log_analyzer',
    )
    fields = (
        'chat_id',
        'type',
        'channel',
        'group',
        'user',
        'shared_media_analyzer',
        'member_count_analyzer',
        'message_view_analyzer',
        'members_analyzer',
        'admin_log_analyzer',
    )

    inlines = [
        # TelegramChannelInline,
        # ChatMemberInline,
        # AdminLogEventInline,
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


# class MessageReplyInline(admin.TabularInline):
#     model = Message
#     verbose_name_plural = 'Replies'


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
    list_per_page = 20
    list_select_related = ()

    raw_id_fields = (
        'chat',
        'scheduled_message',
        'sender_chat',
        'user',
        'forward_from_chat',
        'forward_from_user',
        'forward_from_message',
        'saved_from_chat',
        'saved_from_user',
        'via_bot',
        'reply_to_message',
        'reply_to_user',
        'reply_to_chat',
        'reply_to_top_message',
        'logged_by',
    )
    list_display = ('message_id', 'chat')
    show_full_result_count = False
    inlines = [
        # MessageReplyInline,
        # EntityInline,
        # EntityTypeInline,
        # MessageViewInline,
        # ActionMessagePinnedInline,
        # ActionMessageEditedPrevInline,
        # ActionMessageEditedNewInline,
        # ActionMessageStopPollInline,
    ]


class MessageViewAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_select_related = ()
    raw_id_fields = (
        'discussion_chat',
        'message',
        'logged_by',
        'chat',
    )


#################################################################################
class ChannelParticipantInline(admin.TabularInline):
    model = ChatMember
    fk_name = 'membership'
    verbose_name_plural = 'participant history'
    fields = (
        'user', 'type', 'join_date_ts', 'promoted_by',
        'invited_by', 'demoted_by', 'kicked_by',
        'admin_rights', 'banned_rights', 'can_promote_admins',
    )


class MembershipAdmin(admin.ModelAdmin):
    inlines = [
        ChannelParticipantInline,
    ]


class PostAdmin(admin.ModelAdmin):
    list_select_related = ()
    raw_id_fields = (
        'telegram_channel',
        'created_by',
        'sent_by',
    )

    fields = (
        'telegram_channel',
        'created_by',
        'is_scheduled',
        'schedule_date_ts',
        'upload_to_telegram_schedule_list',
        'is_uploaded_to_telegram_schedule_list',
        'is_sent',
        'sent_date_ts',
        'sent_by',
        'text',
        'has_media',
        'medias',
    )


class DialogAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_select_related = ()
    raw_id_fields = (
        'chat',
        'account'
    )


class ChannelAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_select_related = ()
    raw_id_fields = (
        'migrated_from',
        'linked_chat',
        'creator',
        'default_banned_rights',
    )


class AdminshipAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_select_related = ()
    raw_id_fields = (
        'account',
        'chat',
        'admin_rights',
        'banned_rights',
    )


#################################################################################
#################################################################################

admin.site.register(TelegramAccount, TelegramAccountAdmin)
admin.site.register(TelegramChannel, TelegramChannelAdmin)
admin.site.register(AddChannelRequest)

admin.site.register(User, UserAdmin)
admin.site.register(Dialog, DialogAdmin)
admin.site.register(Chat, ChatAdmin)
admin.site.register(Channel, ChannelAdmin)
admin.site.register(Group)
admin.site.register(AdminShip, AdminshipAdmin)
admin.site.register(Membership, MembershipAdmin)
admin.site.register(Message, MessageAdmin)
admin.site.register(MessageView, MessageViewAdmin)
admin.site.register(ProfilePhoto)
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
admin.site.register(ChatMember)
admin.site.register(ChatPermissions)
admin.site.register(ChatAdminRights)
admin.site.register(SharedMediaAnalyzerMetaData)
admin.site.register(ChatMessageViewsAnalyzerMetaData)
admin.site.register(ChatMemberCountAnalyzerMetaData)
admin.site.register(ChatMembersAnalyzerMetaData)
admin.site.register(AdminLogAnalyzerMetaData)
admin.site.register(Post, PostAdmin)
admin.site.register(File)
