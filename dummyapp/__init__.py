from flask import Flask

import config

API_PREFIX = "api/v1"


def create_app(config_name: str):
    app_obj = Flask(__name__)

    # apply custom configuration
    print(f"loading config '{config_name}'")
    cfg = config.configs[config_name]
    cfg.custom_init_app(app_obj)

    # load the routes
    from .routes import route_blueprint

    app_obj.register_blueprint(route_blueprint)

    from .rest_api import rest_blueprint

    app_obj.register_blueprint(rest_blueprint)

    # return the final object
    return app_obj
