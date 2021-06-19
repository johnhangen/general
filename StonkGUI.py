# Stonk GUI
#
# 6/18/2021
# @author Jack Hangen
# Complete
# Given a user input of a stonk ticker, return all the informaiton about the stonk

# Imports
from tkinter import *
from lxml import html
import requests

root = Tk()
root.title("STONK CHECKER")
root.iconbitmap(r"C:\Users\12034\Desktop\Summer_2021\other\favicon.ico")

def stonkGetterSP():
    ticker = ['MMM', 'ABT', 'ABBV', 'ABMD', 'ACN', 'ATVI', 'ADBE', 'AMD', 'AAP', 'AES', 'AFL', 'A', 'APD', 'AKAM', 'ALK', 'ALB', 'ARE', 'ALXN', 'ALGN', 'ALLE', 'LNT', 'ALL', 'GOOGL', 'GOOG', 'MO', 'AMZN', 'AMCR', 'AEE', 'AAL', 'AEP', 'AXP', 'AIG', 'AMT', 'AWK', 'AMP', 'ABC', 'AME', 'AMGN', 'APH', 'ADI', 'ANSS', 'ANTM', 'AON', 'AOS', 'APA', 'AIV', 'AAPL', 'AMAT', 'APTV', 'ADM', 'ANET', 'AJG', 'AIZ', 'T', 'ATO', 'ADSK', 'ADP', 'AZO', 'AVB', 'AVY', 'BKR', 'BLL', 'BAC', 'BK', 'BAX', 'BDX', 'BRK.B', 'BBY', 'BIO', 'BIIB', 'BLK', 'BA', 'BKNG', 'BWA', 'BXP', 'BSX', 'BMY', 'AVGO', 'BR', 'BF.B', 'CHRW', 'COG', 'CDNS', 'CPB', 'COF', 'CAH', 'KMX', 'CCL', 'CARR', 'CTLT', 'CAT', 'CBOE', 'CBRE', 'CDW', 'CE', 'CNC', 'CNP', 'CERN', 'CF', 'SCHW', 'CHTR', 'CVX', 'CMG', 'CB', 'CHD', 'CI', 'CINF', 'CTAS', 'CSCO', 'C', 'CFG', 'CTXS', 'CLX', 'CME', 'CMS', 'KO', 'CTSH', 'CL', 'CMCSA', 'CMA', 'CAG', 'CXO', 'COP', 'ED', 'STZ', 'COO', 'CPRT', 'GLW', 'CTVA', 'COST', 'CCI', 'CSX', 'CMI', 'CVS', 'DHI', 'DHR', 'DRI', 'DVA', 'DE', 'DAL', 'XRAY', 'DVN', 'DXCM', 'FANG', 'DLR', 'DFS', 'DISCA', 'DISCK', 'DISH', 'DG', 'DLTR', 'D', 'DPZ', 'DOV', 'DOW', 'DTE', 'DUK', 'DRE', 'DD', 'DXC', 'EMN', 'ETN', 'EBAY', 'ECL', 'EIX', 'EW', 'EA', 'EMR', 'ETR', 'EOG', 'EFX', 'EQIX', 'EQR', 'ESS', 'EL', 'ETSY', 'EVRG', 'ES', 'RE', 'EXC', 'EXPE', 'EXPD', 'EXR', 'XOM', 'FFIV', 'FB', 'FAST', 'FRT', 'FDX', 'FIS', 'FITB', 'FE', 'FRC', 'FISV', 'FLT', 'FLIR', 'FLS', 'FMC', 'F', 'FTNT', 'FTV', 'FBHS', 'FOXA', 'FOX', 'BEN', 'FCX', 'GPS', 'GRMN', 'IT', 'GD', 'GE', 'GIS', 'GM', 'GPC', 'GILD', 'GL', 'GPN', 'GS', 'GWW', 'HAL', 'HBI', 'HIG', 'HAS', 'HCA', 'PEAK', 'HSIC', 'HSY', 'HES', 'HPE', 'HLT', 'HFC', 'HOLX', 'HD', 'HON', 'HRL', 'HST', 'HWM', 'HPQ', 'HUM', 'HBAN', 'HII', 'IEX', 'IDXX', 'INFO', 'ITW', 'ILMN', 'INCY', 'IR', 'INTC', 'ICE', 'IBM', 'IP', 'IPG', 'IFF', 'INTU', 'ISRG', 'IVZ', 'IPGP', 'IQV', 'IRM', 'JKHY', 'J', 'JBHT', 'SJM', 'JNJ', 'JCI', 'JPM', 'JNPR', 'KSU', 'K', 'KEY', 'KEYS', 'KMB', 'KIM', 'KMI', 'KLAC', 'KHC', 'KR', 'LB', 'LHX', 'LH', 'LRCX', 'LW', 'LVS', 'LEG', 'LDOS', 'LEN', 'LLY', 'LNC', 'LIN', 'LYV', 'LKQ', 'LMT', 'L', 'LOW', 'LUMN', 'LYB', 'MTB', 'MRO', 'MPC', 'MKTX', 'MAR', 'MMC', 'MLM', 'MAS', 'MA', 'MKC', 'MXIM', 'MCD', 'MCK', 'MDT', 'MRK', 'MET', 'MTD', 'MGM', 'MCHP', 'MU', 'MSFT', 'MAA', 'MHK', 'TAP', 'MDLZ', 'MNST', 'MCO', 'MS', 'MOS', 'MSI', 'MSCI', 'NDAQ', 'NOV', 'NTAP', 'NFLX', 'NWL', 'NEM', 'NWSA', 'NWS', 'NEE', 'NLSN', 'NKE', 'NI', 'NSC', 'NTRS', 'NOC', 'NLOK', 'NCLH', 'NRG', 'NUE', 'NVDA', 'NVR', 'ORLY', 'OXY', 'ODFL', 'OMC', 'OKE', 'ORCL', 'OTIS', 'PCAR', 'PKG', 'PH', 'PAYX', 'PAYC', 'PYPL', 'PNR', 'PBCT', 'PEP', 'PKI', 'PRGO', 'PFE', 'PM', 'PSX', 'PNW', 'PXD', 'PNC', 'POOL', 'PPG', 'PPL', 'PFG', 'PG', 'PGR', 'PLD', 'PRU', 'PEG', 'PSA', 'PHM', 'PVH', 'QRVO', 'PWR', 'QCOM', 'DGX', 'RL', 'RJF', 'RTX', 'O', 'REG', 'REGN', 'RF', 'RSG', 'RMD', 'RHI', 'ROK', 'ROL', 'ROP', 'ROST', 'RCL', 'SPGI', 'CRM', 'SBAC', 'SLB', 'STX', 'SEE', 'SRE', 'NOW', 'SHW', 'SPG', 'SWKS', 'SLG', 'SNA', 'SO', 'LUV', 'SWK', 'SBUX', 'STT', 'STE', 'SYK', 'SIVB', 'SYF', 'SNPS', 'SYY', 'TMUS', 'TROW', 'TSLA', 'TTWO', 'TPR', 'TGT', 'TEL', 'FTI', 'TDY', 'TFX', 'TER', 'TXN', 'TXT', 'TMO', 'TIF', 'TJX', 'TSCO', 'TT', 'TDG', 'TRV', 'TFC', 'TWTR', 'TYL', 'TSN', 'UDR', 'ULTA', 'USB', 'UAA', 'UA', 'UNP', 'UAL', 'UNH', 'UPS', 'URI', 'UHS', 'UNM', 'VLO', 'VAR', 'VTR', 'VRSN', 'VRSK', 'VZ', 'VRTX', 'VFC', 'VIAC', 'VTRS', 'V', 'VNT', 'VNO', 'VMC', 'WRB', 'WAB', 'WMT', 'WBA', 'DIS', 'WM', 'WAT', 'WEC', 'WFC', 'WELL', 'WST', 'WDC', 'WU', 'WRK', 'WY', 'WHR', 'WMB', 'WLTW', 'WYNN', 'XEL', 'XRX', 'XLNX', 'XYL', 'YUM', 'ZBRA', 'ZBH', 'ZION', 'ZTS']


    larger = Tk()
    larger.title("All Stonks")
    w = Scrollbar (larger)
    w.pack(W)
    stonktitles = ["name", "price", "change_per", "previous_close", "Open", "Bid", "Ask_per", "day_range", "weeks_range", "volume", "avg_volume", "market_cap", "beta", "pe_ratio", "eps", "earnings_date", "forward_div_yel", "ex_div_date", "target_est"]

    for j in range(len(stonktitles)):
        askStonk = Label(larger, text=str(stonktitles[j]))
        askStonk.grid(column=j, row=0)

    for i in range(len(ticker)):
        YahooFinanceURL = f'https://finance.yahoo.com/quote/{ticker[i]}'

        resp = requests.get(url=YahooFinanceURL)
        tree = html.fromstring(resp.content)

        name = tree.xpath('//div[contains(@data-test,"quote-header")]/div[2]/div[1]/div[1]/h1/text()')
        price = tree.xpath('//div[contains(@data-test,"quote-header")]/div[3]/div[1]/div[1]/span[1]/text()') 
        change_per = tree.xpath('//div[contains(@data-test,"quote-header")]/div[3]/div[1]/div[1]/span[2]/text()') 

        #  Left
        previous_close = tree.xpath('//div[contains(@data-test,"left-summary-table")]/table/tbody/tr[1]/td[2]/span/text()') 
        Open = tree.xpath('//div[contains(@data-test,"left-summary-table")]/table/tbody/tr[2]/td[2]/span/text()') 
        Bid = tree.xpath('//div[contains(@data-test,"left-summary-table")]/table/tbody/tr[3]/td[2]/span/text()') 
        Ask_per = tree.xpath('//div[contains(@data-test,"left-summary-table")]/table/tbody/tr[4]/td[2]/span/text()') 
        day_range = tree.xpath('//div[contains(@data-test,"left-summary-table")]/table/tbody/tr[5]/td[2]/text()') 
        weeks_range = tree.xpath('//div[contains(@data-test,"left-summary-table")]/table/tbody/tr[6]/td[2]/text()')
        volume = tree.xpath('//div[contains(@data-test,"left-summary-table")]/table/tbody/tr[7]/td[2]/span/text()')
        avg_volume = tree.xpath('//div[contains(@data-test,"left-summary-table")]/table/tbody/tr[8]/td[2]/span/text()')

        #  Right
        market_cap = tree.xpath('//div[contains(@data-test,"right-summary-table")]/table/tbody/tr[1]/td[2]/span/text()')
        beta = tree.xpath('//div[contains(@data-test,"right-summary-table")]/table/tbody/tr[2]/td[2]/span/text()')
        pe_ratio = tree.xpath('//div[contains(@data-test,"right-summary-table")]/table/tbody/tr[3]/td[2]/span/text()')
        eps = tree.xpath('//div[contains(@data-test,"right-summary-table")]/table/tbody/tr[4]/td[2]/span/text()')
        earnings_date = tree.xpath('//div[contains(@data-test,"right-summary-table")]/table/tbody/tr[5]/td[2]/span/text()')
        forward_div_yel = tree.xpath('//div[contains(@data-test,"right-summary-table")]/table/tbody/tr[6]/td[2]/text()')
        ex_div_date = tree.xpath('//div[contains(@data-test,"right-summary-table")]/table/tbody/tr[7]/td[2]/span/text()')
        target_est = tree.xpath('//div[contains(@data-test,"right-summary-table")]/table/tbody/tr[8]/td[2]/span/text()')

        stonkItems = [name, price, change_per, previous_close, Open, Bid, Ask_per, day_range, weeks_range, volume, avg_volume, market_cap, beta, pe_ratio, eps, earnings_date, forward_div_yel, ex_div_date, target_est]
        print(stonkItems)
        
        for j in range(len(stonkItems)):
            askStonk = Label(larger, text=str(stonkItems[j]))
            askStonk.grid(column=j, row= i+1)

