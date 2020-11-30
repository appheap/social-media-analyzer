from ..object import Object

"""- :obj:`~pyrogram.types.InputLocationMessageContent`
    - :obj:`~pyrogram.types.InputVenueMessageContent`
    - :obj:`~pyrogram.types.InputContactMessageContent`"""


class InputMessageContent(Object):
    """Content of a message to be sent as a result of an inline query.

    Pyrogram currently supports the following types:

    - :obj:`~pyrogram.types.InputTextMessageContent`
    """

    def __init__(self):
        super().__init__()

    def write(self, reply_markup):
        raise NotImplementedError
