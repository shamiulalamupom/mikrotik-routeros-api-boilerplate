from backend.models.user_model import user_collection

async def get_user_by_id(user_id: str):
    """
    Retrieve a user by their ID from the database.
    
    :param user_id: The ID of the user to retrieve.
    :return: The user document if found, otherwise None
    """
    user = await user_collection.find_one({"_id": user_id})
    return user if user else None

async def create_user(user_data: dict):
    """
    Create a new user in the database.
    
    :param user_data: A dictionary containing user data.
    :return: The created user document.
    """
    result = await user_collection.insert_one(user_data)
    return await get_user_by_id(str(result.inserted_id))

async def update_user(user_id: str, user_data: dict):
    """
    Update an existing user in the database.
    
    :param user_id: The ID of the user to update.
    :param user_data: A dictionary containing the updated user data.
    :return: The updated user document if found, otherwise None
    """
    result = await user_collection.update_one({"_id": user_id}, {"$set": user_data})
    if result.modified_count > 0:
        return await get_user_by_id(user_id)
    return None