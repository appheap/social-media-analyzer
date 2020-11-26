from django import forms

from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.core.exceptions import ValidationError

from .models import *
from core.globals import logger


class TelegramChannelForm(forms.ModelForm):
    class Meta:
        model = TelegramChannel
        fields = ('username', 'telegram_account',)
        widgets = {
            'username': forms.TextInput(
                attrs={
                    'placeholder': 'username',
                    'required': True,
                    'class': 'form-control',
                    'name': 'username',
                },
            ),
            'telegram_account': forms.Select(
                attrs={
                    'required': True,
                }
            )
        }

    # def clean(self):
    #     cleaned_data = super().clean()
    # self.add_error('username','not valid!')
    # raise ValidationError('error!')

    # def clean_username(self):
    #     # logger.info(self.fields['username'].__dict__)
    #     # self.add_error('username', 'not valid!')
    #     pass


class AddChannelRequestForm(forms.ModelForm):
    class Meta:
        model = AddChannelRequest
        fields = ('channel_username', 'telegram_account',)
        widgets = {
            'channel_username': forms.TextInput(
                attrs={
                    'placeholder': 'username',
                    'required': True,
                    'class': 'form-control text-white',
                    'name': 'username',
                },
            ),
            'telegram_account': forms.Select(
                attrs={
                    'required': True,
                    'class': 'form-control text-white',
                }
            )
        }

    # def is_valid(self):
    #     logger.info('is_valid')
    #     return super().is_valid()
    #
    # def clean(self):
    #     cleaned_data = super().clean()
    # self.add_error('username','not valid!')
    # raise ValidationError('error!')

    # def clean_username(self):
    #     # logger.info(self.fields['username'].__dict__)
    #     # self.add_error('username', 'not valid!')
    #     pass
