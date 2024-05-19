from flask import render_template, make_response, current_app, request
from cls.gregorian_calendar import GregorianCalendar
from func.calendar_func import prev_month_link, next_month_link, previous_week_link, next_week_link


def index_page() -> make_response:
    return make_response(render_template("index.html"))


def calendar_page() -> make_response:
    calendar = calendar_month_page()
    return calendar


def calendar_month_page(year=None, month=None) -> make_response:
    GregorianCalendar.setfirstweekday(current_app.config["FIRST_DAY_WEEK"])

    current_day, current_month, current_year = GregorianCalendar.current_date()
    if (year is None) and (month is None):
        year = current_year
        month = current_month
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
            weekdays_headers=current_app.config["WEEK_DAYS"],
            month_days=month_days,
            previous_month_link=prev_month_link(year, month),
            next_month_link=next_month_link(year, month)
        )
    )


def calendar_week_page(year=None, month=None, week=None) -> make_response:
    GregorianCalendar.setfirstweekday(current_app.config["FIRST_DAY_WEEK"])

    current_day, current_month, current_year = GregorianCalendar.current_date()
    current_week = GregorianCalendar.num_week_in_month_by_date(current_year, current_month, current_day)
    if (year is None) and (month is None):
        year = current_year
        month = current_month
        week = current_week
    else:
        year = int(year)
        month = int(month)
        week = int(week)

    week_days = GregorianCalendar.week_days(year, month, week)

    if week_days[0].month != week_days[6].month:
        month_name = f"{GregorianCalendar.MONTH_NAMES[week_days[0].month - 1]} - {GregorianCalendar.MONTH_NAMES[week_days[6].month - 1]}"
    else:
        month_name = GregorianCalendar.MONTH_NAMES[month - 1]

    current_month_name = GregorianCalendar.MONTH_NAMES[current_month - 1]

    return make_response(render_template(
        "calendar_week.html",
        month_name=month_name,
        current_month_name=current_month_name,
        week=week,
        month=month,
        year=year,
        current_day=current_day,
        current_week=current_week,
        current_month=current_month,
        current_year=current_year,
        weekdays_headers=current_app.config["WEEK_DAYS"],
        week_days=week_days,
        previous_week_link=previous_week_link(year, month, week),
        next_month_link=next_week_link(year, month, week)
    )
    )


def calendar_day_page() -> make_response:
    return make_response(render_template("calendar_day.html"))
