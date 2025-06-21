from quart import Blueprint
from backend.controllers import user_controller

user_bp = Blueprint("users", __name__)

@user_bp.route("/<user_id>")
async def get_user(user_id):
    return await user_controller.get_user(user_id)

@user_bp.route("/", methods=["POST"])
async def create_user():
    return await user_controller.create_user()
