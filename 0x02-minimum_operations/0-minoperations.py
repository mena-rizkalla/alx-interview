#!/usr/bin/python3
"""
Greedy solution to minOperations
"""


def minOperations(n):
    """ Count the minimum number of operations to reach n. """
    count, operations, clipboard = 1, 0, 0

    while count < n:
        if n % count == 0:
            operations = operations + 2
            clipboard = count
            count = count + clipboard
        else:
            operations = operations + 1
            count = count + clipboard

    return operations
