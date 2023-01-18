# 집합 set
# list 를 원소로 가지고 있을 수 X
# 동일한 원소가 존재 X
# set() --> 빈 집합 의미. {} 의 경우 빈 dictionary 이므로 주의
# s = {'a', 123, False}
# s = set([1,2,3,4]) # list 및 tuple 원소 집합으로 변환 --> s = {1,2,3,4}, 문자열도 가능

# A.add(x) 데이터 x를 A의 원소로 추가
# A.clear() A의 모든 원소를 제거. A를 공집합으로 만듬
# B = A.copy() A를 B로 복사(shallow copy)
# A.discard(x) 집합 A에서 원소 x를 제거. 없는 원소를 삭제하려고 할 때에도 에러 발생하지 않음(x ∉ A이면 무시)
# A.remove(x) 집합 A에서 원소 x를 제거. 없는 원소를 삭제하려고 하면 KeyError가 발생(x ∉ A이면 KeyError)
# A.pop( ) 집합 A에서 임의의 원소를 하나 지우고 그 값을 반환(A가 공집합이면 KeyError). 순서가 없기 때문에 임의의 원소 가져옴
# A.isdisjoint(B) A ⋂ B = ∅이면 True
# A.issubset(B) A ⊆ B 이면 True
# A.issuperset(B) A ⊇ B 이면 True
# A.union(B) A ⋃ B를 반환(A | B 와 동일)
# A.update(B) A를 A ⋃ B로 갱신
# A.intersection(B) A ⋂ B를 반환(A & B와 동일)
# A.intersection_update(B) A를 A ⋂ B로 갱신
# A.difference(B) B에는 없고 A에만 있는 원소의 집합 반환. (A – B와 동일)
# A.difference_update(B) A를 A - B로 갱신
# A.symmetric_difference(B) A ⋃ B에는 있으나 A ⋂ B에는 없는 원소의 집합 반환(A ^ B와 동일)
# A.symmetric_difference_update(B) A를 (A ⋃ B) – (A ⋂ B)로 갱신

