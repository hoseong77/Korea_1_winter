import pyupbit

access = "LdnLc27yjLlx7MmIHyfYvzTnebM8yxBuNo4s8FQP"
secret = "Fu7UIcSVbDy8i87Mh3ivAIB6jenkGZtP1jUWhJVR"
upbit = pyupbit.Upbit(access,secret)

print(upbit.get_balance("KRW-XEC"))
print(upbit.get_balance("KRW"))