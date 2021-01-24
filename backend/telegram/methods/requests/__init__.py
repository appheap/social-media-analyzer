from .create_add_channel_request import CreateAddChannelRequest
from .undone_add_channel_request_exists import UndoneAddChannelRequestExists


class Requests(
    CreateAddChannelRequest,
    UndoneAddChannelRequestExists,

):
    pass
