#!/usr/bin/python3
""" N queens Backtracking solution. """
import sys


def check(r, c, grid, n):
    # Check vertical (up and down)
    for i in range(1, n):
        if (r - i >= 0 and grid[r - i][c] == 1) or \
                (r + i < n and grid[r + i][c] == 1):
            return False

    # Check horizontal (left and right)
    for i in range(1, n):
        if (c - i >= 0 and grid[r][c - i] == 1) or \
                (c + i < n and grid[r][c + i] == 1):
            return False

    # Check diagonals
    for i in range(1, n):
        if (r - i >= 0 and c - i >= 0 and grid[r - i][c - i] == 1) or \
           (r - i >= 0 and c + i < n and grid[r - i][c + i] == 1) or \
           (r + i < n and c - i >= 0 and grid[r + i][c - i] == 1) or \
           (r + i < n and c + i < n and grid[r + i][c + i] == 1):
            return False

    # If no conflicts, return true
    return True


def add_ans(ans, columns):
    list_ = []
    row = 0
    for i in columns:
        curr = [row, i]
        list_.append(curr)
        row += 1

    ans.append(list_)


def backtrack(r, n, grid, ans, columns):
    if r == n:
        add_ans(ans, columns)
        return

    for i in range(n):
        grid[r][i] = 1
        if check(r, i, grid, n):
            columns.append(i)
            backtrack(r + 1, n, grid, ans, columns)
            columns.pop()
        grid[r][i] = 0


def solve(n):
    ans = []
    columns = []
    grid = [[0] * n for _ in range(n)]

    backtrack(0, n, grid, ans, columns)
    for i in ans:
        print(i)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    solve(n)
