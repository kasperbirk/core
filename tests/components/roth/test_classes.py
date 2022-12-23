"""Test the touchline-sl custom classes."""
import unittest

from homeassistant.components.roth.roth_user import User, UserHelper


class TestUserCreation(unittest.TestCase):
    """Class for testing roth user."""

    def test_gettoken(self):
        """Test method for testing fetch of token."""
        response = """{
        "authenticated": true,
        "user_id": 324938602,
        "access_google_home": false,
        "token": "eyJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6InVzZXJmb3J0ZXN0IiwidXNlcl9pZCI6MzI0OTM4NjAyLCJpYXQiOjE2NzE1NzAyNjd9.oEBXk4umkHH5KVrDUvaXCi-GVeFn3Yps1eq6DVV8ZFY"
        }"""

        self.assertEqual(
            UserHelper.digest_api_response(self, response),
            "eyJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6InVzZXJmb3J0ZXN0IiwidXNlcl9pZCI6MzI0OTM4NjAyLCJpYXQiOjE2NzE1NzAyNjd9.oEBXk4umkHH5KVrDUvaXCi-GVeFn3Yps1eq6DVV8ZFY",
        )

    def test_class_init(self):
        """Test user class init."""
        user = User("abcdefg", "12345678")
        self.assertEqual(user.username, "abcdefg")
        self.assertEqual(user.password, "12345678")
        with self.assertRaises(ValueError):
            User("1", "12345678")
        with self.assertRaises(ValueError):
            User("abcdefg", "1")

    def test_integration_roth_api_authentication(self):
        """Call roth API for testing of the authentication.

        Using static user for testing:
        {"username": "userfortest", "password": "gexnug-8kenbE-sazqif"}
        """
        # user = User("userfortest", "gexnug-8kenbE-sazqif")


if __name__ == "__main__":
    unittest.main()
