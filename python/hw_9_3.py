A = [4, 8, 2, 3, 4, 2]
B = [7, 2, 5, 2, 3, 6, 5]

A  = list(set(A))
B  = list(set(B))

A.sort()
B.sort()

print([i for i in A for x in B if i == x])