from django.contrib.auth import get_user_model
from django.test import TestCase


class CustomUserTests(TestCase):

    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username='Danil',
            email="test@tpu.ru",
            password='testpass123'
        )
        self.assertEqual(user.username, 'Danil')
        self.assertEqual(user.email, 'test@tpu.ru')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
