# if condition :
#   statement1
#   statement2
# elif condition2 :
#   statement3
# else :
#   statement4

# 자료형의 값으로 True/False 결정 가능. 0이거나, 값이 비어있으면 False (condition으로 쓰일 때 사용됨)
# numeric : 0 (False) / else (True)
# string : "" (False) / "abc" (True)
# list : [] (False) / [1,2, ...] (True)
# tuple : () (False) / (1,) (True)
# dictionary : {} (False) / {"a" : b} (True)

n = 1
k = False

if n and k:
    print("True")
else :
    print("False")