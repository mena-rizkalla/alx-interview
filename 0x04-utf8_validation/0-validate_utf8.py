#!/usr/bin/python3
""" UTF-8 Validation """

def validUTF8(data) -> bool:
    x = 128
    y = 64
    n = 0

    if len(data) == 1 and (data[0] & x) == 0:
        return True

    if len(data) == 1 and (data[0] & x) != 0:
        return False
    for i in range(len(data)):
        if n == 0:
            if (data[i] & x) == 0:
                continue
            while((data[i] & x) != 0):
                data[i] = data[i] << 1
                n = n + 1
            if n == 1 or n >= 5:
                return False
            n = n-1
        else:
            if((data[i] & x) == 0 or (data[i] & y) != 0):
                return False
            n = n - 1
    return n == 0
