#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'usingiter' function below.
#
# The function is expected to return a TUPLE.
# The function accepts following parameters:
#  1. TUPLE tupb
#
import itertools
import operator


def performIterator(tuplevalues):
    main_list = []
    list1 = []
    temp = 0
    for item in itertools.cycle(tuplevalues[0]):
        if temp >= len(tuplevalues[0]):
            break
        else:
            list1.append(item)
            temp += 1
    main_list.append(tuple(list1))

    main_list.append(tuple(list(itertools.repeat(tuplevalues[1][0], len(tuplevalues[1])))))

    main_list.append(tuple(list(itertools.accumulate(tuplevalues[2], operator.add))))

    main_list.append(tuple(list(itertools.chain(tuplevalues[0], tuplevalues[1], tuplevalues[2], tuplevalues[3]))))

    main_list.append(tuple(list(itertools.filterfalse(lambda x: x % 2 == 0, list(itertools.chain(tuplevalues[0], tuplevalues[1], tuplevalues[2], tuplevalues[3]))))))

    return tuple(main_list)


if __name__ == '__main__':

    length = int(input().strip())

    qw1 = []
    for i in range(4):
        qw2 = []
        for _ in range(length):
            qw2_item = int(input().strip())
            qw2.append(qw2_item)
        qw1.append(tuple(qw2))
    tupb = tuple(qw1)

    q = performIterator(tupb)
    print(q)
