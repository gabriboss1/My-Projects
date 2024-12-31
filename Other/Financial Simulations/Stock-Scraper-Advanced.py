import yfinance as yf
import openai
import requests
from bs4 import BeautifulSoup

openai.api_key = ''

def get_stock_data(ticker):
    stock = yf.Ticker(ticker)
    hist = stock.history(period="5d")
    return hist

def get_stock_news(ticker):
    url = f"https://finance.yahoo.com/quote/{ticker}/news"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    headlines = []
    for item in soup.find_all('h3', {'class': 'Mb(5px)'}):
        headline = item.get_text(strip=True)
        headlines.append(headline)
    
    return headlines

def analyze_stock_sentiment(stock_data, headlines):
    data_summary = stock_data.to_string()

    news_summary = "\n".join(headlines)

    prompt = f"""
    Analyze the following stock data and news headlines for the company. 
    Provide a sentiment analysis of the stock based on the news and the data, 
    and conclude whether this stock is a good pick for investment.

    Stock Data:
    {data_summary}

    Recent News Headlines:
    {news_summary}
    
    Sentiment Analysis and Recommendation:
    """

    response = openai.Completion.create(
        model="gpt-4.0-mini",
        prompt=prompt,
        max_tokens=150
    )

    return response['choices'][0]['text'].strip()

if __name__ == "__main__":
    ticker = "AAPL" 
    
    stock_data = get_stock_data(ticker)
    news_headlines = get_stock_news(ticker)
    
    analysis = analyze_stock_sentiment(stock_data, news_headlines)
    print("Analysis and Recommendation:")
    print(analysis)
