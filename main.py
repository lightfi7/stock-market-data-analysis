from dotenv import load_dotenv
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.table as table
import numpy as np

from modules.core import analyze
from modules.utils import get_date_range, get_mondays, generate_times

load_dotenv()

import modules.bot

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    start_date = "2017-01-01"
    end_date = "2017-12-31"
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

    rows = analyze('C:/Users/Fi/Downloads/trade-log.csv')
    data = pd.DataFrame(rows, columns=['Group', 'Starting Capital', 'Ending Capital', 'Profit/Loss (P/L)', 'CAGR',
                                       'Max Drawdown', 'MAR Ratio'])

    cmap = plt.get_cmap('viridis')
    fig, ax = plt.subplots(figsize=(100, 60))
    ax.axis('off')

    colors = [cmap(i) for i in np.linspace(0, 1, len(data))]

    ax = fig.add_axes([0.2, 0.4, 0.6, 0.4])
    ax.bar(data['Group'], data['CAGR'] * 100, color=colors, alpha=0.8, align='center')
    ax.set_xlabel('Group')
    ax.set_ylabel('CAGR (%)')
    ax.set_title('CAGR Bar Chart with Color Based on CAGR')

    ax2 = fig.add_axes([0.2, 0.3, 0.6, 0.3])
    table = table.table(cellText=rows,
                        colLabels=['Group', 'Starting Capital', 'Ending Capital', 'Profit/Loss (P/L)', 'CAGR',
                                   'Max Drawdown', 'MAR Ratio'],
                        ax=ax2,
                        cellLoc='center'
                        )

    ax2.axis('off')
    ax2.add_table(table)
    plt.show()
