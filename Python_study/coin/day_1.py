# -*- coding: utf-8 -*-
#인코딩을 utf-8로 변환 한글 오류 해결

#slicing
greeting = "hello minsu"

print(greeting[:5]) #0~4index slicing

print(greeting[6:]) #6~

#list
hold = ["btc_krw","xrp_krw","eth_krw"]

print(hold[0])
print(hold[1])
print(hold[2])
print(type(hold))
#list slicing
portfolio = ["BTC", "ETH", "XRP", "BCH", "DASH"]
print(portfolio[0:3])

#list add
portfolio = []
portfolio.append("BTC") #.append : list add
portfolio.append("ETH")
portfolio.append("XRP")
print(portfolio)

portfolio.insert(1,"DASH") #list index[1] -> DASH add
print(portfolio)

#list delete
portfolio = ["BTC","XRP","ETH"]
del portfolio[1] #index[1] delete
print(portfolio)

#max min average
ripple_close = [503,505,508,501,530]
print(max(ripple_close)) #max
print(min(ripple_close)) #min

a = [1,2,3,4]
average = sum(a)/len(a) #average = sum/len
print(average)

#tuple add, delete => can't
portfolio = ("ETC","ETH","BTC")
print(portfolio)
print(type(portfolio))

#tuple slicing
print(portfolio[0:2])

#dict
prices = {'BTC':8300000,'XRP':514}
print(prices)

prices = {}
prices['BTC'] = 8300000
prices['XRP'] = 514
print(prices)

#dict indexing
print(prices['BTC']) # value indexing ==> can't ex)prices[1] => X

#dict add
prices = {'BTC':8300000,'XRP':514}
prices['ETH'] = 600000
print(prices)

#dict edit
prices = {'BTC':8300000,'XRP':514}
prices['XRP'] = 513
print(prices)

#dict delete
prices = {'BTC': 8300000, 'XRP': 514}
del prices['XRP']
print(prices)

#dict key
prices = {'BTC': 8300000, 'XRP': 514,'ETH':600000}
print(prices.keys())

#dict values
prices = {'BTC': 8300000, 'XRP': 514,'ETH':600000}
print(prices.values())