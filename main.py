from dotenv import load_dotenv
from modules.utils import get_date_range, get_mondays, generate_times
import pandas as pd

load_dotenv()

import modules.bot

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    start_date = "2017-01-01"
    end_date = "2017-12-19"
    dates = get_date_range(start_date, end_date)
    mondays = get_mondays(start_date, end_date)

    times = generate_times('9:32', '15:59')

    last = ''
    rows = []

    for date in dates:
        for time in times:
            rows.append((last, f'{date} {time}'))
            last = f'{date} {time}'

    df = pd.DataFrame(rows, columns=['OPEN_DATETIME', 'CLOSE_DATETIME'])
    df = df.iloc[1:]
    df.to_csv('output.csv', index=False)

    bot = modules.bot.Bot()
    bot.start()
    bot.run({
        'file':'C:/Users/Fi/Documents/GitHub/stock-market-data-analysis/output.csv'
    })
