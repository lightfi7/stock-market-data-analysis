import os
import tkinter as tk
from threading import Thread
from tkinter import Toplevel

import matplotlib.pyplot as plt
import matplotlib.table as table
import pandas as pd
from dotenv import load_dotenv
from matplotlib.backends._backend_tk import NavigationToolbar2Tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.colors import LinearSegmentedColormap
from matplotlib.figure import Figure

load_dotenv()

from modules.bot import Bot
from modules.core import analyze
from modules.dialog import run_window
from modules.utils import get_date_range, get_days, generate_times, calculate_offset

def ready(start_date, end_date, day, period, is_period):
    # start_date = "2017-01-01"
    # end_date = "2017-12-31"
    # dates = get_date_range(start_date, end_date)
    dates = get_days(start_date, end_date, int(day))

    times = generate_times('9:32', '15:59', step_minutes=int(period) if is_period else 3)

    last = ''
    rows = []

    for date in dates:
        for time in times:
            rows.append((last, f'{date} {time}', None, None, None, None, None))
            last = f'{date} {time}'

    df = pd.DataFrame(rows, columns=['OPEN_DATETIME', 'CLOSE_DATETIME','BUY_SELL','CALL_PUT','STRIKE','EXPIRATION','QUANTITY'])
    df = df.iloc[1:]
    df.to_csv(f'{os.path.dirname(os.path.abspath(__file__))}/output.csv', index=False)

def bot_thread(start_date, end_date, is_period,  root):
    bot = Bot()
    bot.start()
    bot.run({
        'start_date': start_date,
        'end_date': end_date,
        'is_period': is_period,
        'file': f'{os.path.dirname(os.path.abspath(__file__))}/output.csv'
    })

    # root = tk.Tk()
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
    dialog=Toplevel(root)
    canvas = FigureCanvasTkAgg(fig, master=dialog)
    canvas.draw()
    toolbar = NavigationToolbar2Tk(canvas, dialog, pack_toolbar=False)
    toolbar.update()
    toolbar.pack(side=tk.BOTTOM, fill=tk.X)
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    ax1.bar(data['Time'], data['CAGR'], color=colors, alpha=0.8, align='center')
    ax1.set_xlabel('Time')
    ax1.set_ylabel('CAGR (%)')
    ax1.set_title(f'SPX\nCAGR Bar Chart with Color Based on CAGR\n{start_date}-{end_date}')
    ax1.set_xticklabels(data['Time'], rotation=90, ha='left', fontsize=8)

    # filter best...
    sorted_rows = sorted(rows, key=lambda x: x[3])
    sorted_row = sorted_rows[-1:][0]
    v1=f'${sorted_row[1]}'
    v2=f'${sorted_row[2]}'
    v3=f'${sorted_row[3]}'
    v4=f'{sorted_row[4]:.2f}%'
    v5=f'{sorted_row[5]:.2f}%'
    v6=f'{sorted_row[6]:.2f}%'

    tb = table.table(cellText=[[sorted_row[0], v1, v2, v3, v4, v5, v6]],
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

    ax3.plot(time_series, portfolio_values)
    ax3.set_title('Portfolio Value Over Time')
    ax3.set_xlabel('Time')
    ax3.set_ylabel('Portfolio Value')
    # root.mainloop()
    pass

def start(start_date, end_date, is_period, root):
    if os.path.exists(f'{os.path.expanduser("~")}/Downloads/trade-log.csv'):
        os.remove(f'{os.path.expanduser("~")}/Downloads/trade-log.csv')
    thread = Thread(target=bot_thread, args=(start_date, end_date, is_period, root))
    thread.start()



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    run_window(cb_ready=ready, cb=start)




