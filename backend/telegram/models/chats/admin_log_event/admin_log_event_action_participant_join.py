from ...base import BaseModel


class AdminLogEventActionParticipantJoin(BaseModel):
    """
    A user has joined the group (in the case of big groups, info of the user that has joined isn't shown)
    """

    ###########################################
    # `admin_log_event` : AdminLogEvent this action belongs to

    class Meta:
        verbose_name_plural = 'Events (participant join)'
