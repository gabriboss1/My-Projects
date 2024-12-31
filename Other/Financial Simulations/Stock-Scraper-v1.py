import yfinance as yf
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def get_stock_news(stock_symbol):
    stock = yf.Ticker(stock_symbol)
    
    news = stock.news
    headlines = [item['title'] for item in news]
    
    return headlines

def analyze_sentiment(text):
    analyzer = SentimentIntensityAnalyzer()
    sentiment_score = analyzer.polarity_scores(text)
    compound_score = sentiment_score['compound'] 
    
    return compound_score 

def get_stock_sentiment(stock_symbol):
    headlines = get_stock_news(stock_symbol)
    if not headlines:
        return "No news available for this stock."
    
    combined_text = " ".join(headlines)
    sentiment_score = analyze_sentiment(combined_text)
    
    if sentiment_score > 0.1:
        sentiment_classification = "Positive"
    elif sentiment_score < -0.1:
        sentiment_classification = "Negative"
    else:
        sentiment_classification = "Neutral"
    
    return sentiment_score, sentiment_classification

stock_symbol = "AAPL"  
sentiment_score, sentiment_classification = get_stock_sentiment(stock_symbol)
print(f"The sentiment score for {stock_symbol} is: {sentiment_score:.2f}")
print(f"The overall sentiment classification for {stock_symbol} is: {sentiment_classification}")
