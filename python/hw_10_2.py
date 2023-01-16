def primenumber(x):
    for i in range(2, x):	
        if x % i == 0:		
            return False
    return True	

num = int(input('구하려는 소수의 개수를 입력 : '))

a = 2

for i in range(0, num):
    while(True):
        isprimeNumber = primenumber(a)
        a = a+1
        if(isprimeNumber):
            print(a-1)
            break
        
print(num, "개의 소수를 찾았습니다")