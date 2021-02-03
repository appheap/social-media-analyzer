from typing import Optional

from db.scaffold import Scaffold
from telegram import models as tg_models


class GetPostByID(Scaffold):
    def get_post_by_id(self, *, post_id: str) -> Optional['tg_models.Post']:
        if post_id is None:
            return None

        return self.tg_models.Post.posts.get_post_by_id(post_id=post_id)
