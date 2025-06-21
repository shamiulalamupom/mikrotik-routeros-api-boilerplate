from quart import request, jsonify
from quart_jwt_extended import create_access_token
from backend.services.auth_service import create_user, authenticate_user

async def register():
    data = await request.get_json()
    user = await create_user(data["username"], data["password"])
    return jsonify(user), 201

async def login():
    data = await request.get_json()
    user = await authenticate_user(data["username"], data["password"])
    if not user:
        return jsonify({"msg": "Bad username or password"}), 401

    access_token = create_access_token(identity=user["username"])
    return jsonify(access_token=access_token)
