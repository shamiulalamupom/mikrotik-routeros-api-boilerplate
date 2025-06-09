from flask import Flask
from flask_pymongo import PyMongo
from flask_jwt_extended import JWTManager

mongo = PyMongo()
jwt = JWTManager()

def create_backend():
    app = Flask(__name__)
    app.config.from_object('config.MikrotikConfig')

    app.config.from_object('config.MongoConfig')
    mongo.init_app(app)

    app.config.from_object('config.JWTConfig')
    jwt.init_app(app)

    from backend.routes.index_bp import index_bp
    app.register_blueprint(index_bp)

    from backend.routes.pool_bp import pool_bp
    app.register_blueprint(pool_bp)

    from backend.routes.server_bp import server_bp
    app.register_blueprint(server_bp)

    return app
