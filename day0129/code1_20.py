price=input('料金を入力>>')#キーノード入力結果はstr型
price=int(price)
number=input('人数を入力>>')
number=int(number)
payment=price/number
payment=int(payment)
print('お支払いは'+payment+'円です')
