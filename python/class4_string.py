# str 은 튜플 형태로 값 변경 불가능

# str을 선언하는 방법
# 'str', "str", '''str''', """"str""" (str가 여러 줄일 경우 존재할 경우 유용)
# ' " 를 str 에 표함하고 싶을 때 escape 문자열 사용 가능
str = 'hel\'lo'
print(str)

str = """hel
lo"""
print(str)

# 한 줄 짜리 string 을 여러줄에 걸쳐 \ 를 이용해서 작성 가능

# 문자열 연결 +
# 문자열 반복 * n
print(("hell" + "o ") * 3)

# 해당 문자열이 문자열에 있는지 in (Boolean)
print("ell" in "hello")

# string 길이 len(str)
str = 'hi python'
print(len(str))

# index str[index]
# index 가 음수인 경우 뒤에서부터 index
print(str[-2])

# slicing : 문자 일부를 잘라서 return
# str[start : end : step] --> start <= index < end, step 간격
# step 을 음수로 하면 문자열을 거꾸로 return 
# default : start = 0, end = len(str), step = 1
print(str[::-1])

# formating
# % 를 활용한 formating
# %s, %c, %d, %f, %o, %x, %X, %% (% 표시)
# %.nf --> 소숫점 n 자리까지 반올림하여 표시
# %nd --> 총 n 자리로 표현 (오른쪽 정렬). 데이터 총 길이가 n 자리수를 넘을 시, 전부 표시. %0nd --> 총 n 자리로 표현하되 남는 자리를 0으로 채움

str = '%s eats %e apples.' %("Tom", 15)
print(str)

# .foramt()
# format() 의 순서대로 {} 에 입력 및 index 활용하여 사용 가능. 또한, 변수 명을 명시해서 사용 가능
# {:n} 은 n 자리만큼 폭 잡고 default 로 string 의 경우 왼쪽 정렬, 숫자는 오른쪽 정렬. {:>n}, {:<n} 로 정렬 방향 설정 가능
print("{1:3.2f}!!".format(3.1452, 414.1232))
print("{str:>10} {score:10}!!".format(str = 'score', score = 100))

# split()
# default 는 띄어쓰기, 구분자 입력 가능
# return data type은 list
# split() 하여 바로 변수에 나눠 담을 수 있음. 단, 변수 개수는 정확해야함. ValueError: not enough(much) values to unpack (expected 4, got 3) 에러 발생
str_split = 'life is too/short'
print(str_split.split())
print(str_split.split('/'))
str1, str2, str3 = str_split.split()
print(str1, str2, str3)

# lower() --> 모두 소문자로 string return
# upper() --> 모두 대문자로 string return
# swapcase() --> 대소문자 서로 바꿔서 string return
# islower() --> string 내 모든 문자가 소문자면, True return
# isupper() --> string 내 모든 문자가 대문자면, True return
# isalpha() --> string 내 모든 문자가 영어, 한글로만 되어 있으면 True return (띄어쓰기 및 특수 문자도 X)
# isnumeric() --> string 내 모든 문자가 숫자라면 True return
# isalnum() --> string 내 모든 문자가 숫자, 영어, 한글로만 되어있으면 True return
# title() --> 각 단어의 첫번째 문자만 대문자로 변환하여 string return. (단어의 기준은 알파벳으로 시작할 때. 따라서, 꼭 seperator 가 space가 아니여도 됨)
# replace(str1, str2) --> 문자열 내 str1을 str2 로 변환한 상태로 string return
# startswith(str) --> str 로 시작하면 True return
# endswith(str) --> str 로 끝나면 True return
# find(str) --> str 이 처음 발견되는 index 위치 return. 없으면 -1 return
# rfind(str) --> str 이 뒤에서 처음 발견되는 index 위치 return. 없으면 -1 return
# count(str) --> str 이 string 내에 몇 개 존재하는 지 개수 return
# strip() --> string 양 쪽에 있는 공백 제거하여 string return. lstrip()은 왼쪽만, rstrip()은 오른쪽만 제거
alpha = "hi py썬1py"
print(alpha.count('py'))