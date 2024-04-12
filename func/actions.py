from flask import render_template, make_response


def index_page() -> make_response:
    return make_response(render_template("index.html"))


def test_action() -> make_response:
    return make_response(render_template("test.html"))
