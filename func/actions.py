from flask import render_template, make_response, current_app, request
from cls.gregorian_calendar import GregorianCalendar
from func.calendar_func import prev_month_link, next_month_link


def index_page() -> make_response:
    return make_response(render_template("index.html"))


def calendar_page() -> make_response:
    calendar = calendar_month_page()
    return make_response(calendar)


def calendar_month_page(year=None, month=None) -> make_response:
    weekdays_headers = ["ПН", "ВТ", "СР", "ЧТ", "ПТ", "СБ", "ВС"]

    GregorianCalendar.setfirstweekday(current_app.config["FIRST_DAY_WEEK"])

    current_day, current_month, current_year = GregorianCalendar.current_date()
    if (year is None) and (month is None):
        year = int(request.args.get("y", current_year))
        month = int(request.args.get("m", current_month))
    else:
        year = int(year)
        month = int(month)

    month_name = GregorianCalendar.MONTH_NAMES[month - 1]
    current_month_name = GregorianCalendar.MONTH_NAMES[current_month - 1]
    month_days = GregorianCalendar.month_days(year, month)

    return make_response(
        render_template(
            "calendar_month.html",
            current_month_name=current_month_name,
            month_name=month_name,
            month=month,
            year=year,
            current_day=current_day,
            current_month=current_month,
            current_year=current_year,
            weekdays_headers=weekdays_headers,
            month_days=month_days,
            previous_month_link=prev_month_link(year, month),
            next_month_link=next_month_link(year, month)
        ),
    )


def calendar_week_page() -> make_response:
    return make_response(render_template("calendar_week.html"))


def calendar_day_page() -> make_response:
    return make_response(render_template("calendar_day.html"))
