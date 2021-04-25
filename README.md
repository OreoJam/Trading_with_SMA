## Trading with SMA

### Input

- target_symbols.csv
- "종목코드", "종목명"

### Output

- result.csv
- "일자", "종목코드", "B or S"(Buy / Sell)

### Condition for Buy

- SMA5가 SMA20보다 높은 경우
- 최근 5일 간의 SMA5가 SMA20을 초과한 적이 없는 경우

### Condition for Sell

- SMA5가 SMA20보다 낮은 경우
- 최근 20일 간의 SMA5가 SMA20을 하회한 적이 없는 경우
