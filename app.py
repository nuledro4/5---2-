from flask import Flask
from typing import Dict, Optional
from func.actions import index_page, calendar_page, calendar_month_page, calendar_week_page, calendar_day_page


def create_app(config_overrides: Optional[Dict] = None) -> Flask:
    app = Flask(__name__)

    app.config.from_object("config")
    if config_overrides is not None:
        app.config.from_mapping(config_overrides)

    app.add_url_rule("/", "index_page", index_page)
    app.add_url_rule("/calendar/", "calendar_page", calendar_page)
    app.add_url_rule("/calendar/month/", "calendar_month_page", calendar_month_page)
    app.add_url_rule("/calendar/month/<year>/<month>/", "calendar_month_page", calendar_month_page)
    app.add_url_rule("/calendar/week/", "calendar_week_page", calendar_week_page)
    app.add_url_rule("/calendar/week/<year>/<month>/<week>/", "calendar_week_page", calendar_week_page)
    app.add_url_rule("/calendar/day/", "calendar_day_page", calendar_day_page)

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=app.config["DEBUG"],
            host=app.config["HOST_IP"],
            port=app.config["PORT"])
