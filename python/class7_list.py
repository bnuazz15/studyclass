# list = [1, 'A', 3]
# n = len(list) --> 리스트 크기 구하기
# Slicing Rule
# L[ b : e : s ]
# s > 0 ( b < e 이어야 함. 아니면 빈 리스트 생성)
# s < 0 ( b > e 이어야 한다. 아니면 빈 리스트 생성)

# a = [0, 1, 2, 3, 4]
# a[1:3] = [] # a[1], a[2] 제거
# print(a) # [0,3,4]
# del a[:2] # a[0 ~ 1] 제거
# print(a) # [4]

# a = [0, 1, 2, 3, 4]
# a [0:1] = [1] # 교체할떄는 list to list 로 Slicing 으로 교체해야함. 그냥 a[0] = [1] 이렇게 대입하면 리스트가 원소로서 대입되는 것
# a [0:0] = [1,2] # 0번째 자리에 교체 없이 끼워넣기
# a [1::2] = 9 # 불가능
# print(a)

# 리스트 참조 복사
# A = ['ab', 'cd', 'ef']
# B = A # 같은 object를 참조(복사가 아님)
# print(id(A), id(B)) # id 동일(같은 객체를 가리키기 때문)
# B[1] = 10
# print(A, B) # 같은 데이터 값 출력

# 리스트 값 복사 with Slicing
# A = ['ab', 'cd', 'ef']
# B = A[:] # B = A.copy( )
# print(id(A), id(B)) # id가 다름(다른 객체)
# B[2] = 10 
# print(A, B)

# 리스트 값 복사 시에 A의 2번째 원소는 리스트의 주소값을 가지고 있는 거이기에 B에서도 주소값을 복사하게 되어 A, B 둘다 영향 있음
# copy 모듈의 함수 deepcopy( )를 사용하면 리스트의 내부 구조를 모두 복사 가능
# A = ['ab', 'cd', [1,2]]
# B = A[:] # B = A.copy( )
# print(id(A), id(B)) # id가 다름(다른 객체)
# B[0] = 'e' # B의 원소 값만 바뀜
# B[2][0] = 8 # A와 B 모두 값이 바뀜(원소가 리스트인 경우: 문제 발생)
# print(A, B)

# 리스트 연산
# list + list : 리스트들을 연결하여 새로운 리스트로 만듬
# list * n : list의 item들을 n번 반복하여 새로운 list를 만듬

# x.append(a) 데이터 a를 리스트 x의 끝에 추가
# x.extend(L) 리스트 L의 모든 원소를 리스트 x의 마지막에 추가
# x.insert(i, a) a를 리스트 x의 index i에 추가
# x.remove(a) 리스트 x에서 원소 값이 데이터 a인 첫 원소 제거 (반환 값 없음)
# x.pop( ) x의 마지막 원소 제거 및 반환
# x.pop(i) x[i]를 x에서 제거하고 그 값을 반환
# x.clear( ) 리스트 x의 모든 원소를 삭제. 빈 리스트가 됨
# x.index(a) 리스트 x에서 원소 값이 a인 첫 번째 원소의 index를 반환
# x.count(a) 리스트 x에서 a 값과 같은 원소의 개수를 반환
# x.sort( ) x의 원소들을 오름차순으로 정렬. 내림차순으로 정렬하려면 x.sort(reverse=True) 사용
# x.reverse( ) x의 원소들을 역으로 재 배치 (정렬과 다름)
# x.copy( ) a shallow copy of the list (y = x[:]와 동일
# all(x) x의 모든 원소가 True(i.e. != 0)이거나, 또는 x가 빈 리스트이면 True 반환
# any(x) x에 True인(i.e. != 0인) 원소가 한 개라도 있으면 True, 또는 x가 빈 리스트이면 False 반환
# enumerate(x) x의 모든 원소에 대해 튜플 (index, 원소 값)을 얻을 수 있는 enumerate object를 반환. index = 0, 1, 2, …
# len(x) x의 원소 개수를 반환
# list(y) Iterable한 y를 리스트로 변환하여 반환
# max(x) x의 원소 중 최대 값 반환(비교 불가이면 TypeError)
# min(x) x의 원소 중 최소 값 반환(비교 불가이면 TypeError)
# sorted(x) x의 원소를 정렬한 리스트 반환. x는 불변이고 오름차순 또는 내림차순으로 정렬(sorted(x, reverse=True))
# sum(x) x의 원소 합을 반환(더할 수 없으면 TypeError)

# L = ["Jan", "Apr", "Sep"]
# print(list(enumerate(L)))