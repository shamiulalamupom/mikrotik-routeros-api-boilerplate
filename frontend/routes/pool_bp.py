from flask import Blueprint, render_template, request, redirect, url_for
import os

from dotenv import load_dotenv
load_dotenv()

pool_bp = Blueprint('pools', __name__, url_prefix='/pools')

from ..utils.axios_client import Axios
axios = Axios(base_url=os.getenv('BACKEND_HOST'), headers={'Content-Type': 'application/json'})

@pool_bp.route('/', methods=['GET', 'POST'])
def pools():
    pools = axios.get('/ppp/ip-pools').json()
    if request.method == 'GET':
        return render_template('pool/pools.html', pools=pools)
    elif request.method == 'POST':
        data = request.form.to_dict()
        response = axios.post('/ppp/ip-pool', json=data)
        if response.status_code == 201:
            pools = axios.get('/ppp/ip-pools').json()
            return redirect(url_for('pool_bp.pools', pools=pools))
        else:
            return render_template('pool/ip_pool.html', error=response.json().get('error', 'Unknown error'))