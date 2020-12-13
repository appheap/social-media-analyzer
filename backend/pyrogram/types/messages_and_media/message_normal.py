import pyrogram
from pyrogram import types, raw
from ..object import Object
from typing import List, Union


class MessageNormal(Object):
    """
    """

    def __init__(
            self,
            *,
            client: "pyrogram.Client" = None,

            edit_date: int = None,
            is_outgoing: bool = None,
            mentioned: bool = None,
            media_unread: bool = None,
            is_silent: bool = None,
            is_post: bool = None,
            post_author: str = None,
            from_scheduled: bool = None,
            legacy: bool = None,
            edit_hide: bool = None,
            is_pinned: bool = None,
            media_group_id: int = None,
            from_chat: "types.Chat" = None,
            from_user: "types.User" = None,
            forward_header: "types.MessageForwardHeader" = None,
            via_bot: "types.User" = None,
            reply_header: "types.MessageReplyHeader" = None,
            text: "types.Str" = None,
            media: Union[
                None,
                "types.Photo",
                "types.GeoPoint",
                "types.Contact",
                "types.Document",
                "types.WebPage",
                "types.Venue",
                "types.Game",
                "types.Invoice",
                "types.GeoLive",
                "types.Poll",
                "types.Dice",
            ] = None,
            media_type: str = None,
            reply_markup: Union[
                "types.InlineKeyboardMarkup",
                "types.ReplyKeyboardMarkup",
                "types.ReplyKeyboardRemove",
                "types.ForceReply"
            ] = None,
            entities: List["types.MessageEntity"] = None,
            views: "types.MessageViews" = None,
            restrictions: List["types.Restriction"] = None,
    ):
        super().__init__(client=client)

        self.edit_date = edit_date
        self.is_outgoing = is_outgoing
        self.mentioned = mentioned
        self.media_unread = media_unread
        self.is_silent = is_silent
        self.is_post = is_post
        self.post_author = post_author
        self.from_scheduled = from_scheduled
        self.legacy = legacy
        self.edit_hide = edit_hide
        self.is_pinned = is_pinned
        self.media_group_id = media_group_id
        self.from_chat = from_chat
        self.from_user = from_user
        self.forward_header = forward_header
        self.via_bot = via_bot
        self.reply_header = reply_header
        self.text = text
        self.media = media
        self.media_type = media_type
        self.reply_markup = reply_markup
        self.entities = entities
        self.views = views
        self.restrictions = restrictions

    @staticmethod
    async def _parse(client, message: raw.types.Message, users: dict, chats: dict):
        if message is None:
            return None

        entities = [types.MessageEntity._parse(client, entity, users) for entity in message.entities]
        entities = types.List(filter(lambda x: x is not None, entities))

        from_id = message.from_id
        from_chat = None
        from_user = None
        if from_id:
            if isinstance(from_id, raw.types.PeerUser):
                from_user = types.User._parse(client, users.get(from_id.user_id, None))
            else:
                if isinstance(from_id, raw.types.PeerChannel):
                    _peer_id = from_id.channel_id
                else:
                    _peer_id = from_id.chat_id

                from_chat = types.Chat._parse_chat(client, chats.get(_peer_id, None))

        reply_markup = message.reply_markup

        if reply_markup:
            if isinstance(reply_markup, raw.types.ReplyKeyboardForceReply):
                reply_markup = types.ForceReply.read(reply_markup)
            elif isinstance(reply_markup, raw.types.ReplyKeyboardMarkup):
                reply_markup = types.ReplyKeyboardMarkup.read(reply_markup)
            elif isinstance(reply_markup, raw.types.ReplyInlineMarkup):
                reply_markup = types.InlineKeyboardMarkup.read(reply_markup)
            elif isinstance(reply_markup, raw.types.ReplyKeyboardHide):
                reply_markup = types.ReplyKeyboardRemove.read(reply_markup)
            else:
                reply_markup = None

        raw_media = message.media
        media = None
        media_type = None
        if raw_media:
            if isinstance(raw_media, raw.types.MessageMediaPhoto):
                media = types.Photo._parse(client, raw_media.photo, raw_media.ttl_seconds)
                media_type = 'photo'

            elif isinstance(raw_media, raw.types.MessageMediaGeo):
                media = types.Geo._parse(client, raw_media)
                media_type = 'location'

            elif isinstance(raw_media, raw.types.MessageMediaContact):
                media = types.Contact._parse(client, raw_media)
                media_type = 'contact'

            elif isinstance(raw_media, raw.types.MessageMediaDocument):
                doc = raw_media.document

                if isinstance(doc, raw.types.Document):
                    attributes = {type(i): i for i in doc.attributes}

                    file_name = getattr(
                        attributes.get(
                            raw.types.DocumentAttributeFilename, None
                        ), "file_name", None
                    )

                    if raw.types.DocumentAttributeAudio in attributes:
                        audio_attributes = attributes[raw.types.DocumentAttributeAudio]

                        if audio_attributes.voice:
                            media = types.Voice._parse(client, doc, audio_attributes)
                            media_type = 'voice'
                        else:
                            media = types.Audio._parse(client, doc, audio_attributes, file_name)
                            media_type = 'audio'
                    elif raw.types.DocumentAttributeAnimated in attributes:
                        video_attributes = attributes.get(raw.types.DocumentAttributeVideo, None)

                        media = types.Animation._parse(client, doc, video_attributes, file_name)
                        media_type = 'animation'
                    elif raw.types.DocumentAttributeVideo in attributes:
                        video_attributes = attributes[raw.types.DocumentAttributeVideo]

                        if video_attributes.round_message:
                            media = types.VideoNote._parse(client, doc, video_attributes)
                            media_type = 'video_note'
                        else:
                            media = types.Video._parse(client, doc, video_attributes, file_name,
                                                       raw_media.ttl_seconds)
                            media_type = 'video'
                    elif raw.types.DocumentAttributeSticker in attributes:
                        media = await types.Sticker._parse(
                            client, doc,
                            attributes.get(raw.types.DocumentAttributeImageSize, None),
                            attributes[raw.types.DocumentAttributeSticker],
                            file_name
                        )
                        media_type = 'sticker'
                    else:
                        media = types.Document._parse(client, doc, file_name)
                        media_type = 'document'

            elif isinstance(raw_media, raw.types.MessageMediaWebPage):
                if isinstance(raw_media.webpage, raw.types.WebPage):
                    media = types.WebPage._parse(client, raw_media.webpage)
                    media_type = 'webpage'
                else:
                    media = None

            elif isinstance(raw_media, raw.types.MessageMediaVenue):
                media = types.Venue._parse(client, raw_media)
                media_type = 'venue'

            elif isinstance(raw_media, raw.types.MessageMediaGame):
                media = types.Game._parse(client, message)
                media_type = 'game'

            elif isinstance(raw_media, raw.types.MessageMediaInvoice):
                media = types.Invoice._parse(client, raw_media)
                media_type = 'invoice'

            elif isinstance(raw_media, raw.types.MessageMediaGeoLive):
                media = types.GeoLive._parse(client, raw_media)
                media_type = 'live_location'

            elif isinstance(raw_media, raw.types.MessageMediaPoll):
                media = types.Poll._parse(client, raw_media)
                media_type = 'poll'

            elif isinstance(raw_media, raw.types.MessageMediaDice):
                media = types.Dice._parse(client, raw_media)
                media_type = 'dice'

            else:
                media = None

        return MessageNormal(
            client=client,

            edit_date=getattr(message, 'edit_date', None),
            is_outgoing=getattr(message, 'out', None),
            mentioned=getattr(message, 'mentioned', None),
            media_unread=getattr(message, 'media_unread', None),
            is_silent=getattr(message, 'silent', None),
            is_post=getattr(message, 'post', None),
            from_scheduled=getattr(message, 'from_scheduled', None),
            legacy=getattr(message, 'legacy', None),
            edit_hide=getattr(message, 'edit_hide', None),
            is_pinned=getattr(message, 'pinned', None),
            media_group_id=getattr(message, 'grouped_id', None),
            from_chat=from_chat,
            from_user=from_user,
            forward_header=await types.MessageForwardHeader._parse(client, getattr(message, 'fwd_from', None), users,
                                                                   chats),
            via_bot=users.get(message.via_bot_id, None) if getattr(message, 'via_bot_id', None) else None,
            reply_header=types.MessageReplyHeader._parse(client, getattr(message, 'reply_to', None), users, chats),
            text=types.Str(message.message).init(entities) or None,
            media=media,
            media_type=media_type,
            reply_markup=reply_markup,
            entities=entities,
            views=await types.MessageViews._parse_from_message(client, message.id, message, users, chats),
            restrictions=types.List([types.Restriction._parse(restriction) for restriction in
                                     getattr(message, 'restrictions', [])]) or None,
        )
