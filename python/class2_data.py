# 정수형 데이터 표현
# 16진수 0x, 0X
# 8진수 0o, 0O
# 2진수 0b, 0B
print(0xFF, 0o77, 0b1111)

# python의 경우 데이터를 모두 object 로 관리
# x가 100을 저장하는 정수형 object를 가리킴
x = 100
y = "hello"

# 변수명은 영어, 숫자, _ 만 가능하며, 숫자로 시작 불가

# type 함수를 통해 data type 확인 가능
print(type(x))

# int(), float(), str() 를 통해 형변환 가능
print(type(str(x)))

# swap 코드
x, y = y, x
print(x, y)