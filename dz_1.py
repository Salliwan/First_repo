from datetime import datetime, timedelta

def get_days_from_today(date):
    date_string = datetime.strptime(date, "%Y-%m-%d").date()
    now = datetime.today().date()
    difference = now - date_string
    return difference.days
