import matplotlib.pyplot as plt

def plot_predictions(df, predictions):
    plt.plot(df['Close'], label='Historical')
    plt.plot(range(len(df), len(df)+len(predictions)), predictions, label='Predicted')
    plt.legend()
    plt.title('Stock Price Prediction')
    plt.show()