from flask import Flask, render_template, request, jsonify
import requests

API_KEY = ''
BASE_URL = 'https://www.alphavantage.co/query'

app = Flask(__name__)

def get_stock_price(symbol):
    params = {
        'function': 'TIME_SERIES_INTRADAY',
        'symbol': symbol,
        'interval': '1min',
        'apikey': API_KEY
    }
    try:
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()
        data = response.json()
        time_series = data.get("Time Series (1min)")
        if not time_series:
            return None
        latest_time = sorted(time_series.keys())[0]
        latest_price = time_series[latest_time]["4. close"]
        return float(latest_price)
    except Exception as e:
        return None

def get_stock_chart_data(symbol):
    params = {
        'function': 'TIME_SERIES_DAILY',
        'symbol': symbol,
        'apikey': API_KEY
    }
    try:
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()
        data = response.json()
        time_series = data.get("Time Series (Daily)")
        if not time_series:
            return None
        chart_data = []
        for date, metrics in sorted(time_series.items(), reverse=True):
            chart_data.append({"date": date, "close": float(metrics["4. close"])})
        return chart_data
    except Exception as e:
        return None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_price', methods=['POST'])
def get_price():
    symbol = request.form.get('symbol')
    price = get_stock_price(symbol)
    if price is not None:
        return jsonify({"symbol": symbol, "price": f"${price:.2f}"})
    else:
        return jsonify({"error": "Failed to fetch stock price. Check the symbol or API limits."}), 400

@app.route('/get_chart', methods=['POST'])
def get_chart():
    symbol = request.form.get('symbol')
    chart_data = get_stock_chart_data(symbol)
    if chart_data is not None:
        return jsonify(chart_data)
    else:
        return jsonify({"error": "Failed to fetch chart data. Check the symbol or API limits."}), 400

if __name__ == "__main__":
    app.run(debug=True)
