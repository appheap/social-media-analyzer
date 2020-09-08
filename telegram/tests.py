from django.test import TestCase
from django.contrib.auth import get_user_model

import arrow
from . import models
from users.tests import BaseTestCase
from utils.utils import prettify


# Create your tests here.

class TelegramTestCase(BaseTestCase):

    def create_telegram_account(self, user, blockage=None):
        return models.TelegramAccount.objects.create(
            user_id=100,
            first_name='sigma',
            last_name='phi',
            username='sigma',
            dc_id=2,
            phone_number='+989189991234',
            custom_user=user,
            is_bot=False,
            is_scam=False,
            is_restricted=False,
            is_deleted=False,
            language_code='en',
            blockage=blockage,
        )

    def create_telegram_channel(self, telegram_account, blockage=None):
        return models.TelegramChannel.objects.create(
            channel_id=1,
            is_public=True,
            telegram_account=telegram_account,
            blockage=blockage,
        )

    def test_create_telegram_account(self):
        print("\n\ntest_create_telegram_account:")

        new_user = self.create_user()
        telegram_account = self.create_telegram_account(new_user)
        self.assertEqual(models.TelegramAccount.objects.all().count(), 1)
        self.assertEqual(models.TelegramAccount.objects.all()[0].user_id, 100)
        self.assertEqual(models.TelegramAccount.objects.all()[0].first_name, 'sigma')

        print(prettify(telegram_account))

    def test_telegram_channel(self):
        print("\n\ntest_telegram_channel:")

        new_user = self.create_user()
        telegram_account = self.create_telegram_account(new_user)
        telegram_channel = self.create_telegram_channel(telegram_account)

        self.assertEqual(models.TelegramChannel.objects.all().count(), 1)
        self.assertEqual(models.TelegramChannel.objects.all()[0].channel_id, 1)

        print(prettify(telegram_channel))

    def test_blockage_telegram_account(self):
        print("\n\ntest_blockage_telegram_account:")
        new_user = self.create_user()
        telegram_account = self.create_telegram_account(new_user, self.create_blockage())

        # self.assertEqual(models.Blockage.objects.all().count(), 1)
        # self.assertEqual(models.Blockage.objects.all()[0].blocked, True)
        # self.assertEqual(models.Blockage.objects.all()[0].blocked_at, self.timestamp)

        print(prettify(telegram_account))

    def test_blockage_telegram_channel(self):
        print("\n\ntest_blockage_telegram_channel:")
        new_user = self.create_user()
        telegram_account = self.create_telegram_account(new_user)
        telegram_channel = self.create_telegram_channel(telegram_account, self.create_blockage())

        # self.assertEqual(models.Blockage.objects.all().count(), 1)
        # self.assertEqual(models.Blockage.objects.all()[0].blocked, True)
        # self.assertEqual(models.Blockage.objects.all()[0].blocked_at, self.timestamp)

        print(prettify(telegram_channel))
