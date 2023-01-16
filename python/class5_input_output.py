# input()
# string 으로 받게되어 필요 시, casting 필요
# 여러 개 받고 싶을 때,
n1, n2 = input("Enter two numbers: ").split()
n1 = int(n1)
n2 = int(n2)

# print(a, b) --> a 와 b 를 스페이스 간격으로 출력
# print() 는 자동으로 \n 이 되어, \n 안하고 싶을 때 print(a, end = '') 사용
print('hello', end = '')
print('world')