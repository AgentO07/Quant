import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta

ticker_symbol = "AAPL"

end_date = datetime.now()
start_date = end_date - timedelta(days=5*365) # No of years of data you want to work on

print(f"fetching data for {ticker_symbol} from {start_date.strftime('%Y-%m-%d')} to {end_date.strftime('%Y-%m-%d')}")


try:
	data = yf.download(ticker_symbol, start=start_date, end=end_date)
	print(data.head())
	print(data.tail())
	data.info

	#Save to a file
	file_name = f"{ticker_symbol}_5_yr_data.csv"
	data.to_csv(file_name)

	print(f"\nData saved to {file_name}")
except Exception as e:
	print("Error Occured")

