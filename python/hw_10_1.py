list = []

num = 1
sum = 0

while num != 0:
    num = int(input('정수를 입력 (0을 입력하면 종료): '))
    if(num != 0):
        list.append(num)

print("입력한 정수 리스트 :", list)

for i in list:
    sum += i

print('합계 :', sum)
print('평균 :', sum/len(list))