from functools import wraps
from quart import request, jsonify
from pydantic import BaseModel, ValidationError

def validate_body(schema: type[BaseModel]):
    def decorator(func):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            try:
                body = await request.get_json()
                validated_data = schema(**body)
            except ValidationError as e:
                return jsonify({"errors": e.errors()}), 422
            return await func(*args, **kwargs, body=validated_data)
        return wrapper
    return decorator
