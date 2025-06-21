from passlib.hash import bcrypt
from backend.models.user_model import user_collection

async def check_existing_user(username, email):
    """
    Check if a user with the given username or email already exists.
    
    :param username: The username to check.
    :param email: The email to check.
    :return: True if user exists, False otherwise.
    """
    existing_user = await user_collection.find_one({"username": username, "email": email})
    return existing_user is not None

async def create_user(username, password, email):
    """
    Create a new user in the database with hashed password.
    
    :param user_data: A dictionary containing user data.
    :return: The created user document.
    """
    hashed_password = bcrypt.hash(password)
    await user_collection.insert_one({
        "username": username,
        "password": hashed_password,
        "email": email
    })
    return {"username": username}

async def authenticate_user(username, password):
    user = await user_collection.find_one({"username": username})
    if user and bcrypt.verify(password, user["password"]):
        return user
    return None