import requests
from twilio.rest import Client
from newsapi import NewsApiClient
import os
from datetime import date
from datetime import timedelta


STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={STOCK}&apikey={os.environ["ALPHA"]}'
response = requests.get(url)
response.raise_for_status()
stock_data = response.json()
stock_data_refined = stock_data["Time Series (Daily)"]
yesterday = date.today()-timedelta(days=1)
day_before_yesterday = yesterday-timedelta(days=1)
initial_closing = stock_data_refined[str(day_before_yesterday)]["4. close"]
final_closing = stock_data_refined[str(yesterday)]["4. close"]

percent_change = (float(final_closing)-float(initial_closing))*100/float(final_closing)

if percent_change<0:
    symbol_to_print = f"↓{abs(int(percent_change))}%"
else:
    symbol_to_print = f"↑{abs(int(percent_change))}%"

print(symbol_to_print)



## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number.


# Optional: Format the SMS message like this:
# """TSLA: 🔺2% Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. Brief: We at Insider Monkey have
# gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings
# show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
# or "TSLA: 🔻5% Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. Brief: We at Insider Monkey
# have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F
# filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus
# market crash. """



