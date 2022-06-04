import unittest
from authapi import AuthAPI
from authapi.providers.google.ads import AuthData
from cloudops_google_secretmanager import SecretManager


class DummySecret:
    def push(self):
        pass

    def pull(self):
        pass


class TestInstantiation(unittest.TestCase):
    def setUp(self):
        app_token = DummySecret()

        auth_data = AuthData(
            client_id="...",
            client_secret="...",
        )
        self.app = AuthAPI(
            name="DummyApp",
            auth_data=auth_data,
            token_secret=app_token,
        )

    def test_dummy(self):
        self.assertEqual(True, True, "I leave Python!")