def stonkGetter():
    stock = str(StonkEntry.get())
    YahooFinanceURL = f'https://finance.yahoo.com/quote/{stock}'

    resp = requests.get(url=YahooFinanceURL)
    tree = html.fromstring(resp.content)

    #  Bases
    #top_base = tree.xpath('//div[contains(@data-test,"quote-header")]')
    #left_base = tree.xpath('//div[contains(@data-test,"left-summary-table")]/table/tbody')
    #right_base = tree.xpath('//div[contains(@data-test,"right-summary-table")]/table/tbody')

    #  Top
    name = tree.xpath('//div[contains(@data-test,"quote-header")]/div[2]/div[1]/div[1]/h1/text()')
    price = tree.xpath('//div[contains(@data-test,"quote-header")]/div[3]/div[1]/div[1]/span[1]/text()') 
    change_per = tree.xpath('//div[contains(@data-test,"quote-header")]/div[3]/div[1]/div[1]/span[2]/text()') 

    #  Left
    previous_close = tree.xpath('//div[contains(@data-test,"left-summary-table")]/table/tbody/tr[1]/td[2]/span/text()') 
    Open = tree.xpath('//div[contains(@data-test,"left-summary-table")]/table/tbody/tr[2]/td[2]/span/text()') 
    Bid = tree.xpath('//div[contains(@data-test,"left-summary-table")]/table/tbody/tr[3]/td[2]/span/text()') 
    Ask_per = tree.xpath('//div[contains(@data-test,"left-summary-table")]/table/tbody/tr[4]/td[2]/span/text()') 
    day_range = tree.xpath('//div[contains(@data-test,"left-summary-table")]/table/tbody/tr[5]/td[2]/text()') 
    weeks_range = tree.xpath('//div[contains(@data-test,"left-summary-table")]/table/tbody/tr[6]/td[2]/text()')
    volume = tree.xpath('//div[contains(@data-test,"left-summary-table")]/table/tbody/tr[7]/td[2]/span/text()')
    avg_volume = tree.xpath('//div[contains(@data-test,"left-summary-table")]/table/tbody/tr[8]/td[2]/span/text()')

    #  Right
    market_cap = tree.xpath('//div[contains(@data-test,"right-summary-table")]/table/tbody/tr[1]/td[2]/span/text()')
    beta = tree.xpath('//div[contains(@data-test,"right-summary-table")]/table/tbody/tr[2]/td[2]/span/text()')
    pe_ratio = tree.xpath('//div[contains(@data-test,"right-summary-table")]/table/tbody/tr[3]/td[2]/span/text()')
    eps = tree.xpath('//div[contains(@data-test,"right-summary-table")]/table/tbody/tr[4]/td[2]/span/text()')
    earnings_date = tree.xpath('//div[contains(@data-test,"right-summary-table")]/table/tbody/tr[5]/td[2]/span/text()')
    forward_div_yel = tree.xpath('//div[contains(@data-test,"right-summary-table")]/table/tbody/tr[6]/td[2]/text()')
    ex_div_date = tree.xpath('//div[contains(@data-test,"right-summary-table")]/table/tbody/tr[7]/td[2]/span/text()')
    target_est = tree.xpath('//div[contains(@data-test,"right-summary-table")]/table/tbody/tr[8]/td[2]/span/text()')

    stonkItems = [name, price, change_per, previous_close, Open, Bid, Ask_per, day_range, weeks_range, volume, avg_volume, market_cap, beta, pe_ratio, eps, earnings_date, forward_div_yel, ex_div_date, target_est]
    stonktitles = ["name", "price", "change_per", "previous_close", "Open", "Bid", "Ask_per", "day_range", "weeks_range", "volume", "avg_volume", "market_cap", "beta", "pe_ratio", "eps", "earnings_date", "forward_div_yel", "ex_div_date", "target_est"]
    
    second = Tk()
    second.title(stock.upper())

    for i in range(len(stonktitles)):
        askStonk = Label(second, text=str(stonktitles[i]))
        askStonk.grid(column=i, row=4)
    
    for i in range(len(stonkItems)):
        askStonk = Label(second, text=str(stonkItems[i]))
        askStonk.grid(column=i, row=5)


askStonk = Label(root, text="Enter Stonk Ticker")
askStonk.grid(column=1, row=1)

stonkSubmit = Button(root, text="Get Stonk information", padx=20, pady = 10, command= stonkGetter)
stonkSubmit.grid(column=2, row=2)

stonkSubmit = Button(root, text="Get all Stonk information", padx=20, pady = 10, command= stonkGetterSP)
stonkSubmit.grid(column=2, row=3)

StonkEntry = Entry(root, borderwidth= 5)
StonkEntry.grid(column=1, row=2)

root.mainloop()