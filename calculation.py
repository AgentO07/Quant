import pandas as pd

def calculate_daily_return(csv,date_column=date_col,price_column='Close'):

	df = pd.read_csv(csv)
	df[date_column] = pd.to_datetime([date_column])
	df = df.set_index(date_column)
	
	df = df.sort_index()
	
	df['Daily_Return'] = df[price_column].pct_change()*100
	
	return df
	
if __name__ == "__main__":
	csv = 'AAPL_5_yr_data.csv'
	date_col = "Date"
	price_col = "Close"

	df_with_returns = calculate_daily_returns(csv,date_column=date_col,price_column=price_col)
	
	print(df_with_returns.head())
	print(df_with_returns['Daily_Returns'].describe())
