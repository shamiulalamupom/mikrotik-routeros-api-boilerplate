from flask import jsonify
from http import HTTPStatus
import traceback

def handle_request(service_func, payload=None, *args, success_status=HTTPStatus.OK, **kwargs):
    try:
        result = service_func(payload, *args, **kwargs)
        return jsonify({
            "success": True,
            "data": result
        }), success_status
    except Exception as e:
        print(traceback.format_exc())  # Optional: log error

        status_code = getattr(e, 'code', HTTPStatus.BAD_REQUEST)
        return jsonify({
            "success": False,
            "error": str(e)
        }), status_code
