def isTwoNum(x):
    count = 0
    for i in x:
        if(i.isdigit()):
            count = count + 1
    
    if(count < 2):
        return False
    
    return True 

def validPassword(x):
    if(len(x) < 8):
        print('error! 8 글자 이상이어야 함')
        return False
    if(not x.isalnum()):
        print('error! 영문자, 숫자로만 구성되어야 함')
        return False
    if(x.isdigit()):
        print('error! 영문도 포함되어야 함')
        return False
    if(x.isalpha()):
        print('error! 숫자도 포함되어야 함')
        return False
    if(not isTwoNum(x)):
        print('error! 최소한 2개의 숫자를 포함해야 함')
        return False
    return True	


valid = False

for i in range(0, 5):
    password = input('Enter password: ')
    valid = validPassword(password)
    if(valid):
        print('Valid password')
        break
    else:
        print('Invalid password')