# number = {1:25, 2:30, 3:27}
# number[key] 로 조회
# D1 = dict([(1,'a'),(2,'b')]) --> dict() 함수를 통해 list,tuple,set 값을 dictionary 화 {1: 'a', 2: 'b'}

# len(D) D의 원소 개수를 반환
# sorted(D) D의 key를 정렬한 리스트 반환. D는 불변이고 오름차순 또는 내림차순으로 정렬 가능. 예) sorted(D, reverse=True)
# list(D) D의 key들을 리스트로 변환하여 반환
# set(D) D의 key들을 집합으로 변환하여 반환
# tuple(D) D의 key들을 튜플로 변환하여 반환
# D.clear( ) D의 모든 원소를 삭제. D = { }가 됨
# D.items( ) key와 value의 쌍을 튜플로 묶은 값을 dict_items 객체로 반환. 튜플 (key, value)를 원소로 하는 리스트를 만들거나 (key, value)가 필요한 반복문에서 사용
# D.keys() 딕셔너리 D의 Key만을 모아서 dict_keys객체로 반환
# D.values( ) value로 구성된 dict_values객체를 반환
# D.get(key) key에 대한 value 값 반환. 존재하지 않는 key이면 d 반환, d가 주어지지 않았으면 None 반환
# D.pop(key) key에 대한 value 반환하고 해당 원소를 삭제. 존재하지 않는 key이면 d 반환, d가 주어지지 않았으면 KeyError
# D.copy( ) D를 복사하여 반환 (shallow copy).
# D.update(other) 존재하는 key이면 value를 갱신, 없으면 쌍을 추가. 예) D.update([(‘a’,2),(‘b’,3)]) #D에 없으면 (‘a’,2)와 (‘b’,3)를 추가. 
# key in D dictionary 내에서 key 값이 있는 지 확인 가능 (value 값 불가)

number = {1:25, 2:30, 3:27}
print(number.pop(2))