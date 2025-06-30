import yfinance as yf
from src.predictor import predict
from src.visualizer import plot_predictions

df = yf.download('AAPL', start='2020-01-01', end='2024-01-01')
predictions = predict(df)
plot_predictions(df, predictions)