# -*- coding: utf-8 -*-
#인코딩을 utf-8로 변환 한글 오류 해결

#1장 파이썬 문법(1)

#if
bitcoin = 8400000
if bitcoin > 1000000:
    print("bitcoin 매수")

#if else
bitcoin = 8400000
if bitcoin >= 1000:
    print("bitcoin 1000 돌파")
else:
    print("bitcoin 1000 미만")
    
#if / elif / else
ticker = "BTC"

if ticker == "BTC":
    print("비트코인")
elif ticker == "BCH":
    print("비트코인 캐시")
elif ticker == "BTG":
    print("비트코인 골드")
elif ticker == "ETH":
    print("이더리움")
else:
    print("리플")
    
#for
for value in ["가","나","다","라"]:
    print(value)
    
ripple = [511,516,508,505,503]
for close in ripple:
    print(close)
    
tickers = ["BTC", "BTG", "BCH", "XRP", "ETH", "DASH"]
for ticker in tickers:
    print(ticker)

#for range
for num in [1,2,3,4,5,6,7,8,9,10]:
    print(num)
    
for num in range(1,11,2):
    print(num)
    
#for dic
cur_price = {"BTC": 9010000, "XRP": 511, "DASH": 360000}
for ticker in cur_price:
    print(ticker)
    
cur_price = {"BTC": 9010000, "XRP": 511, "DASH": 360000}
for ticker, price in cur_price.items(): #items() => mothod : key & value
    print(ticker, price)
    
cur_price = {"BTC": 9010000, "XRP": 511, "DASH": 360000}
for ticker in cur_price:
    print(ticker, cur_price[ticker])
    
#loop if
ripple = [511,516,508,505,503]
for close in ripple:
    if close >= 510:
        print(close)
        
#while
    #1~99
num = 1
while True:
    if num == 100:
        break
    print(num)
    num = num + 1

    #2~99
num = 1
while True:
    num = num + 1
    if num == 100:
        break
    print(num)
    
    #countinue => 조건만족시 루프 조건으로 복귀
num = 1
while True:
    num = num + 1
    if num  < 10:
        continue
    elif num == 100:
        break
    print(num)
    
#def => 호출 : 함수이름() 
def hap(a,b):
    ret = a+b
    return ret
result = hap(3,4)
print(result)

def print_ohlc(open,high,low,close):
    pass    #pass 함수제작 후 아무런 실행 x 
print_ohlc(100,120,80,90)   #pass하여도 값은 함수에 맞는 개수 필요

def print_ohlc(open,high,low,close):
    print("시가: ",open)
    print("고가: ",high)
    print("저가: ",low)
    print("종가: ",close)
print_ohlc(100,120,80,90)

def print_ohlc(ohlc):
    print("시가: ", ohlc[0])
    print("고가: ", ohlc[1])
    print("저가: ", ohlc[2])
    print("종가: ", ohlc[3])
xrp_ohlc = [100,120,80,90]
print_ohlc(xrp_ohlc)

def get_min_order(ticker):
    min_order = None
    if ticker == "ETC":
        min_order = 0.1
    elif ticker == "ETH":
        min_order = 0.5
    elif ticker == "BTC":
        min_order = 0.01
    elif ticker == "XRP":
        min_order = 10
    else:
        min_order= 0.005
    return min_order
min_order = get_min_order("BTC")
print(min_order)
min_order = get_min_order("XRP")
print(min_order)
print(get_min_order("ETC"))


#module
import coin
print(coin.get_open_price("BTC"))

import coin as newname
print(newname.get_open_price("BTC"))


from coin import get_open_price
print(get_open_price("BTC"))

#module - datetime
import datetime
now = datetime.datetime.now()
print(now)

print(now + datetime.timedelta(hours=10))
print(now - datetime.timedelta(minutes=30))

#module - requests (= web scarpping)
import requests
resp = requests.get("https://api.bithumb.com/public/ticker/BTC")
print(resp)
print(resp.content)


