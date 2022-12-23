"""Handle the user."""

import json

import aiohttp


class User:
    """Class for handling the user."""

    def __init__(self, username, password):
        """Initialize the user for later authentication against API."""
        if len(username) < 6:
            raise ValueError("Username must be at least 6 characters long")
        if len(password) < 8:
            raise ValueError("Password must be at least 8 characters long")

        self.username = username
        self.password = password
        self.token = None
        self.url = "https://emodul.eu/api/v1/authentication"

    async def authenticate(self):
        """Authenticate the user."""
        async with aiohttp.ClientSession() as session:
            async with session.post(
                self.url,
                # json={"username": self.username, "password": self.password},
                json={"username": "userfortest", "password": "gexnug-8kenbE-sazqif"},
            ) as resp:
                if resp.status == 200:
                    self.token = (await resp.json())["token"]
                else:
                    raise Exception("Authentication failed")


class UserHelper:
    """Helper class for helper methods related to User class."""

    def digest_api_response(self, response):
        """Digest service request."""
        json_request = json.loads(response)
        if json_request["authenticated"]:
            return json_request["token"]
