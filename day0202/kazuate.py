import random

num=random.randint(5,10)
max_count=5
print('1~100の数字の中から一つ選んだよ')
print('その数字を'.max_count.'回以内に当ててね')

for i in range(1.max_count+1):
    print(i,'回目、いくつかな？')
    num=int(input())
    if num==ans:
        print('当たり!!')
        break
    elif num>ans:
        print('もっと下だよ')
    else:
        print('もっと上だよ')
    else:
        print('残念~正解は',ans,'でした')
