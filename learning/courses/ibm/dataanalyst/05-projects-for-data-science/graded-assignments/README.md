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

## Stock Data Using a Web Scraping

1. **What is the primary role of the BeautifulSoup library in the web scraping process?**
   - [ ] To automatically control a web browser like Firefox or Chrome.
   - [ ] To download the raw HTML content from a specific URL.
   - [x] To parse HTML or XML content and create a navigable tree structure.
   - [ ] To directly convert scraped data into a machine learning model.

2. **In an HTML document, which tag is used to define a single table row that contains table cell data?**
   - [ ] `<table>`
   - [ ] `<td>`
   - [x] `<tr>`
   - [ ] `<th>`

3. **When using the** `find_all('p')` **method on a BeautifulSoup soup object, what kind of result is returned?**
   - [ ] A single string containing the text from all paragraph tags combined.
   - [ ] A Pandas DataFrame with all paragraphs organized into rows.
   - [x] A list-like iterable containing all the paragraph (`<p>`) tag objects.
   - [ ] The first paragraph (`<p>`) tag found in the document.

4. **According to the module content, what is a significant limitation of using the** `pandas.read_html()` **function for web scraping?**
   - [ ] It is significantly slower than using BeautifulSoup for all tasks.
   - [ ] It requires a paid subscription, unlike open-source libraries like BeautifulSoup.
   - [x] It can only extract data from HTML `<table>` tags and is not flexible for other content.
   - [ ] It cannot download data from websites that use HTTPS.

5. **In the HTML tree structure, if the** `<head>` **tag and** `<body>` **tag are both directly inside the** `<html>` **tag, what is their relationship to each other?**
   - [ ] The `<body>` tag is the parent of the `<head>` tag.
   - [x] They are siblings.
   - [ ] The `<head>` tag is a child of the `<body>` tag.
   - [ ] They are both descendants but not children of the `<html>` tag.
