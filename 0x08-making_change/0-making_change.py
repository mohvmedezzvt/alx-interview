#!/usr/bin/python3
""" Making Change """


def makeChange(coins, total):
    """ Given a pile of coins of different values, determine the fewest number
        of coins needed to meet a given amount total """
    if total <= 0:
        return 0

    coins.sort(reverse=True)
    check, steps = 0, 0

    for coin in coins:
        while check < total:
            check += coin
            steps += 1

        if check == total:
            return steps

        check -= coin
        steps -= 1

    return -1
