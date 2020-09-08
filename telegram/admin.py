from django.contrib import admin
from . import models
from users import models as user_models


# Register your models here.
class TelegramChannelInline(admin.TabularInline):
    model = models.TelegramChannel


class TelegramAccountAdmin(admin.ModelAdmin):
    inlines = [
        TelegramChannelInline,
    ]
    list_display = ['first_name', 'username', 'created_at', 'modified_at']


admin.site.register(models.TelegramAccount, TelegramAccountAdmin)
admin.site.register(models.TelegramChannel)

admin.site.register(models.User)
admin.site.register(models.Chat)
admin.site.register(models.Message)
admin.site.register(models.MessageView)
admin.site.register(models.Entity)
admin.site.register(models.EntityType)
admin.site.register(models.ChatMemberCount)
admin.site.register(models.ChatSharedMedia)
admin.site.register(models.Restriction)
admin.site.register(models.AdminLog)
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
admin.site.register(models.ChannelParticipantSelf)
admin.site.register(models.ChannelParticipantCreator)
admin.site.register(models.ChannelParticipantAdmin)
admin.site.register(models.ChannelParticipantBanned)
admin.site.register(models.ChatBannedRight)
admin.site.register(models.ChatPermissions)
admin.site.register(models.AdminRights)
