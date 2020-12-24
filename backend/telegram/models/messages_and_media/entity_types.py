from django.db import models


class EntitySourceTypes(models.TextChoices):
    text = "text"
    caption = "caption"


class EntityTypes(models.TextChoices):
    mention = 'mention'
    hashtag = 'hashtag'
    cashtag = 'cashtag'
    bot_command = 'bot_command'
    url = 'url'
    email = 'email'
    phone_number = 'phone_number'
    bold = 'bold'
    italic = 'italic'
    code = 'code'
    pre = 'pre'
    text_link = 'text_link'
    text_mention = 'text_mention'
    undefined = 'undefined'

    @staticmethod
    def get_type(entity_type: str):
        for choice in EntityTypes.choices:
            if choice[0] == entity_type:
                return getattr(EntityTypes, str(choice[0]).lower())
        else:
            return EntityTypes.undefined
