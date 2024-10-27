from typing import List, Tuple


def find_sum(target: int, li: List[int]) -> Tuple[int, int]:
    n = len(li)

    for i in range(n):
        for j in range(i + 1, n):
            if li[i] + li[j] == target:
                return (i, j)

# Time complexity: O(n^2) because we are iterating over all pairs of elements.


def find_sum_fast(target: int, li: List[int]) -> Tuple[int, int]:
    seen = {}
 
    for i, num in enumerate(li):
        complement = target - num
        if complement in seen:
            return (seen[complement], i)
        seen[num] = i

# Time complexity: O(n) because we iterate through the list only once.


assert find_sum(5, [1, 2, 3, 4, 5]) in {(0, 3), (1, 2)}
assert find_sum_fast(5, [1, 2, 3, 4, 5]) in {(0, 3), (1, 2)}

result_1 = find_sum(5, [1, 2, 3, 4, 5])
result_2 = find_sum_fast(5, [1, 2, 3, 4, 5])

print(f"Result of find_sum: {result_1}")
print(f"Result of find_sum_fast: {result_2}")