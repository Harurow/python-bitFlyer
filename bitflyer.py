#!/usr/local/bin/python3

import os
import pybitflyer
from dotenv import load_dotenv
load_dotenv(override=True)


# 認証情報は.envから取得する
API_KEY = os.getenv('API_KEY')
API_KEY_SECRET = os.getenv('API_KEY_SECRET')

api = pybitflyer.API(API_KEY, API_KEY_SECRET)
balances = api.getbalance()

print(f'+{"":->10}+{"":->24}+{"":->24}+{"":->24}+{"":->24}+{"":->24}+')
print(f'|{"CURRENCY":^10}|{"AMOUNT":^24}|{"AVAILABLE":^24}'
      f'|{"AMOUNT(JPY)":^24}|{"AVAILABLE(JPY)":^24}|{"TRADE PRICE":^24}|')
print(f'+{"":->10}+{"":->24}+{"":->24}+{"":->24}+{"":->24}+{"":->24}+')

for balance in balances:
    currency_code = balance['currency_code']
    final_trade_price = 1.0
    disp_final_trade_price = 0.0

    amount = float(balance['amount'])
    available = float(balance['available'])

    # 保持していない通貨はパス
    if amount == 0.0 and available == 0.0:
        continue

    if currency_code != "JPY":
        # JPY以外は最終取引価格を求める
        ticker = api.ticker(product_code=f"{currency_code}_JPY")
        if ticker.get('ltp') is not None:
            final_trade_price = ticker.get('ltp')
            disp_final_trade_price = final_trade_price
    else:
        disp_final_trade_price = 1.0

    print(f'|{currency_code:^10}|{amount:>24,.8f}|{available:>24,.8f}'
          f'|{amount * final_trade_price:>24,.8f}'
          f'|{available * final_trade_price:>24,.8f}'
          f'|{disp_final_trade_price:>24,.8f}|')

print(f'+{"":->10}+{"":->24}+{"":->24}+{"":->24}+{"":->24}+{"":->24}+')
