sample = "Good words cost nothing"
word = input("찾는 단어 입력 : ")

print("%s 문장에서는 %s 단어가 %d 번 있습니다." % (sample, word, sample.lower().count(word)))