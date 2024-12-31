import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout

stock_symbol = input("Enter the stock symbol (e.g., AAPL): ")
data = yf.download(stock_symbol, start='2015-01-01', end='2024-01-01')
data = data[['Close']]

scaler = MinMaxScaler(feature_range=(0, 1))
scaled_data = scaler.fit_transform(data)

train_size = int(len(scaled_data) * 0.8)
train_data = scaled_data[:train_size]
test_data = scaled_data[train_size:]

def create_sequences(data, seq_length):
    x, y = [], []
    for i in range(len(data) - seq_length):
        x.append(data[i:i + seq_length])
        y.append(data[i + seq_length])
    return np.array(x), np.array(y)

sequence_length = 60
x_train, y_train = create_sequences(train_data, sequence_length)
x_test, y_test = create_sequences(test_data, sequence_length)

x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1], 1))
x_test = np.reshape(x_test, (x_test.shape[0], x_test.shape[1], 1))

model = Sequential([
    LSTM(50, return_sequences=True, input_shape=(x_train.shape[1], 1)),
    Dropout(0.2),
    LSTM(50, return_sequences=False),
    Dropout(0.2),
    Dense(25),
    Dense(1)
])

model.compile(optimizer='adam', loss='mean_squared_error')
model.fit(x_train, y_train, batch_size=32, epochs=10)

future_days = 365
last_sequence = scaled_data[-sequence_length:]
predicted_prices = []

for _ in range(future_days):
    x_input = np.reshape(last_sequence, (1, sequence_length, 1))
    predicted_price = model.predict(x_input, verbose=0)
    predicted_prices.append(predicted_price[0][0])
    last_sequence = np.append(last_sequence[1:], predicted_price, axis=0)

predicted_prices = scaler.inverse_transform(np.array(predicted_prices).reshape(-1, 1))

future_dates = pd.date_range(data.index[-1], periods=future_days + 1, freq='D')[1:]

plt.figure(figsize=(10, 6))
plt.plot(data.index, data['Close'], label="Historical Prices")
plt.plot(future_dates, predicted_prices, label="Future Predictions")
plt.title(f"{stock_symbol} Stock Price Prediction")
plt.xlabel("Date")
plt.ylabel("Price")
plt.legend()
plt.show()
