from quart import Blueprint
from backend.controllers.auth_controller import register, login

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/register", methods=["POST"])
async def register_route():
    return await register()

@auth_bp.route("/login", methods=["POST"])
async def login_route():
    return await login()
