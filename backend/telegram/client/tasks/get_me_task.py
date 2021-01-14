from tasks.task_scaffold import TaskScaffold
import pyrogram
from ..base_response import BaseResponse


class GetMeTask(TaskScaffold):
    def get_me_task(self, *args, **kwargs) -> BaseResponse:
        data = {}
        for client in self.clients:
            client: pyrogram.Client = client
            data.update({
                str(client.session_name): str(client.get_me())
            })
        return BaseResponse().done(data=data)
