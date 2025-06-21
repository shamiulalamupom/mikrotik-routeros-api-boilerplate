from quart import request, jsonify

async def index():
    """
    Handle the index route.
    
    :return: JSON response with a welcome message.
    """
    return jsonify({"message": "Welcome to the Netrivy API"}), 200