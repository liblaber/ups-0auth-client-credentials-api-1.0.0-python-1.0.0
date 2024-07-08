# This file was generated by liblab | https://liblab.com/

from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap({})
class TokenSuccessResponse(BaseModel):
    """TokenSuccessResponse

    :param token_type: Container for token response., defaults to None
    :type token_type: str, optional
    :param issued_at: Issue time of requested token., defaults to None
    :type issued_at: str, optional
    :param client_id: Client id for requested token., defaults to None
    :type client_id: str, optional
    :param access_token: Token to be used in API requests., defaults to None
    :type access_token: str, optional
    :param scope: Scope for requested token., defaults to None
    :type scope: str, optional
    :param expires_in: Expire time for requested token in seconds., defaults to None
    :type expires_in: str, optional
    :param refresh_count: Number of refreshes for requested token., defaults to None
    :type refresh_count: str, optional
    :param status: Status for requested token., defaults to None
    :type status: str, optional
    """

    def __init__(
        self,
        token_type: str = None,
        issued_at: str = None,
        client_id: str = None,
        access_token: str = None,
        scope: str = None,
        expires_in: str = None,
        refresh_count: str = None,
        status: str = None,
    ):
        if token_type is not None:
            self.token_type = token_type
        if issued_at is not None:
            self.issued_at = issued_at
        if client_id is not None:
            self.client_id = client_id
        if access_token is not None:
            self.access_token = access_token
        if scope is not None:
            self.scope = scope
        if expires_in is not None:
            self.expires_in = expires_in
        if refresh_count is not None:
            self.refresh_count = refresh_count
        if status is not None:
            self.status = status
