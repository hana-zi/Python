amount=int(input('支払総額を入力してください>>'))
pepple=int(input('参加人数を入力してください>>'))

dnum=amount/people
pay=dnum//100*100

if dnum>pay:
    pay(pay+100)

    payorg = amount - pay * (people -1)
    print('***支払額**')
    print('1人あたり{}円({}人)、幹事は{}円です'
            .format(pay,people - 1,payorg))
