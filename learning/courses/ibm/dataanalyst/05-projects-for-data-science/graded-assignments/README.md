# Graded Assignment

## Stock Data Using a Python Library

1. **Which line of Python code correctly creates a yfinance Ticker object for the company with the stock symbol "AAPL"?**
   - [x] `aapl = yf.Ticker("AAPL")`
   - [ ] `aapl = yf.get_ticker("AAPL")`
   - [ ] `aapl = yf.History("AAPL")`
   - [ ] `aapl = yf.Ticker(AAPL)`

2. **What is the primary purpose of the .history() method when called on a yfinance Ticker object?**
   - [ ] To get the latest, real-time stock price.
   - [ ] To retrieve company profile information like its sector and business summary.
   - [ ] To display a graph of the stock's performance.
   - [x] To download historical market data like open, high, low, and close prices.

3. **If you execute the code** `stock_data = msft.history(period="ytd")`**, what data will be retrieved?**
   - [x] Historical data from the beginning of the current year to today.
   - [ ] All historical data from one year ago to today.
   - [ ] All available historical data for the stock.
   - [ ] Data for yesterday only.

4. **What type of Python object is returned by the** `ticker.history()` **method?**
   - [x] A Pandas DataFrame
   - [ ] A Python Dictionary
   - [ ] A List of Lists
   - [ ] A JSON string

5. **Which attribute of a yfinance Ticker object is used to retrieve static company information like its industry, country, and a long business summary?**
   - [ ] .metadata
   - [ ] .summary
   - [ ] .details()
   - [x] .info

6. **What is the data structure of the object returned by the .info attribute?**
   - [ ] A NumPy Array
   - [ ] A Pandas DataFrame
   - [x] A Python Dictionary
   - [ ] A Python Set

7. **Assuming** `amd = yf.Ticker("AMD")`**, which line of code correctly accesses the company's sector from its information dictionary?**
   - [ ] `amd.sector`
   - [ ] `amd.history['sector']`
   - [ ] `amd.info('sector')`
   - [x] `amd.info['sector']`

8. **After running** `amd_data = amd.history(period="max")`**, what are the names of the columns that represent the stock's opening and closing price for a given day?**
   - [ ] 'Price' and 'Volume'
   - [ ] 'High' and 'Low'
   - [x] 'Open' and 'Close'
   - [ ] 'Start' and 'End'

9. **The yfinance Python library provides an interface for downloading market data from which primary online source?**
   - [x] Yahoo Finance
   - [ ] Google Finance
   - [ ] The New York Stock Exchange (NYSE)
   - [ ] Bloomberg Terminal

10. **You need to download historical stock data for exactly the last 6 months using the .history() method. Which value for the period parameter should you use to accomplish this?**
    - [ ] period="6d"
    - [ ] period="ytd"
    - [x] period="6mo"
    - [ ] period="max"
