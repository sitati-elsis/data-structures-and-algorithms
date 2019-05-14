def solution(A):
    # The lookup table will enable us to check if
    # a number is in A in O(1) time
    lookup_table = {}
    for i in A:
        if i > 0:
            lookup_table[i] = True

    for i in range(1, 1000001):
        # `i not in lookup_table` is equivalent to A.index(i) but in O(1) time
        # instead of O(n)
        if i not in lookup_table:
            return i

A = [1, 3, 6, 4, 1, 2]
B = [-1, -3]

print(solution(A))
print(solution(B))
