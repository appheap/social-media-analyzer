from django.test import TestCase
from django.contrib.auth import get_user_model

import arrow
from . import models
from backend.utils.utils import prettify


# Create your tests here.


class BaseTestCase(TestCase):
    email = 'newuser@email.com'
    username = 'newuser'

    def setUp(self) -> None:
        self.timestamp = arrow.utcnow().timestamp

    def create_user(self, blockage=None):
        return get_user_model().objects.create_user(
            username=self.username,
            email=self.email,
            created_at=arrow.utcnow().timestamp,
            modified_at=arrow.utcnow().timestamp,
            blockage=blockage
        )

    def create_blockage(self):
        return models.Blockage.objects.create(
            blocked=True,
            blocked_at=self.timestamp,
            blocked_reason='just for test',
            blocked_type=models.BlockageTypes.TEMPORARY,
            blocked_until=self.timestamp + 60,
        )


class UsersTestCase(BaseTestCase):

    def test_create_user(self):
        print("\n\ntest_create_user:")

        new_user = self.create_user()
        self.assertEqual(get_user_model().objects.all().count(), 1)
        self.assertEqual(get_user_model().objects.all()[0].username, self.username)
        self.assertEqual(get_user_model().objects.all()[0].email, self.email)

        print(prettify(new_user))

    def test_blockage_user(self):
        print("\n\ntest_blockage_user:")

        user = self.create_user(blockage=self.create_blockage())

        self.assertEqual(models.Blockage.objects.all().count(), 1)
        self.assertEqual(models.Blockage.objects.all()[0].blocked, True)
        self.assertEqual(models.Blockage.objects.all()[0].blocked_at, self.timestamp)

        print(prettify(user))
