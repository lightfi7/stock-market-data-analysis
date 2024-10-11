import os
import time

from dotenv import load_dotenv
from modules.utils import get_date_range, get_mondays
load_dotenv()

import modules.bot

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    start_date = "2023-10-01"
    end_date = "2024-10-11"
    dates = get_date_range(start_date, end_date)
    mondays = get_mondays(start_date, end_date)
    print(dates)
    print(mondays)
    while True:
        time.sleep(1000)
