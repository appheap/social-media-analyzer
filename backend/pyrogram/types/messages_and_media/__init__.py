from .animation import Animation
from .audio import Audio
from .contact import Contact
from .dice import Dice
from .document import Document
from .game import Game
from .location import Location
from .message import Message
from .message_entity import MessageEntity
from .photo import Photo
from .poll import Poll
from .poll_option import PollOption
from .sticker import Sticker
from .stripped_thumbnail import StrippedThumbnail
from .thumbnail import Thumbnail
from .venue import Venue
from .video import Video
from .video_note import VideoNote
from .voice import Voice
from .webpage import WebPage

# added
from .sticker_set import StickerSet
from .photo_size_base import PhotoSizeBase
from .photo_size_empty import PhotoSizeEmpty
from .photo_size import PhotoSize
from .photo_cached_size import PhotoCachedSize
from .photo_stripped_size import PhotoStrippedSize
from .photo_size_progressive import PhotoSizeProgressive
from .photo_path_size import PhotoPathSize
from .file_location import FileLocation
from .message_views import MessageViews
from .message_replies import MessageReplies

__all__ = [
    "Animation", "Audio", "Contact", "Document", "Game", "Location", "Message", "MessageEntity", "Photo", "Thumbnail",
    "StrippedThumbnail", "Poll", "PollOption", "Sticker", "Venue", "Video", "VideoNote", "Voice", "WebPage", "Dice",

    # added
    "StickerSet",
    "PhotoSizeBase",
    "PhotoSizeEmpty",
    "PhotoSize",
    "PhotoCachedSize",
    "PhotoStrippedSize",
    "PhotoSizeProgressive",
    "PhotoPathSize",
    "MessageViews",
    "MessageReplies",

    "FileLocation",

]
