import pandas as pd
import numpy as nd

def eval_sma_buy(df):
  e_date = df.index.max()
  s_date = df.index.min()

  # SMA5 > SMA20 -> PASS
  # SMA5 <= SMA20 -> FALSE
  if (df.loc[e_date]['SMA5'] <= df.loc[e_date]['SMA20']):
    return False
  
  # SMA5 of last day < SMA20 of last 5 days -> PASS
  # SMA5 of last day >= SMA20 of last 5 days -> FALSE
  p_date = df[:e_date].index[:-1].max() # Yesterday
  if (df.loc[:p_date]['SMA5'] >= df.loc[:p_date]['SMA20']).any():
    return False
  
  return True

def eval_sma_sell(df):
  e_date = df.index.max()
  s_date = df.index.min()

  # SMA5 < SMA20 -> TRUE
  # SMA5 >= SMA20 -> FALSE
  if (df.loc[e_date]['SMA5'] >= df.loc[e_date]['SMA20']):
    return False

  # SMA5 of last day > SMA20 of last 20 days -> PASS
  # SMA5 of last day <= SMA20 of last 20 days -> FALSE
  p_date = df[:e_date].index[:-1].max() # Yesterday
  if (df.loc[:p_date]['SMA5'] <= df.loc[:p_date]['SMA20']).any():
    return False
  
  return True


def main():
  print("Hello World")


if __name__ == '__main__':
    main()