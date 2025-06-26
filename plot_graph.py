import matplotlib.pyplot as plt
import numpy as np

def plot_prediction(df, predictions, symbol):
    future_days = list(range(len(df), len(df) + len(predictions)))
    plt.figure(figsize=(10, 5))
    plt.plot(df['Close'], label='Actual Prices')
    plt.plot(future_days, predictions, label='Predicted Prices', linestyle='--')
    plt.title(f"{symbol} Price Prediction")
    plt.xlabel("Days")
    plt.ylabel("Price")
    plt.legend()
    plt.grid()
    plt.show()