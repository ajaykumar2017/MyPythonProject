#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'strmethod' function below.
#
# The function accepts following parameters:
#  1. STRING para
#  2. STRING spch1
#  3. STRING spch2
#  4. LIST li1
#  5. STRING strf
#

def stringmethod(para, special1, special2, list1, strfind):
    # Write your code here
    word1 = ""
    for character in para:
        if character not in special1:
            word1 = word1 + character

    rword2 = word1[0:70]
    print(rword2)

    rword2 = rword2.strip()
    print(rword2 + special2)

    a = True
    for s in list1:
        if s not in para:
            a = False

    if a:
        print("Every string in {list1} were present")
    else:
        print("Every string in {list1} were not present")

    print(word1.split(' ', 20))
    Counter = Counter(word1.split())
    print(Counter.less_common(20))
    print(word1.rindex(strfind))


if __name__ == '__main__':
    para = input()

    spch1 = input()

    spch2 = input()

    qw1_count = int(input().strip())

    qw1 = []

    for _ in range(qw1_count):
        qw1_item = input()
        qw1.append(qw1_item)

    strf = input()

    stringmethod(para, spch1, spch2, qw1, strf)
