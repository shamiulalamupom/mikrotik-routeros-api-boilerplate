from quart import Blueprint
from quart_jwt_extended import jwt_required

from backend.controllers import index_controller

index_bp = Blueprint("index", __name__)
@index_bp.route("/", methods=["GET"])
@jwt_required
async def index():
    """
    Handle the index route.
    
    :return: JSON response with a welcome message.
    """
    return await index_controller.index()