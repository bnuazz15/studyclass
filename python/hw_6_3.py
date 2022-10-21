n = input("두 자리 정수 두개를 입력 : ")
n1, n2 = n.split()

if n1[0] == n2[0] and n1[1] == n1[1]:
    print("두 정수는 모두 {n1} 로 같은 정수입니다.".format(n1 = n1))
elif n1[0] == n2[1] and n1[1] == n2[0]:
    print("{n1} , {n2} : 자리 값만 다른 정수입니다.".format(n1 = n1, n2 = n2))
elif n1[0] == n2[0] or n1[0] == n2[1] or n1[1] == n2[0] or n1[1] == n2[1]:
    print("{n1} , {n2} : 하나의 숫자만 일치합니다.".format(n1 = n1, n2 = n2))
else:
    print("{n1} , {n2} : 일치하지 않는 정수입니다.".format(n1 = n1, n2 = n2))