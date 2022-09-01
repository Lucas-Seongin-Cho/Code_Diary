import time
import pyupbit
import datetime

# Upbit API access and secret key
access = "AEyjWpHlE8M6jt75zQxVmyfWffL5cKps2HHdWxEr"
secret = "xEWpUM1itP82I493HsdIctM1m8fbuGI1VYx2nsNT"

def get_target_price(ticker, k):
    """변동성 돌파 전략으로 매수 목표가 조회"""
    # ohlcv of ticker for last two days
    df = pyupbit.get_ohlcv(ticker, interval="day", count=2)
    # Returning target price
    target_price = df.iloc[0]['close'] + (df.iloc[0]['high'] - df.iloc[0]['low']) * k
    return target_price

def get_start_time(ticker):
    """시작 시간 조회"""
    # ohlcv of ticker for last day
    df = pyupbit.get_ohlcv(ticker, interval="day", count=1)
    # Returning start time
    start_time = df.index[0]
    return start_time

def get_ma15(ticker):
    """15일 이동 평균선 조회"""
    # ohlcv of ticker for last fifteen days
    df = pyupbit.get_ohlcv(ticker, interval="day", count=15)
    # Returning moving average line for last fifteen days
    ma15 = df['close'].rolling(15).mean().iloc[-1]
    return ma15

def get_balance(ticker):
    """잔고 조회"""
    # Upbit balance inquiry
    balances = upbit.get_balances()
    for b in balances:
        if b['currency'] == ticker:
            # When there is balance, return the left balance, if not, return 0
            if b['balance'] is not None:
                return float(b['balance'])
            else:
                return 0
    return 0

def get_current_price(ticker):
    """현재가 조회"""
    # Returning the current price
    return pyupbit.get_orderbook(ticker=ticker)["orderbook_units"][0]["ask_price"]

# <Log in using personal access and secret key>
upbit = pyupbit.Upbit(access, secret)
# When loging in, start autotrade
print("autotrade start")

# <Start Auto trade>
while True:
    # State star time and end time
    try:
        now = datetime.datetime.now()
        start_time = get_start_time("KRW-BTC")
        end_time = start_time + datetime.timedelta(days=1)
        # 09:00<current time<08:59:50
        if start_time < now < end_time - datetime.timedelta(seconds=10):
            # Target price of Bitcoin
            target_price = get_target_price("KRW-BTC", 0.5)
            # Moving average for 15days of Bitcoin
            ma15 = get_ma15("KRW-BTC")
            # Current price of Bitcoin
            current_price = get_current_price("KRW-BTC")
            # If current price and ma for 15 is greater than target price and lower than current price, return the balance.
            if target_price < current_price and ma15 < current_price:
                krw = get_balance("KRW")
                # If balance is larger than 5000, buy possible amount of Bitcoin
                if krw > 5000:
                    upbit.buy_market_order("KRW-BTC", krw*0.9995)
        # If Bitcoin passed amount of 0.00008, sell them
        else:
            btc = get_balance("BTC")
            if btc > 0.00008:
                upbit.sell_market_order("KRW-BTC", btc*0.9995)
        time.sleep(1)
        # If all of the conditions are not fit, let it be
    except Exception as e:
        print(e)
        time.sleep(1)