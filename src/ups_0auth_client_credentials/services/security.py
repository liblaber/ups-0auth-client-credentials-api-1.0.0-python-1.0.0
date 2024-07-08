# This file was generated by liblab | https://liblab.com/

from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..models.utils.cast_models import cast_models
from ..models.token_success_response import TokenSuccessResponse
from ..models.create_token_request import CreateTokenRequest


class SecurityService(BaseService):

    @cast_models
    def create_token(
        self, request_body: CreateTokenRequest, x_merchant_id: str = None
    ) -> TokenSuccessResponse:
        """create_token

        :param request_body: The request body.
        :type request_body: CreateTokenRequest
        :param x_merchant_id: 6-digit UPS account number., defaults to None
        :type x_merchant_id: str, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: successful operation
        :rtype: TokenSuccessResponse
        """

        Validator(CreateTokenRequest).validate(request_body)
        Validator(str).is_optional().validate(x_merchant_id)

        serialized_request = (
            Serializer(
                f"{self.base_url}/security/v1/oauth/token", self.get_default_headers()
            )
            .add_header("x-merchant-id", x_merchant_id)
            .serialize()
            .set_method("POST")
            .set_body(request_body, "application/x-www-form-urlencoded")
        )

        response = self.send_request(serialized_request)

        return TokenSuccessResponse._unmap(response)