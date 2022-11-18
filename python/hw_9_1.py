for i in range(0,10) :
    num = int(input('Enter a number : '))
    
    odd_even = '홀수'
    pos_neg = '양수'

    if(num == 0):
        print('입력 받은 수가 0 입니다')
        print('프로그램을 종료합니다')
        break;
    
    if(num > 0):
        pos_neg = '양수'
    else:
        pos_neg = '음수'
    
    if(num % 2 == 0):
        odd_even = '짝수'
    else:
        odd_even = '홀수'
    
    print(num, ':', pos_neg + ',', odd_even)
