import datetime as dt
import sys

import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from pandas_datareader import data as pdr

WINDOW = 5          # look‑back days for features
PERIOD_YEARS = 2    # history length to download

def fetch_series(ticker: str) -> pd.Series:
    """Download daily Close prices from Stooq and return ascending series."""
    end = dt.datetime.now()
    start = end - dt.timedelta(days=365 * PERIOD_YEARS)
    df = pdr.DataReader(ticker, "stooq", start, end)
    # Stooq gives newest first → flip
    return df["Close"].sort_index().dropna()

def make_xy(series: pd.Series, window: int = WINDOW):
    X, y = [], []
    vals = series.values
    for i in range(window, len(vals)):
        X.append(vals[i - window : i])
        y.append(vals[i])
    return np.asarray(X), np.asarray(y)

def main():
    try:
        ticker = input("Enter stock ticker (e.g. AAPL): ").strip().upper() or "AAPL"
    except KeyboardInterrupt:
        sys.exit()

    print(f"\n📥  Downloading {ticker} …\n", flush=True)
    try:
        series = fetch_series(ticker)
    except Exception as e:
        print("⚠️  Download failed:", e)
        print("→ Switching to demo data so you can still see the prediction.\n")
        series = pd.Series(
            [100, 101, 102, 101, 100, 99, 100, 102, 103, 104],
            index=pd.date_range(end=dt.datetime.now(), periods=10),
            name="Close",
        )

    if len(series) <= WINDOW:
        print("Not enough data to train.")
        sys.exit(1)

    X, y = make_xy(series)
    model = LinearRegression().fit(X, y)

    next_close = model.predict([series.values[-WINDOW:]])[0]
    last_close = series.iloc[-1]
    change_pct = (next_close - last_close) / last_close * 100

    print(f"Last close  ({series.index[-1].date()}): {last_close:.2f}")
    print(f"Predicted next close        : {next_close:.2f} ({change_pct:+.2f}%)")

if __name__ == "__main__":
    main()
