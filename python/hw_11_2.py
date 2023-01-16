def countAlpha(x):

    dic = {}
    for i in x:
        if(i != ' '):
            if(dic.get(i) is None):
                dic[i] = 1
            else:
                dic[i] = dic[i] + 1

    return dic

str = input('문자열 입력 : ')
str = str.lower()
for i in countAlpha(str).items():
    print(i[0], ":", i[1])
