import datetime
import jwt
from flask import Blueprint, request, jsonify, current_app
from werkzeug.security import check_password_hash

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

def generate_tokens(user_id):
    """Generate access and refresh JWT tokens with expiration times from environment."""
    access_exp_seconds = int(current_app.config.get('JWT_ACCESS_TOKEN_EXPIRES', 900))
    refresh_exp_seconds = int(current_app.config.get('JWT_REFRESH_TOKEN_EXPIRES', 604800))

    exp_access = int((datetime.datetime.now() + datetime.timedelta(seconds=access_exp_seconds)).timestamp() * 1000)
    access_token = jwt.encode(
        {
            'user_id': user_id,
            'exp': exp_access
        },
        current_app.config['SECRET_KEY'],
        algorithm='HS256'
    )

    exp_refresh = int((datetime.datetime.now() + datetime.timedelta(seconds=refresh_exp_seconds)).timestamp() * 1000)
    refresh_token = jwt.encode(
        {
            'user_id': user_id,
            'exp': exp_refresh
        },
        current_app.config['REFRESH_SECRET_KEY'],
        algorithm='HS256'
    )

    return access_token, refresh_token

@auth_bp.route('/login', methods=['POST'])
def login():
    """
    Login endpoint.
    Expects JSON with 'username' and 'password'. Returns access and refresh tokens on success.
    """
    try:
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')

        if not username or not password:
            return jsonify(message='Username and password required'), 400

        # Look up the user in MongoDB.
        user = current_app.mongo.db.users.find_one({"username": username})
        if user and check_password_hash(user['password_hash'], password):
            # Generate tokens using the user's unique identifier.
            # Assuming _id is used from MongoDB; convert to string if necessary.
            user_id = str(user['_id'])
            access_token, refresh_token = generate_tokens(user_id=user_id)
            return jsonify(access_token=access_token, refresh_token=refresh_token), 200
        else:
            return jsonify(message='Invalid credentials'), 401
    except Exception as e:
        current_app.logger.error(f"Error during login: {e}")
        return jsonify(message='Internal server error'), 500

@auth_bp.route('/refresh', methods=['POST'])
def refresh():
    """
    Refresh endpoint.
    Expects JSON with 'refresh_token'. Returns a new access token if the refresh token is valid.
    """
    data = request.get_json()
    refresh_token = data.get('refresh_token')
    if not refresh_token:
        return jsonify(message='Refresh token is missing'), 400

    try:
        payload = jwt.decode(
            refresh_token,
            current_app.config['REFRESH_SECRET_KEY'],
            algorithms=['HS256']
        )
        user_id = payload.get('user_id')
        # Create a new access token.
        access_token = jwt.encode(
            {
                'user_id': user_id,
                'exp': datetime.datetime.now() + datetime.timedelta(minutes=15)
            },
            current_app.config['SECRET_KEY'],
            algorithm='HS256'
        )
        return jsonify(access_token=access_token), 200
    except jwt.ExpiredSignatureError:
        return jsonify(message='Refresh token expired'), 401
    except jwt.InvalidTokenError:
        return jsonify(message='Invalid refresh token'), 401
