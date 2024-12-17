from flask import Flask, render_template, request, jsonify
import yfinance as yf

app = Flask(__name__)

def get_stock_price(symbol):
    try:
        stock = yf.Ticker(symbol)
        data = stock.history(period="1d", interval="1m")
        if data.empty:
            return None
        latest_price = data["Close"].iloc[-1]
        return latest_price
    except Exception as e:
        print(f"Error fetching stock price: {e}")
        return None

def get_stock_chart_data(symbol, timeframe):
    try:
        timeframe_map = {
            "1d": "1d",
            "5d": "5d",
            "1mo": "1mo",
            "3mo": "3mo",
            "1y": "1y",
            "5y": "5y"
        }
        period = timeframe_map.get(timeframe, "1d")
        
        stock = yf.Ticker(symbol)
        data = stock.history(period=period)
        
        if data.empty:
            return None
        chart_data = [
            {"date": str(date.date()), "close": row["Close"]} for date, row in data.iterrows()
        ]
        return chart_data
    except Exception as e:
        print(f"Error fetching chart data: {e}")
        return None

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get_price", methods=["POST"])
def get_price():
    symbol = request.form.get("symbol")
    price = get_stock_price(symbol)
    if price is not None:
        return jsonify({"symbol": symbol, "price": f"${price:.2f}"})
    else:
        return jsonify({"error": "Failed to fetch stock price. Check the symbol or API limits."}), 400

@app.route("/get_chart", methods=["POST"])
def get_chart():
    symbol = request.form.get("symbol")
    timeframe = request.form.get("timeframe")
    chart_data = get_stock_chart_data(symbol, timeframe)
    if chart_data is not None:
        return jsonify(chart_data)
    else:
        return jsonify({"error": "Failed to fetch chart data. Check the symbol or API limits."}), 400

if __name__ == "__main__":
    app.run(debug=True)
