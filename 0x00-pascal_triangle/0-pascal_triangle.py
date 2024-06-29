#!/usr/bin/python3
"""
Pascal Triangle
"""


def pascal_triangle(n):
    """pascal_triangle(n): return the pascal triangle of size n.
    """
    triangle = []
    if n > 0:
        for i in range(1, n + 1):
            level = []
            cell = 1
            for j in range(1, i + 1):
                level.append(cell)
                cell = cell * (i - j) // j
            triangle.append(level)
    return triangle
