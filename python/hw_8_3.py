fruit = {'배' : [2, 1000], '자몽' : [1, 2000], '메론' : [1, 8000], '감' : [6, 800]}

n = input('먹고 싶은 과일은? : ')
data = fruit.get(n)
if(data == None) :
    print(n, '준비되어 있지 않습니다')
else :
    print(n, '맛있게 드세요')
    data[0] = data[0] - 1
    fruit.update({n : data})

total = 0
for i in fruit.values():
    if(i[0] < 5):
        total = total + (5 - i[0]) * i[1]

print('')
print('각 과일 당 최소 5개는 되도록 구입합니다')
print('구입에 필요한 총 금액은 :', total, '원 입니다')
