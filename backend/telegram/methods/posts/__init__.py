from .get_post_by_id import GetPostByID
from .get_file_by_hash_digest import GetFileByHashDigest


class Posts(
    GetPostByID,
    GetFileByHashDigest,
):
    pass
