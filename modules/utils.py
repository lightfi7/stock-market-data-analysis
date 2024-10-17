import csv
from datetime import datetime, timedelta


def get_date_range(start_date, end_date):
    start = datetime.strptime(start_date, "%Y-%m-%d")
    end = datetime.strptime(end_date, "%Y-%m-%d")

    date_list = []
    delta = timedelta(days=1)

    while start <= end:
        date_list.append(start.strftime("%Y-%m-%d"))
        start += delta

    return date_list


def get_mondays(start_date, end_date):

    start_date = datetime.strptime(start_date, "%Y-%m-%d")
    end_date = datetime.strptime(end_date, "%Y-%m-%d")

    while start_date.weekday() != 0:  # Monday is 0 in weekday()
        start_date += timedelta(days=1)

    mondays = []
    while start_date <= end_date:
        mondays.append(start_date.strftime("%Y-%m-%d"))
        start_date += timedelta(days=7)

    return mondays


def generate_times(start_time_str, end_time_str, step_minutes=3):
    start_time = datetime.strptime(start_time_str, "%H:%M")
    end_time = datetime.strptime(end_time_str, "%H:%M")

    times = []
    current_time = start_time
    while current_time <= end_time:
        times.append(current_time.strftime("%H:%M"))
        current_time += timedelta(minutes=step_minutes)

    return times


def calculate_offset(time1_str, time2_str):
    time1 = datetime.strptime(time1_str, "%H:%M:%S")
    time2 = datetime.strptime(time2_str, "%H:%M:%S")
    offset = (time2 - time1).total_seconds() / 60
    return offset


def write_to_csv(file_name, mondays, times):
    with open(file_name, mode='w', newline='') as file:
        writer = csv.writer(file)

        writer.writerow(["Monday", "Entry Times"])

        for monday in mondays:
            for time in times:
                writer.writerow([monday, time])
