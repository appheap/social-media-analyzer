from tasks.task_scaffold import TaskScaffold
import pyrogram
from ..base_response import BaseResponse


class GetMeTask(TaskScaffold):
    def get_me_task(self, *args, **kwargs) -> BaseResponse:
        data = {}
        for client_session_name, task_queue in self.task_queues.items():
            client = self.get_client(client_session_name)
            data.update({
                str(client_session_name): str(client('get_me'))
            })
        return BaseResponse().done(data=data)
