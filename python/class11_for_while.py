# for in iterable:
#   to-do

# print(range(5)) --> range(5) 로 자료형으로 쓰려면 tuple(range(5)) 이런 식으로 변환 필요
# list conprehension (리스트 내포)
# a = [1,2,3,4]
# result = [num * 3 for num in a] --> [3, 6, 9, 12]
# result = [num * 3 for num in a if num % 2 == 0] --> [6, 12]
# 
# L = input("Numbers? ") # 정수로 구성된 문자열 입력
# L = L.split() # 정수 문자열로 분리
# for i in range(len(L)) : # 정수 문자열을 정수로 변환
# L[i] = int(L[i]) 
# print(L) # 변환된 정수 리스트 출력

# 위와 동일한 코드
# L =[ int(x) for x in input("Numbers? ").split() ]