import requests

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = "MBUDC61G8LQT9ZN6"
NEWS_API_KEY = "df07c140dbf64defb62a85db608e783a"

stock_params = {
    "function" : "TIME_SERIES_DAILY",
    "symbol" : STOCK_NAME,
    "apikey": STOCK_API_KEY,
}
response = requests.get(url= STOCK_ENDPOINT, params=stock_params)
response.raise_for_status()
data = response.json()
stock_data = data["Time Series (Daily)"]
data_list = [value for (key, value) in stock_data.items()]  #Converting dictionary to list
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]
print(f"Yesterday Closing Price: {yesterday_closing_price}")

day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]
print(f"Day before yesterday Closing Price: {day_before_yesterday_closing_price}")

difference = abs(float(yesterday_closing_price) - float(day_before_yesterday_closing_price))    #Absolute function makes sure difference is positive
if (difference > 0):
    up_down = "🔺"
else:
    up_down = "🔻"

diff_percent = round((difference/float(yesterday_closing_price))*100)
print(f"Percentage Difference: {diff_percent}%")

if (diff_percent > 5):
    news_params= {
        "apiKey": NEWS_API_KEY,
        "qInTitle": COMPANY_NAME,
        
    }
    response = requests.get(url=NEWS_ENDPOINT, params=news_params)
    response.raise_for_status()
    news_data = response.json()
    news_articles = news_data["articles"]
    three_articles = news_articles[:3]  #Chooses top 3 articles
    print(f"Top 3 Articles: {three_articles}")
    
    formatted_articles_list = [f"{STOCK_NAME}: {up_down}{abs(difference)}% \nHeadline: {article["title"]}. \nBrief: {article["description"]}" for article in three_articles]
    
    for article in formatted_articles_list:
        print(article)
