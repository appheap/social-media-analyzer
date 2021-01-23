from django import forms

from ..models import *


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
