#!/usr/bin/python3
"""
Rotate 2D Matrix
"""


def rotate_2d_matrix(matrix):
    """rotate two dimension matrix 90 degrees clockwise
    Args:
        matrix (list[[list]]): a matrix
    """
    n = len(matrix)

    for i in range(0, n):
        for j in range(i + 1, n):
            tmp = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = tmp

    for i in range(0, n):
        for j in range(0, int(n / 2)):
            tmp = matrix[i][j]
            matrix[i][j] = matrix[i][n - j - 1]
            matrix[i][n - j - 1] = tmp
