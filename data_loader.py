import yfinance as yf

def load_data(ticker, start, end):
    return yf.download(ticker, start=start, end=end)