from .analyze_admin_logs_task import AnalyzeAdminLogsTask
from .init_clients_task import InitClientsTask
from .iterate_dialogs_task import IterateDialogsTask
from .get_me_task import GetMeTask


class TelegramTasks(
    AnalyzeAdminLogsTask,
    InitClientsTask,
    IterateDialogsTask,
    GetMeTask,

):
    pass
