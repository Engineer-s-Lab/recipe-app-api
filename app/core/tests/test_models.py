from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelTests(TestCase):

    def test_create_user_with_email(self):
        email = "test@alphabyte.xyz"
        password = "Testpass123"
        user = get_user_model().objects.create_user(
            email = email,
            password = password
        )

        self.assertEqual(user.email,email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        # Test the email for new user is normalized
        email = "test@ALPHABYTE.XYZ"
        user = get_user_model().objects.create_user(email,'test123')

        self.assertEqual(user.email,email.lower())
    
    def test_new_user_invalid_email(self):
        # Test if raises error when creating user with no email
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None,'test123')

    def test_create_new_superuser(self):
        # Test creating super user
        user = get_user_model().objects.create_superuser(
            'test@alphabyte.xyz',
            'test123'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)



