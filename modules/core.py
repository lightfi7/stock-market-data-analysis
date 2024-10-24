import pandas as pd


def analyze(path):

    # Load data from CSV (or raw string)
    df = pd.read_csv(path)
    df = df.groupby('Time Opened')

    rows = []

    for group in df.groups:
        data = pd.DataFrame(df.get_group(group))

        # Ensure proper data types
        data['Date Opened'] = pd.to_datetime(data['Date Opened'])
        data['Date Closed'] = pd.to_datetime(data['Date Closed'])
        data['Funds at Close'] = data['Funds at Close'].astype(float)

        # Starting Capital (fixed to $100,000)
        starting_capital = 100000.00

        # Ending Capital (last trade)
        ending_capital = data['Funds at Close'].iloc[0]

        # Profit/Loss (P/L)
        pl = ending_capital - starting_capital

        # Calculate number of years (for CAGR)
        days = (data['Date Closed'].max() - data['Date Opened'].min()).days
        years = days / 365.25

        # CAGR Calculation
        cagr = (ending_capital / starting_capital) ** (1 / years) - 1

        # Calculate Max Drawdown
        data['Peak Capital'] = data['Funds at Close'].cummax()  # Track running peak

        data['Drawdown'] = (data['Funds at Close'] - data['Peak Capital']) / data['Peak Capital']  # Drawdown %
        max_drawdown = data['Drawdown'].min()  # Max drawdown is the most negative value

        # MAR Ratio (CAGR / Max Drawdown)
        mar_ratio = cagr / abs(max_drawdown) if max_drawdown != 0 else float('inf')

        # Display results
        # print(f"Group: {data['Time Opened'].iloc[0]}")
        # print(f"Starting Capital: ${starting_capital:.2f}")
        # print(f"Ending Capital: ${ending_capital:.2f}")
        # print(f"Profit/Loss (P/L): ${pl:.2f}")
        # print(f"CAGR: {cagr:.2%}")
        # print(f"Max Drawdown: {max_drawdown:.2%}")
        # print(f"MAR Ratio: {mar_ratio:.2f}")

        rows.append((group, starting_capital, ending_capital, pl, cagr*100, max_drawdown*100, mar_ratio*100 ))

    return rows