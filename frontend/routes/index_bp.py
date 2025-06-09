from flask import Blueprint, render_template, request, redirect, url_for
import os

from dotenv import load_dotenv
load_dotenv()

main = Blueprint('main', __name__)

from ..utils.axios_client import Axios
axios = Axios(base_url=os.getenv('BACKEND_HOST'), headers={'Content-Type': 'application/json'})
        
@main.route("/profile", methods=["GET", "POST"])
def profile():
    profiles = axios.get('/ppp/profiles').json()
    if request.method == 'GET':
        return render_template('profile/profiles.html', profiles=profiles)
    elif request.method == 'POST':
        data = request.form.to_dict()
        response = axios.post('/ppp/profile', json=data)
        if response.status_code == 201:
            profiles = axios.get('/ppp/profiles').json()
            return redirect(url_for('main.profile', profiles=profiles))
        else:
            return render_template('profile/profile.html', error=response.json().get('error', 'Unknown error'))