from cls.gregorian_calendar import GregorianCalendar


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
