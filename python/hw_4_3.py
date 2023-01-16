sample = "abcABCdEFaBCDeFAbC"

print("abc 문자열 : %d 인덱스, %d 번 존재" % (sample.lower().find("abc"), sample.lower().count("abc")))
print("def 문자열 : %d 인덱스, %d 번 존재" % (sample.lower().find("def"), sample.lower().count("def")))