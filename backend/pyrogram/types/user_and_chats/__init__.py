from .chat import Chat
from .chat_member import ChatMember
from .chat_permissions import ChatPermissions
from .chat_photo import ChatPhoto
from .chat_preview import ChatPreview
from .dialog import Dialog
from .restriction import Restriction
from .user import User

# added
from .peer_notify_settings import PeerNotifySettings

__all__ = [
    "Chat", "ChatMember", "ChatPermissions", "ChatPhoto", "ChatPreview", "Dialog", "User", "Restriction",

    # added
    "PeerNotifySettings",
]
