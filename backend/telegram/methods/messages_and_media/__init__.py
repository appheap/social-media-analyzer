from .get_updated_message import GetUpdatedMessage
from .get_updated_message_entities import GetUpdatedMessageEntities
from .get_updated_message_entity_types import GetUpdatedMessageEntityTypes


class MessageAndMedia(
    GetUpdatedMessage,
    GetUpdatedMessageEntities,
    GetUpdatedMessageEntityTypes,

):
    pass
