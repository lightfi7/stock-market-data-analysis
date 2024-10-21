import os

import matplotlib.pyplot as plt
import matplotlib.table as table
import pandas as pd
from dotenv import load_dotenv
from matplotlib.colors import LinearSegmentedColormap
load_dotenv()

from modules.bot import Bot
from modules.core import analyze
from modules.dialog import run_window
from modules.utils import get_date_range, get_days, generate_times, calculate_offset

def ready(start_date, end_date, day):
    # start_date = "2017-01-01"
    # end_date = "2017-12-31"
    # dates = get_date_range(start_date, end_date)
    dates = get_days(start_date, end_date, int(day))

    times = generate_times('9:32', '15:59')

    last = ''
    rows = []

    for date in dates:
        for time in times:
            rows.append((last, f'{date} {time}', None, None, None, None, None))
            last = f'{date} {time}'

    df = pd.DataFrame(rows, columns=['OPEN_DATETIME', 'CLOSE_DATETIME','BUY_SELL','CALL_PUT','STRIKE','EXPIRATION','QUANTITY'])
    df = df.iloc[1:]
    df.to_csv('output.csv', index=False)

def start(start_date, end_date):

    bot = Bot()
    bot.start()
    bot.run({
        'start_date': start_date,
        'end_date': end_date,
        'file':f'{os.path.expanduser("~")}/OneDrive/Documents/GitHub/stock-market-data-analysis/output.csv'
    })

    rows = analyze(f'{os.path.expanduser("~")}/Downloads/trade-log.csv')
    data = pd.DataFrame(rows, columns=['Time', 'Starting Capital', 'Ending Capital', 'Profit/Loss (P/L)', 'CAGR',
                                       'Max Drawdown', 'MAR Ratio'])

    # Define a colormap from green (positive P/L) to red (negative P/L)
    cmap = LinearSegmentedColormap.from_list("green_red", ["red", "yellow", "green"])

    # Normalize the 'P/L' values to a range from 0 to 1
    norm = plt.Normalize(data['Profit/Loss (P/L)'].min(), data['Profit/Loss (P/L)'].max())

    # Apply the colormap to 'P/L' values
    colors = cmap(norm(data['Profit/Loss (P/L)']))

    fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(19.2, 10.8), constrained_layout=True)

    ax1.bar(data['Time'], data['CAGR'] * 100, color=colors, alpha=0.8, align='center')
    ax1.set_xlabel('Time')
    ax1.set_ylabel('CAGR (%)')
    ax1.set_title('CAGR Bar Chart with Color Based on CAGR')
    ax1.set_xticklabels(data['Time'], rotation=90, ha='left', fontsize=8)

    # filter best...
    sorted_rows = sorted(rows, key=lambda x: x[3])

    tb = table.table(cellText=sorted_rows[-1:],
                        colLabels=['Time', 'Starting Capital', 'Ending Capital', 'Profit/Loss (P/L)', 'CAGR',
                                   'Max Drawdown', 'MAR Ratio'],
                        ax=ax2,
                        loc='center',
                        cellLoc='center'
                        )
    ax2.axis('off')
    ax2.set_title('Optimal Entries by Day', loc='center')
    ax2.add_table(tb)

    portfolio_values = []
    time_series = []
    for row in rows:
        portfolio_values.append(row[2])
        time_series.append(calculate_offset(rows[0][0], row[0]))

    print(time_series)
    print(portfolio_values)

    ax3.plot(time_series, portfolio_values)
    ax3.set_title('Portfolio Value Over Time')
    ax3.set_xlabel('Time')
    ax3.set_ylabel('Portfolio Value')

    plt.show()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    run_window(cb_ready=ready, cb=start)


