import sys
from typing import List


def get_triangle(rows: int) -> List[List[int]]:
    triangle = []

    for i in range(rows):
        row = [1] * (i + 1)

        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)

    return triangle


def print_triangle(triangle: List[List[int]]) -> None:
    for row in triangle:
        print(" ".join(map(str, row)))


try:
    rows = int(input("Please enter the number of rows: "))
    print(f"Number of rows provided: {rows}")
except ValueError:
    print("Please provide a valid integer for the number of rows.")
    sys.exit(1)

if rows < 1:
    print("Number of rows should be at least 1.")
    sys.exit(1)


triangle = get_triangle(rows)
print(f"Generated triangle: {triangle}")
print_triangle(triangle)
