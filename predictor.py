import numpy as np

def predict(df):
    last_close = df['Close'].iloc[-1]
    predictions = np.full(30, last_close)
    return predictions