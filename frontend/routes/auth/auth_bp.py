from flask import Blueprint, render_template, request, redirect, url_for
import os

from dotenv import load_dotenv
load_dotenv()

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

from ...utils.axios_client import Axios
axios = Axios(base_url=os.getenv('BACKEND_HOST'), headers={'Content-Type': 'application/json'})
        
@auth_bp.route("/login", methods=["GET", "POST"])
def profile():
    if request.method == 'GET':
        return render_template('auth/login.html')
    elif request.method == 'POST':
        pass