import tkinter as tk
from tkinter import messagebox
from src.data_loader import load_stock_data
from src.predictor import train_and_predict
from src.visualize import plot_predictions

def run_app():
    def on_submit():
        symbol = symbol_entry.get().upper()
        start = start_entry.get()
        end = end_entry.get()

        if not symbol or not start or not end:
            messagebox.showerror("Input Error", "Please fill all fields.")
            return

        data = load_stock_data(symbol, start, end)
        if data is None or data.empty:
            messagebox.showerror("Data Error", "Failed to fetch stock data.")
            return

        actual, predicted = train_and_predict(data)
        plot_predictions(actual, predicted, symbol)

    # GUI layout
    root = tk.Tk()
    root.title("📈 Stock Market Predictor")

    tk.Label(root, text="Stock Symbol:").grid(row=0, column=0, padx=10, pady=5)
    symbol_entry = tk.Entry(root)
    symbol_entry.grid(row=0, column=1)

    tk.Label(root, text="Start Date (YYYY-MM-DD):").grid(row=1, column=0, padx=10, pady=5)
    start_entry = tk.Entry(root)
    start_entry.grid(row=1, column=1)

    tk.Label(root, text="End Date (YYYY-MM-DD):").grid(row=2, column=0, padx=10, pady=5)
    end_entry = tk.Entry(root)
    end_entry.grid(row=2, column=1)

    submit_btn = tk.Button(root, text="Predict", command=on_submit)
    submit_btn.grid(row=3, column=0, columnspan=2, pady=15)

    root.mainloop()