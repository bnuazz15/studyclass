import math

n = input("세 개의 정수를 입력하시오 : ")
n1, n2, n3 = n.split()

n1 = int(n1)
n2 = int(n2)
n3 = int(n3)

max = n1
if max <= n2:
    max = n2
if max <= n3:
    max = n3

temp = 0
if max == n2:
    temp = n1
    n1 = n2
    n2 = temp
elif max == n3:
    temp = n1
    n1 = n3
    n3 = temp

max = n2

if max <= n3:
    max = n3

if max == n3:
    temp = n2
    n2 = n3
    n3 = temp

print("내림차순 정렬:", n1, n2, n3)