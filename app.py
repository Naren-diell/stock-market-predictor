import tkinter as tk
from tkinter import messagebox
from predictor.fetch_data import get_stock_data
from predictor.model import predict_stock_price
from utils.plot_graph import plot_prediction

def run_app():
    def on_predict():
        symbol = symbol_entry.get().upper()
        try:
            days = int(days_entry.get())
            df = get_stock_data(symbol)
            predictions, model, df = predict_stock_price(df, days)
            plot_prediction(df, predictions, symbol)
        except Exception as e:
            messagebox.showerror("Error", str(e))

    window = tk.Tk()
    window.title("Stock Market Predictor")
    window.geometry("300x200")

    tk.Label(window, text="Stock Symbol:").pack(pady=5)
    symbol_entry = tk.Entry(window)
    symbol_entry.pack()

    tk.Label(window, text="Days to Predict:").pack(pady=5)
    days_entry = tk.Entry(window)
    days_entry.pack()

    tk.Button(window, text="Predict", command=on_predict).pack(pady=15)

    window.mainloop()