from src.data_loader import load_data
from src.predictor import predict
from src.visualizer import plot_predictions

# Load data
df = load_data('AAPL', start='2020-01-01', end='2024-01-01')

# Make predictions
predictions = predict(df)

# Plot results
plot_predictions(df, predictions)
