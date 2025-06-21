from quart import Blueprint
from quart_jwt_extended import verify_jwt_refresh_token_in_request

from ..utils.validation import validate_body
from backend.schemas.auth_schemas import UserLoginSchema, UserRegistrationSchema

from backend.controllers.auth_controller import register, login
from backend.controllers.auth_controller import refresh_token

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/register", methods=["POST"])
@validate_body(UserRegistrationSchema)
async def register_route(body):
    return await register(body)

@auth_bp.route("/login", methods=["POST"])
@validate_body(UserLoginSchema)
async def login_route(body):
    return await login(body)

@auth_bp.route("/refresh", methods=["POST"])
async def refresh_token_route():
    """
    Refresh the access token using the refresh token.
    
    :return: JSON response containing the new access token.
    """
    await verify_jwt_refresh_token_in_request()
    return await refresh_token()
