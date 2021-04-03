#!/bin/python3


def payment_pairs(payments):
    n = 0
    for i in range(len(payments)):
        for j in range(i + 1, len(payments)):
            if (payments[i] + payments[j]) % 100 == 0:
                n = n + 1
    return n


payment_pairs([50, 60, 150, 50, 40])
