from ...base import BaseModel


class AdminLogEventActionChangeStickerSet(BaseModel):
    """
    The supergroup's stickerset was changed
    """

    ###########################################
    # `admin_log_event` : AdminLogEvent this action belongs to

    class Meta:
        verbose_name_plural = 'Events (change sticker set)'
