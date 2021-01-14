from .analyze_admin_logs_task import AnalyzeAdminLogsTask
from .init_clients_task import InitClientsTask
from .iterate_dialogs_task import IterateDialogsTask
from .get_me_task import GetMeTask
from .analyze_chat_shared_medias_task import AnalyzeChatSharedMediasTask
from .analyze_chat_members_task import AnalyzeChatMembersTask
from .analyze_chat_member_count_task import AnalyzeChatMemberCountTask


class TelegramTasks(
    AnalyzeAdminLogsTask,
    InitClientsTask,
    IterateDialogsTask,
    GetMeTask,
    AnalyzeChatSharedMediasTask,
    AnalyzeChatMembersTask,
    AnalyzeChatMemberCountTask,

):
    pass
