## Trading with SMA

### Input

- target_symbols.csv
- "종목코드", "종목명"

### Output

- result.csv
- "일자", "종목코드", "B or S"(Buy / Sell)

### Run

- python trading_sma_5_20.py

### Condition for Buy

- SMA5가 SMA20보다 높은 경우
- 최근 5일 간의 SMA5가 SMA20을 초과한 적이 없는 경우

### Condition for Sell

- SMA5가 SMA20보다 낮은 경우
- 최근 20일 간의 SMA5가 SMA20을 하회한 적이 없는 경우

### Modules

- yfinance (https://pypi.org/project/yfinance/)
- pandas (https://pandas.pydata.org/)
- pandas_datareader (https://pandas-datareader.readthedocs.io/en/latest/)
