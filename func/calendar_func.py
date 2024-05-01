from cls.gregorian_calendar import GregorianCalendar


def prev_month_link(year: int, month: int) -> str:
    month, year = GregorianCalendar.prev_month_and_year(year=year, month=month)
    return f"/{year}/{month}/"


def next_month_link(year: int, month: int) -> str:
    month, year = GregorianCalendar.next_month_and_year(year=year, month=month)
    return f"/{year}/{month}/"
