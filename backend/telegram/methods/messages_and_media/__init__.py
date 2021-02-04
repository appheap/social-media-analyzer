from .get_updated_message import GetUpdatedMessage
from .get_updated_messages import GetUpdatedMessages
from .update_message_and_view import UpdateMessageAndView
from .get_message_by_message_id import GetMessageByMessageId
from .get_message_from_raw import GetMessageFromRaw
from .get_updated_message_entities import GetUpdatedMessageEntities
from .get_updated_message_entity_types import GetUpdatedMessageEntityTypes
from .profile_photo_exists import ProfilePhotoExists
from .get_updated_profile_photo import GetUpdatedProfilePhoto
from .get_latest_profile_photo import GetLatestProfilePhoto


class MessageAndMedia(
    GetUpdatedMessage,
    GetUpdatedMessages,
    UpdateMessageAndView,
    GetMessageByMessageId,
    GetMessageFromRaw,
    GetUpdatedMessageEntities,
    GetUpdatedMessageEntityTypes,
    ProfilePhotoExists,
    GetUpdatedProfilePhoto,
    GetLatestProfilePhoto,

):
    pass
