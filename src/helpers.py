import yfinance as yf

def create_stock(name, ticker, information, current_price):
    return {
        "name": name,
        "ticker": ticker,
        "information": information,
        "current_price": current_price
    }

def get_stock(ticker):
    return yf.Ticker(ticker)

def get_data(stock, period = "1y"):
    return stock.history(period = period)

def get_price(data, ticker):
    currency = ticker.info['currency']
    if currency != 'USD':
        exchange_rate = yf.Ticker(f'{currency}USD=X').history(period='1d')['Close'].iloc[-1]
        return f'{data["Close"].iloc[-1] * exchange_rate:,.2f}'
    else:
        return f'{data["Close"].iloc[-1]:,.2f}'

def make_list():
    stocks = []
    companies = ['Adidas', 'Birkenstock', 'Dr. Martens', 'Logitech', 'L\'Oreal','Nintendo', 'Samsung', 'Shiseido', 'Toyota', 'Unilever']
    tickers = ['ADDYY', 'BIRK', 'DOCMF', 'LOGI', 'LRLCY', 'NTDOY', '005930.KS', 'SSDOY', 'TM', 'UL']

    for company, ticker_symbol in zip(companies, tickers):
        ticker = get_stock(ticker_symbol)
        data = get_data(ticker)
        current_price = get_price(data, ticker)
        stock = create_stock(company, ticker_symbol, "Information about the company", current_price)
        stocks.append(stock)

    return stocks