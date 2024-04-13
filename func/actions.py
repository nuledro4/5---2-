from flask import render_template, make_response


def index_page() -> make_response:
    return make_response(render_template("index.html"))


def calendar_page() -> make_response:
    calendar = calendar_month_page()
    return make_response(calendar)


def calendar_month_page() -> make_response:
    return make_response(render_template("calendar_month.html"))


def calendar_week_page() -> make_response:
    return make_response(render_template("calendar_week.html"))


def calendar_day_page() -> make_response:
    return make_response(render_template("calendar_day.html"))
