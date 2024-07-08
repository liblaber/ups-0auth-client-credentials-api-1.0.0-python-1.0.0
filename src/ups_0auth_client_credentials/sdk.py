# This file was generated by liblab | https://liblab.com/

from .services.security import SecurityService
from .net.environment import Environment


class Ups0authClientCredentials:
    def __init__(
        self,
        username: str = None,
        password: str = None,
        base_url: str = Environment.DEFAULT.value,
    ):
        """
        Initializes Ups0authClientCredentials the SDK class.
        """
        self.security = SecurityService(base_url=base_url)
        self.set_basic_auth(username=username, password=password)

    def set_base_url(self, base_url):
        """
        Sets the base URL for the entire SDK.
        """
        self.security.set_base_url(base_url)

        return self

    def set_basic_auth(self, username: str, password: str):
        """
        Sets the username and password for the entire SDK.
        """
        self.security.set_basic_auth(username=username, password=password)

        return self


# c029837e0e474b76bc487506e8799df5e3335891efe4fb02bda7a1441840310c
