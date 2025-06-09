from flask import Blueprint, render_template, request, redirect, url_for
from ..mikrotik_client import MikroTikClient
from flask import jsonify

pool_bp = Blueprint("ppp", __name__, url_prefix="/ppp")

client = MikroTikClient()


    
@pool_bp.route("/user", methods=["POST"])
def create_pppoe_user():
    try:
        data = request.json
        user = {
            "name": data["username"],
            "password": data["password"],
            "service": "pppoe",
            "profile": data.get("profile", "default"),
        }

        resource = client.api.get_resource("/ppp/secret")
        result = resource.add(**user)

        return jsonify({"message": "PPPoE user created", "result": result}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    
@pool_bp.route("/profile", methods=["POST"])
def create_pppoe_profile():
    try:
        data = request.json

        profile_data = {
            "name": data["name"],  # required
            "local-address": data.get("local_address", "192.168.88.1"),
            "remote-address": data.get("remote_address", "pppoe-pool"),
            "dns-server": data.get("dns_server", "8.8.8.8"),
            "rate-limit": data.get("rate_limit"),  # e.g., "2M/2M"
            "only-one": data.get("only_one", "yes"),
        }

        # Remove keys with None values (optional fields)
        clean_profile_data = {key: value for key, value in profile_data.items() if value is not None}

        profile_resource = client.api.get_resource("/ppp/profile")
        result = profile_resource.add(**clean_profile_data)

        return jsonify({"message": "PPP profile created", "result": result}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    
@pool_bp.route("/profiles", methods=["GET"])
def get_pppoe_profiles():
    try:
        profile_resource = client.api.get_resource("/ppp/profile")
        profiles = profile_resource.get()
        return jsonify(profiles), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@pool_bp.route("/ip-pool", methods=["POST"])
def create_ip_pool():
    try:
        data = request.json

        pool_data = {
            "name": data["name"],               # e.g., "pppoe-pool"
            "ranges": data["ranges"],           # e.g., "192.168.77.10-192.168.77.100"
        }

        pool_resource = client.api.get_resource("/ip/pool")
        result = pool_resource.add(**pool_data)

        return jsonify({"message": "IP pool created", "result": result}), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 400

@pool_bp.route("/ip-pools", methods=["GET"])
def get_ip_pools():
    try:
        pool_resource = client.api.get_resource("/ip/pool")
        pools = pool_resource.get()
        return jsonify(pools), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@pool_bp.route("/ip-pool/id/<string:pool_id>", methods=["DELETE"])
def delete_ip_pool_by_id(pool_id):
    try:
        pool_resource = client.api.get_resource("/ip/pool")
        pool_resource.remove(id=f"*{pool_id}")
        return jsonify({"message": f"Pool with ID '{pool_id}' deleted successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
