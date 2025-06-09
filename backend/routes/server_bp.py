from flask import Blueprint, render_template, request, redirect, url_for
from ..mikrotik_client import MikroTikClient
from flask import jsonify

server_bp = Blueprint("server", __name__, url_prefix="/server")

client = MikroTikClient()

@server_bp.route("/server", methods=["POST"])
def create_pppoe_server():
    try:
        data = request.json

        # Required fields for PPPoE server interface
        pppoe_config = {
            "interface": data["interface"],         # e.g., "ether1"
            "service-name": data.get("service_name", "pppoe-service"),
            "one-session-per-host": data.get("one_session_per_host", "yes"),
            "default-profile": data.get("default_profile", "default"),
            "authentication": data.get("authentication", "pap,chap"),
        }

        resource = client.api.get_resource("/interface/pppoe-server/server")
        result = resource.add(**pppoe_config)

        return jsonify({"message": "PPPoE server interface created", "result": result}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400