import yfinance as yf

def get_stock_data(symbol):
    df = yf.download(symbol, period="6mo")
    if df.empty:
        raise ValueError("Invalid stock symbol or no data found.")
    return df