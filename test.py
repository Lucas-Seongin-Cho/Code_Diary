import pyupbit

access = "oA4fRUOc9cpMlrgDVZ6AP96GFLMdaQkntPx1eA78"          # 본인 고유값으로 변경
secret = "csGafUOofqEnBp5F1mWQrBa2QMw3fqqhdiGuAU1U"          # 본인 고유값으로 변경
upbit = pyupbit.Upbit(access, secret)

print(upbit.get_balance("KRW-XRP"))     # KRW-XRP 조회
print(upbit.get_balance("KRW"))         # 보유 현금 조회