from datetime import datetime, timedelta


def get_date_range(start_date, end_date):
    # Convert string dates to datetime objects
    start = datetime.strptime(start_date, "%Y-%m-%d")
    end = datetime.strptime(end_date, "%Y-%m-%d")

    # Generate list of dates
    date_list = []
    delta = timedelta(days=1)

    while start <= end:
        date_list.append(start.strftime("%Y-%m-%d"))
        start += delta

    return date_list

def get_mondays(start_date, end_date):
    # Start from January 1st of the start year
    start_date = datetime.strptime(start_date, "%Y-%m-%d")
    # End on December 31st of the end year
    end_date = datetime.strptime(end_date, "%Y-%m-%d")

    # Find the first Monday in the date range
    while start_date.weekday() != 0:  # Monday is 0 in weekday()
        start_date += timedelta(days=1)

    # Generate all Mondays
    mondays = []
    while start_date <= end_date:
        mondays.append(start_date.strftime("%Y-%m-%d"))
        start_date += timedelta(days=7)

    return mondays
