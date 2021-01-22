from .create_add_channel_request import CreateAddChannelRequest
from .add_channel_request_exists import AddChannelRequestExists


class Requests(
    CreateAddChannelRequest,
    AddChannelRequestExists,

):
    pass
