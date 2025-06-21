from quart import jsonify, request
from backend.services.user_service import get_user_by_id, create_user, update_user

async def get_user():
    """
    Retrieve the user information based on the provided user ID in the request arguments.
    
    :return: JSON response containing user data or an error message if not found.
    """
    user_id = request.args.get('user_id')
    if not user_id:
        return jsonify({"error": "User ID is required"}), 400

    user = await get_user_by_id(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404

    return jsonify(user), 200

async def create_new_user():
    """
    Create a new user with the data provided in the request body.
    
    :return: JSON response containing the created user data or an error message.
    """
    user_data = await request.get_json()
    if not user_data:
        return jsonify({"error": "User data is required"}), 400

    try:
        new_user = await create_user(user_data)
        return jsonify(new_user), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500