count=1
print('カレーを召し上がれ')
while True:
    print('{}皿のカレーを食べました'.format(count))
    key = input('おかわりはいかがですか?(y/n)>>')
    if key == 'y':
        count += 1
    else:
        ans = False
        print('ごちそうさまでした')
