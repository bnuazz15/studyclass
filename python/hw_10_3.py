num_list = list(map(int, input('정수들을 입력 :\n').split()))

sum = 0
negative = 0
positive = 0

for i in num_list:
    sum = sum + i
    if(i > 0):
        positive = positive + 1
    elif (i < 0):
        negative = negative + 1
    
if(len(num_list) == 0):
    print('입력한 숫자가 없습니다')

print('양수:', positive, '개, 음수 :', negative, '개, 합계 :', sum)

