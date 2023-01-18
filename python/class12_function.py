# def function_name(parameters) :
#    """docstring""" # optional(없어도 됨)
#    statements # 함수 기능에 필요한 statements
#    return ret_values # return 값이 없는 경우, 함수는 None 값 반환
#   return a, b # 튜플로 반환하여 여러 값 return 가능
#
# def test(b):
#   pass
# a = 3
# test(a)
# argument a 가 immutable 객체일 경우, 함수 내에서 parameter 값이 변할 때 새로운 value 객체를 참조하지만,
# argument a 가 mutable 객체일 경우 (list, set, dictionary), argument 와 parameter 가 동일한 mutable 객체를 참조하므로 parameter 값을 바꾸면 argument 값도 변함
# mutable 객체를 argument로 쓰되, parameter 때문에 변경되는 일을 막고 싶으면, deepcopy 를 통해 복사된 값을 argument로 사용해야 함.

# 함수 안에서 생성되는 변수는 local variable 로 함수 밖에서 참조 불가
# global 을 통해 전역변수화 가능

# def classify_var():
#    global globalS
#    globalS = "I like only this!" # 함수 안에서 전역 변수의 값을 수정
#    print(globalS) # I like only this! 수정된 전역 변수 globalS의 값 출력
#
# globalS = "I like all everything!" # 전역 변수 생성
# print(globalS) # I like all everything! 전역변수 globalS의 값을 출력
# classify_var()
# print(globalS) # I like only this! 함수에서 수정된 전역 변수 globalS 값 출력

# 모듈(module) - 함수나 변수들을 모아 놓은 파일
# 라이브러리 > module

# import 모듈이름 (as m) # 모듈 내 모든 함수 사용가능. 호출 시 형식: 모듈이름(m).함수명()
# from 모듈이름 import * # 모듈 내 모든 함수 사용가능. 호출 시 형식: 함수명()
# from 모듈이름 import 모듈함수1, 모듈함수2 # 지정된 함수만 사용가능. 호출 시 형식: 모듈 함수명()