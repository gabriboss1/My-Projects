import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf
import requests
from textblob import TextBlob
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, Dense, LSTM, concatenate
from sklearn.preprocessing import MinMaxScaler
from tqdm import tqdm

def fetch_stock_data(stock_symbol):
    data = yf.download(stock_symbol, start='2015-01-01', end='2024-01-01')
    return data[['Close']]

def fetch_real_time_news(api_key, query, num_articles=10):
    url = f"https://newsapi.org/v2/everything?q={query}&apiKey={api_key}&pageSize={num_articles}"
    response = requests.get(url).json()
    articles = response['articles']
    
    sentiments = []
    for article in articles:
        analysis = TextBlob(article['description'] or article['content'])
        sentiments.append(analysis.sentiment.polarity)
    return sum(sentiments) / len(sentiments) if sentiments else 0

def create_sequences(data, seq_length):
    x, y = [], []
    for i in range(len(data) - seq_length):
        x.append(data[i:i + seq_length])
        y.append(data[i + seq_length])
    return np.array(x), np.array(y)

def create_features(stock_data, sentiment_series):
    stock_data['Sentiment'] = sentiment_series
    return stock_data

def build_model(input_shape):
    stock_input = Input(shape=(input_shape, 1))
    x = LSTM(50, return_sequences=True)(stock_input)
    x = LSTM(50)(x)
    
    sentiment_input = Input(shape=(1,))
    y = Dense(10, activation='relu')(sentiment_input)
    
    combined = concatenate([x, y])
    z = Dense(25, activation='relu')(combined)
    z = Dense(1)(z)
    
    model = Model(inputs=[stock_input, sentiment_input], outputs=z)
    model.compile(optimizer='adam', loss='mean_squared_error')
    return model

if __name__ == '__main__':
    stock_symbol = input("Enter the stock symbol (e.g., AAPL): ")
    api_key = '70cbaefc560e4319a179c3722ba381a4'
    data = fetch_stock_data(stock_symbol)
    
    sentiment_series = []
    print("Fetching news sentiment...")
    for i in tqdm(range(len(data))):
        sentiment = fetch_real_time_news(api_key, stock_symbol)
        sentiment_series.append(sentiment)
    
    sentiment_series = np.array(sentiment_series)
    
    scaler = MinMaxScaler(feature_range=(0, 1))
    stock_data_normalized = scaler.fit_transform(data[['Close']].values)
    
    stock_data = create_features(data, sentiment_series)
    
    sequence_length = 60
    stock_sequences, stock_targets = create_sequences(stock_data_normalized, sequence_length)
    
    sentiment_data = sentiment_series[sequence_length:]
    
    x_train_stock = stock_sequences[:-365]
    x_train_sentiment = sentiment_data[:-365]
    y_train = stock_targets[:-365]
    
    model = build_model(x_train_stock.shape[1])
    print("Training the model...")
    model.fit([x_train_stock, x_train_sentiment], y_train, epochs=10, batch_size=32, verbose=0)
    
    future_sentiments = [fetch_real_time_news(api_key, stock_symbol)] * 365
    future_stock_input = stock_sequences[-365:]
    
    predictions = []
    for _ in tqdm(range(365), desc="Making predictions"):
        prediction = model.predict([future_stock_input, np.array(future_sentiments)])
        predictions.append(prediction)
    
    predicted_prices = scaler.inverse_transform(np.array(predictions).reshape(-1, 1))
    
    future_dates = pd.date_range(data.index[-1], periods=365 + 1, freq='D')[1:]
    
    predicted_prices = predicted_prices[:len(future_dates)]
    
    plt.figure(figsize=(10, 6))
    plt.plot(data.index, data['Close'], label="Historical Prices")
    plt.plot(future_dates, predicted_prices.flatten(), label="Future Predictions", color='orange')
    plt.title(f"{stock_symbol} Stock Price Prediction")
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.legend()
    plt.show()
