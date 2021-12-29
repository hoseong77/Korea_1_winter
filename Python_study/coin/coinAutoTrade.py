import time
import pyupbit
import datetime

access = "LdnLc27yjLlx7MmIHyfYvzTnebM8yxBuNo4s8FQP"
secret = "Fu7UIcSVbDy8i87Mh3ivAIB6jenkGZtP1jUWhJVR"
myToken = "xoxb-2887580007333-2890578944355-ybCWYsA7VYMfpm3Kv0knX693"

def post_message(token, channel, text):
    """���� �޽��� ����"""
    response = requests.post("https://slack.com/api/chat.postMessage",
        headers={"Authorization": "Bearer "+token},
        data={"channel": channel,"text": text}
    )

def get_target_price(ticker, k):
    """������ ���� �������� �ż� ��ǥ�� ��ȸ"""
    df = pyupbit.get_ohlcv(ticker, interval="day", count=2)
    target_price = df.iloc[0]['close'] + (df.iloc[0]['high'] - df.iloc[0]['low']) * k
    return target_price

def get_start_time(ticker):
    """���� �ð� ��ȸ"""
    df = pyupbit.get_ohlcv(ticker, interval="day", count=1)
    start_time = df.index[0]
    return start_time

def get_ma15(ticker):
    """15�� �̵� ��ռ� ��ȸ"""
    df = pyupbit.get_ohlcv(ticker, interval="day", count=15)
    ma15 = df['close'].rolling(15).mean().iloc[-1]
    return ma15

def get_balance(ticker):
    """�ܰ� ��ȸ"""
    balances = upbit.get_balances()
    for b in balances:
        if b['currency'] == ticker:
            if b['balance'] is not None:
                return float(b['balance'])
            else:
                return 0
    return 0

def get_current_price(ticker):
    """���簡 ��ȸ"""
    return pyupbit.get_orderbook(ticker=ticker)["orderbook_units"][0]["ask_price"]

# �α���
upbit = pyupbit.Upbit(access, secret)
print("autotrade start")

# ���� �޼��� ���� ����
post_message(myToken,"#crypto", "autotrade start")

# �ڵ��Ÿ� ����
while True:
    try:
        now = datetime.datetime.now()
        start_time = get_start_time("KRW-XEC")
        end_time = start_time + datetime.timedelta(days=1)

        if start_time < now < end_time - datetime.timedelta(seconds=10):
            target_price = get_target_price("KRW-XEC", 2)
            ma15 = get_ma15("KRW-XEC")
            current_price = get_current_price("KRW-XEC")
            if target_price < current_price and ma15 < current_price:
                krw = get_balance("KRW")
                if krw > 5000:
                    buy_result = upbit.buy_market_order("KRW-XEC", krw*0.9995)
                    post_message(myToken,"#crypto", "XEC buy : " +str(buy_result))
        else:
            xec = get_balance("XEC")
            if xec > 40:
                sell_result = upbit.sell_market_order("KRW-XEC", xec*0.9995)
                post_message(myToken,"#crypto", "XEC buy : " +str(sell_result))
        time.sleep(1)
    except Exception as e:
        print(e)
        time.sleep(1)