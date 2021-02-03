from .log_admin_logs_task import LogAdminLogsTask
from .init_clients_task import InitClientsTask
from .iterate_dialogs_task import IterateDialogsTask
from .iterate_chat_history_task import IterateChatHistoryTask
from .log_message_views_task import LogMessageViewsTask
from .get_me_task import GetMeTask
from .log_chat_shared_medias_task import LogChatSharedMediasTask
from .log_chat_members_task import LogChatMembersTask
from .log_chat_member_count_task import LogChatMemberCountTask
from .add_telegram_channel_task import AddTelegramChannelTask
from .upload_post import UploadPost


class TelegramTasks(
    LogAdminLogsTask,
    InitClientsTask,
    IterateDialogsTask,
    IterateChatHistoryTask,
    LogMessageViewsTask,
    GetMeTask,
    LogChatSharedMediasTask,
    LogChatMembersTask,
    LogChatMemberCountTask,
    AddTelegramChannelTask,
    UploadPost,

):
    pass
