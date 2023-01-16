n = input("정수 세 개를 입력 : ")
n1, n2, n3 = n.split()
total = int(n1) + int(n2) + int(n3)
avg = total/3
print("입력 받은 값 :", n1, n2, n3)
print("총합 : ", total)
print("평균 %.2f" % avg)