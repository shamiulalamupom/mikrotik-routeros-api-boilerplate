from quart import Quart
from quart_jwt_extended import JWTManager

from backend.routes.index_route import index_bp
from backend.routes.auth_routes import auth_bp

from dotenv import load_dotenv

jwt = JWTManager()

def create_backend():
    load_dotenv()
    app = Quart(__name__)
    app.config.from_object('config.MikrotikConfig')
    app.config.from_object('config.JWTConfig')

    jwt.init_app(app)

    # from backend.routes.auth.auth_bp import auth_bp
    # app.register_blueprint(auth_bp)

    app.register_blueprint(index_bp)
    app.register_blueprint(auth_bp, url_prefix='/auth')

    # from backend.routes.pool_bp import pool_bp
    # app.register_blueprint(pool_bp)

    # from backend.routes.server_bp import server_bp
    # app.register_blueprint(server_bp)

    return app
