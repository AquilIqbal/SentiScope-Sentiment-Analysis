from flask import Flask

from app.extensions import db


def create_app(config_object=None):
    app = Flask(__name__, instance_relative_config=True)

    if isinstance(config_object, str):
        app.config.from_object(config_object)
    elif config_object is not None:
        app.config.from_object(config_object)
    else:
        app.config.from_object("config.DevelopmentConfig")

    db.init_app(app)

    from app.blueprints.main.routes import main_bp
    from app.blueprints.analysis.routes import analysis_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(analysis_bp)

    return app
