from flask import Flask

def create_frontend():
    app = Flask(__name__)

    from .routes.index_bp import main
    app.register_blueprint(main)

    from .routes.auth.auth_bp import auth_bp
    app.register_blueprint(auth_bp)

    from .routes.pool_bp import pool_bp
    app.register_blueprint(pool_bp)

    return app
