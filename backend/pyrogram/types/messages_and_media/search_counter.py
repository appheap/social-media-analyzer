from pyrogram import raw
from ..object import Object

_filter_names = {'InputMessagesFilterPhotos': 'photo', 'InputMessagesFilterVideo': 'video',
                 'InputMessagesFilterDocument': 'document', 'InputMessagesFilterMusic': 'music',
                 'InputMessagesFilterUrl': 'url', 'InputMessagesFilterVoice': 'voice',
                 'InputMessagesFilterRoundVideo': 'video_note', 'InputMessagesFilterGif': 'animation',
                 'InputMessagesFilterGeo': 'location', 'InputMessagesFilterContacts': 'contact'}


class SearchCounter(Object):

    def __init__(
            self,
            *,
            count: int,
            filter_name: str,
            inexact: bool = None,
    ):
        super().__init__()

        self.count = count
        self.filter_name = filter_name
        self.inexact = inexact

    @staticmethod
    def _parse(*, raw_obj: raw.types.messages.SearchCounter):
        if raw_obj is None:
            return None

        class_name = raw_obj.filter.__class__.__name__
        if class_name not in _filter_names:
            return None
        else:
            filter_name = _filter_names[class_name]

        return SearchCounter(
            count=raw_obj.count,
            filter_name=filter_name,
            inexact=getattr(raw_obj, 'inexact', None)
        )
