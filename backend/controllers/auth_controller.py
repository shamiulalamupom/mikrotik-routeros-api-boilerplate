from quart import request, jsonify
from pydantic import ValidationError
from quart_jwt_extended import get_jwt_identity

from quart_jwt_extended import create_access_token, create_refresh_token
from backend.services.auth_service import create_user, authenticate_user, check_existing_user

from backend.schemas.auth_schemas import UserLoginSchema, UserRegistrationSchema

async def register(body: UserRegistrationSchema):
    existing_user = await check_existing_user(body.username, body.email)
    if existing_user:
        return jsonify({"msg": "User with this username or email already exists"}), 409

    user = await create_user(body.username, body.password, body.email)
    access_token = create_access_token(identity=user["username"])
    refresh_token = create_refresh_token(identity=user["username"])
    return jsonify(user=user, access_token=access_token, refresh_token=refresh_token), 201

async def login(body: UserLoginSchema):
    user = await authenticate_user(body.username, body.password)
    if not user:
        return jsonify({"msg": "Bad username or password"}), 401

    access_token = create_access_token(identity=user["username"])
    refresh_token = create_refresh_token(identity=user["username"])
    return jsonify(access_token=access_token, refresh_token=refresh_token), 200

async def refresh_token():
    """
    Refresh the access token using the refresh token.
    
    :return: JSON response containing the new access token.
    """
    identity = get_jwt_identity()
    new_access_token = create_access_token(identity=identity)
    return jsonify(access_token=new_access_token), 200

