#!/usr/bin/python3

""" Contains makeChange function"""


def makeChange(coins, total):
    if total <= 0:
        return 0

    # Sort coins in descending order
    coins.sort(reverse=True)
    num_coins = 0
    for coin in coins:
        if total <= 0:
            break
        # Use as many of the current coin as possible
        num_coins += total // coin
        total %= coin

    # If total is not zero, return -1
    if total != 0:
        return -1

    return num_coins
