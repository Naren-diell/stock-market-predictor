import matplotlib.pyplot as plt

def plot_predictions(df, predictions):
    plt.figure(figsize=(12, 6))
    plt.plot(df['Close'].values, label='Historical')
    future_x = range(len(df), len(df) + len(predictions))
    plt.plot(future_x, predictions, label='Predicted')
    plt.xlabel('Time')
    plt.ylabel('Price')
    plt.title('Stock Price Prediction')
    plt.legend()
    plt.show()
