from sklearn.linear_model import LinearRegression
import numpy as np

def predict_stock_price(df, days):
    df = df[['Close']].copy()
    df['Prediction'] = df['Close'].shift(-days)
    X = np.array(df.drop(['Prediction'], axis=1))[:-days]
    y = np.array(df['Prediction'])[:-days]

    model = LinearRegression()
    model.fit(X, y)

    X_future = df.drop(['Prediction'], axis=1)[-days:]
    prediction = model.predict(X_future)
    return prediction, model, df