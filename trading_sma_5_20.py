import csv
import yfinance as yf
import pandas as pd
from pandas_datareader import data as pdr
import datetime as dt
import evaluate_sma as evsma

## FUNCTION ################################################

# get stock price list & calculate SMA
def get_stock_price(code):
  # get 100 days information
  end_dt = dt.datetime.now()
  dt_gap = dt.timedelta(days = 100)
  start_dt = end_dt - dt_gap

  # get price list
  df = pdr.get_data_yahoo(code, start_dt, end_dt)
  df = df.loc[:, ["Open", "High", "Low", "Adj Close", "Volume"]]
  df = df.rename(columns={"Adj Close": "Close"})

  # SMA 5days
  # Series to DataFrame
  sma5 = df['Close'].rolling(window=5).mean()
  df_sma5 = sma5.to_frame(name='SMA5')

  # SMA 20days
  # Series to DataFrame
  sma20 = df['Close'].rolling(window=20).mean()
  df_sma20 = sma20.to_frame(name='SMA20')

  # Concatenate SMA5 and SMA20
  df_sma = pd.concat([df['Close'], df_sma5, df_sma20], axis=1)
  # Remove NaN
  df_sma = df_sma.dropna()

  return df_sma

# evaluate stock
def evaluate_sma(df):
  last_date = df.index.max()
  dt_gap = dt.timedelta(days = 20)
  first_date = last_date - dt_gap

  # BUY - 평가일부터 이전 5일간의 SMA를 가지고 평가
  max_date = last_date
  min_date = df[:max_date].index[-5:][0]
  df_for_buy = df.loc[min_date : max_date].copy()

  ''' for test
  df_for_buy['SMA5'] = 1
  df_for_buy.loc[max_date, 'SMA5'] = 1000

  print("TEST " + str(df_for_buy.loc[max_date, 'SMA5']))
  print("TEST " + str(df_for_buy.loc[max_date, 'SMA20']))
  print("TEST " + min_date.strftime("%Y%m%d"))
  print("TEST " + max_date.strftime("%Y%m%d"))
  '''

  # Call EvalBuy from evaluate_sma.py
  if evsma.eval_sma_buy(df_for_buy):
    #print("[signal]-[buy]-[{}]".format(max_date.strftime("%Y%m%d")))
    return (last_date, "B")

  # SELL - 평가일부터 이전 20일간의 SMA를 가지고 평가
  max_date = last_date
  min_date = df[:max_date].index[-20:][0]
  df_for_sell = df.loc[min_date : max_date].copy()

  # Call EvalSell from evaluate_sma.py
  if evsma.eval_sma_sell(df_for_sell):
    #print("[signal]-[sell]-[{}]".format(max_date.strftime("%Y%m%d")))
    return (last_date, "S")

############################################################

## PROC ####################################################
# Initialize
yf.pdr_override()
# result condition
something_traded = False

# open result file
result_file = open('result.csv', 'w', newline='')
rf = csv.writer(result_file)

# read symbol list
# csv - symbol, stock_name
with open('target_symbols.csv', 'r') as symbol_file:
  reader = csv.reader(symbol_file)

  for item in reader:
    print("Symbol - " + item[0] + " ---------------------------")
    df_sma_5_20 = get_stock_price(item[0])
    result_evaluate = evaluate_sma(df_sma_5_20)
    if (result_evaluate):
      rf.writerow([result_evaluate[0].strftime("%Y%m%d"), item[0], result_evaluate[1]])
      something_traded = True

# close result file
result_file.close()

if (something_traded == True):
  print("There is something to trade.")
else:
  print("There is nothing to trade.")

