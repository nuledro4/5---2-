from cls.gregorian_calendar import GregorianCalendar
import datetime


def prev_month_link(year: int, month: int) -> str:
    month, year = GregorianCalendar.prev_month_and_year(year=year, month=month)
    return f"/{year}/{month}/"


def next_month_link(year: int, month: int) -> str:
    month, year = GregorianCalendar.next_month_and_year(year=year, month=month)
    return f"/{year}/{month}/"


def previous_week_link(year: int, month: int, week: int) -> str:
    week = week - 1
    if week < 0:
        week = 4
        month, year = GregorianCalendar.prev_month_and_year(year=year, month=month)
    return f"/{year}/{month}/{week}"


def next_week_link(year: int, month: int, week: int) -> str:
    week = week + 1
    if week > 4:
        week = 0
        month, year = GregorianCalendar.next_month_and_year(year=year, month=month)
    return f"/{year}/{month}/{week}"


def prev_day_link(year: int, month: int, day: int) -> str:
    previous_day_link = datetime.date(year, month, day) - datetime.timedelta(days=1)
    return f"/{previous_day_link.year}/{previous_day_link.month}/{previous_day_link.day}"


def next_day_link(year: int, month: int, day: int) -> str:
    next_day = datetime.date(year, month, day) + datetime.timedelta(days=1)
    return f"/{next_day.year}/{next_day.month}/{next_day.day}"

