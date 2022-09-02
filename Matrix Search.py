"""
@user: Asadbek Muxtorov
MatrixSearch

@problem: Given a two-dimensional integer matrix, where every row and column is sorted in ascending order, find the kth (0-indexed) smallest number.

@link: https://binarysearch.com/problems/Matrix-Search

"""


def solve(matrix, k):
    matrix_items = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            matrix_items.append(matrix[i][j])

    def bubble_sort(matrix_items: list[int]) -> list[int]:
        for _ in range(len(matrix_items) - 1):
            for i in range(len(matrix_items) - 1):
                if matrix_items[i] > matrix_items[i + 1]:
                    matrix_items[i], matrix_items[i + 1] = matrix_items[i + 1], matrix_items[i]
        return matrix_items

    return bubble_sort(matrix_items)[k]

print(solve(matrix,k))