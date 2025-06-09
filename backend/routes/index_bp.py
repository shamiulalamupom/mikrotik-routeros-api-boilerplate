from flask import Blueprint, render_template, request, redirect, url_for
from ..mikrotik_client import MikroTikClient
from flask import jsonify

index_bp = Blueprint('index', __name__)

client = MikroTikClient()

@index_bp.route('/add-ip', methods=['POST'])
def add_ip():
    address = request.form.get('address')
    interface = request.form.get('interface')
    client.add_ip_address(address, interface)
    client.close()
    return redirect(url_for('main.dashboard'))