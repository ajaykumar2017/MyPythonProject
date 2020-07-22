#!/bin/python3

import math
import os
import random
import re
import sys
import calendar
import datetime
#
# Complete the 'calen' function below.
#
# The function accepts TUPLE datetuple as parameter.
#

def usingcalendar(datetuple):
    is_leap = calendar.isleap(datetuple[0])
    month = 2
    print(calendar.month(datetuple[0], month))

    obj = calendar.Calendar()
    day_list = []
    for day in obj.itermonthdates(datetuple[0], month):
        day_list.append(day)
    print(day_list[-7:])

    day_name_list = []
    for day in day_list:
        day_name_list.append(day.strftime("%A"))
    print(day_name_list)


if __name__ == '__main__':
    qw1 = []

    for _ in range(3):
        qw1_item = int(input().strip())
        qw1.append(qw1_item)

    tup = tuple(qw1)

    usingcalendar(tup)
