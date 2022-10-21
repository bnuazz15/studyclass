import math

x = 10
print(x, type(x))
print()
print("5의 루트 값은: {:.5f}".format(math.sqrt(5)))
print()
str = 'hello'
print(str[::2])
print(str[::-1])
print(str[:2:][::-1])
print(str[2::])
print()
korean_score = 80.3
english_score = 95.7
math_score = 73.2
avg = (korean_score + english_score + math_score) / 3
print('{:8.2f}'.format(korean_score))
print('{:8.2f}'.format(english_score))
print('{:8.2f}'.format(math_score))
print('{:10.4f}'.format(avg))
print()
str2 = 'These_functions_cannot_be_used_with_complex_numbers.'
print(str2)
str2 = str2.replace('_', ' ')
print(str2)
print("a는 {}번 나왔다.".format(str2.count('a')))
print("e는 {}번 나왔다.".format(str2.count('e')))
print("u는 {}번 나왔다.".format(str2.count('u')))
print("space는 {}번 나왔다.".format(str2.count(' ')))
print("모두 대문자로 바꾸면: {}".format(str2.upper()))