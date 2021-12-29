import pyupbit
import numpy as np

df = pyupbit.get_ohlcv("KRW-BTC",count = 7) #당일 시가 고가 저가 종가 거래량


#변동폭 * k 계산, (고가-저가)*k값
df['range'] = (df['high'] - df['low']) * 0.5
#target(매수가)range칼럼을 한칸씩 및으로 내림(.shift(1))
df['target'] = df['open'] + df['range'].shift(1)
print(df)
#수수료
fee = 0.005
#ror(수익율),np.where(조건문, 참, 거짓)
df['ror'] = np.where(df['high'] > df['target'],
                     df['close'] / df['target'] - fee,
                     1)
#누적곱계산(cumprod) => 누적 수익율
df['hpr'] = df['ror'].cumprod()

#Drawdown 계산 (누적 최대값과 현재 hpr차이 / 누적최대값 * 100)
df['dd'] = (df['hpr'].cummax() - df['hpr']) / df['hpr'].cummax() * 100
#MDD계산(MaxDrawDown)
print("MDD(%): ", df['dd'].max())
#엑셀로 출력
df.to_excel("dd.xlsx")