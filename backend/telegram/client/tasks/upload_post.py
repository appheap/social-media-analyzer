from tasks.task_scaffold import TaskScaffold
import pyrogram
from ..base_response import BaseResponse


class UploadPost(TaskScaffold):
    def upload_post(self, *args, **kwargs) -> BaseResponse:
        return BaseResponse().done()
