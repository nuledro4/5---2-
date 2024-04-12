from flask import Flask
from typing import Dict, Optional
from func.actions import test_action, index_page


def create_app(config_overrides: Optional[Dict] = None) -> Flask:
    app = Flask(__name__)

    app.config.from_object("config")
    if config_overrides is not None:
        app.config.from_mapping(config_overrides)

    app.add_url_rule("/", "index_page", index_page)
    app.add_url_rule("/test", "test_action", test_action)

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=app.config["DEBUG"], host=app.config["HOST_IP"])

