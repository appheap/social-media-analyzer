from django.db.models.signals import (pre_save, post_save, pre_delete, )
from django.dispatch import receiver

from core.globals import logger
from .models import *
from . import tasks

# @receiver(pre_save, sender=models.AddChannelRequest)
# def handle_presave(sender, **kwargs):
#     logger.info(f'\npresave: {str(sender)} : {kwargs}')
from utils.utils import prettify


@receiver(post_save, sender=models.AddChannelRequest)
def handle_postsave(sender, instance, created, update_fields, raw, **kwargs):
    # def handle_postsave(sender,**kwargs):
    logger.info(f"\npostsave: {str(sender)} : <{str(instance)}> : {kwargs}")


@receiver(pre_save, sender=models.Message)
def handle_presave(sender, instance, **kwargs):
    logger.info(f"\npresave: {str(sender)} : <{prettify(instance.__dict__)}> : {kwargs}")


@receiver(pre_delete, sender=models.Chat)
def handle_predelete(sender, instance, **kwargs):
    logger.info(f"\npre_delete: {str(sender)} : <{prettify(instance.__dict__)}> : {kwargs}")
    messages = models.Message.objects.filter(
        forward_from_chat=instance,
    )
    if messages:
        for message in messages:
            logger.info(message)
    # db_chat = models.Chat.objects.get(chat_id=instance.chat_id)
    # logger.info(db_chat.messages)


@receiver(post_save, sender=Post)
def post_postsave(sender, instance: 'Post', created: 'bool', update_fields, raw, **kwargs):
    if created:
        if instance.is_scheduled:
            if instance.upload_to_telegram_schedule_list:
                # upload to the telegram now
                tasks.upload_post.apply_async(
                    kwargs={
                        'db_post_id': instance.id,
                    },
                    countdown=1
                )
            else:
                # schedule to upload to the telegram later
                pass
        else:
            # send now
            tasks.upload_post.apply_async(
                kwargs={
                    'db_post_id': instance.id,
                },
                countdown=1
            )
    else:
        pass
