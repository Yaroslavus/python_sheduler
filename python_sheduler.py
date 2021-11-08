#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  7 03:41:59 2021

@author: yaroslav
"""

import sys
import datetime
from time import sleep
# ==================================================================== #
# Please, fill the list of time marks with strings in following format:
# Time mark = "hh:mm:ss"
# Time marks HAVE TO BE recorded in the ascending order.
# ==================================================================== #

TIME_MARKS = ["12:00:00", "18:00:00", "00:00:00", "06:00:00"]

TIME_MARKS_DATETIME_FORMAT = []
for time_mark in TIME_MARKS:
    h, m, s = [int(x) for x in time_mark.split(":")]
    TIME_MARKS_DATETIME_FORMAT.append(datetime.datetime.combine(
            datetime.date.today(), datetime.time(hour=h, minute=m, second=s)))

next_time_mark = TIME_MARKS_DATETIME_FORMAT[0]
n = 0
time_now = datetime.datetime.now()
for i in range(len(TIME_MARKS_DATETIME_FORMAT)-1):
    if (TIME_MARKS_DATETIME_FORMAT[i] < time_now) and (TIME_MARKS_DATETIME_FORMAT[i+1] > time_now):
        next_time_mark = TIME_MARKS_DATETIME_FORMAT[i+1]
        n = i+1

while True:
    time_now = datetime.datetime.now()
    if time_now > TIME_MARKS_DATETIME_FORMAT[n]:
        for i in range(len(TIME_MARKS_DATETIME_FORMAT)):
            TIME_MARKS_DATETIME_FORMAT[i] += datetime.timedelta(days=1)
    next_time_mark = TIME_MARKS_DATETIME_FORMAT[n]
    sleep((next_time_mark - time_now).total_seconds())
# ==================================================================== #
# Here will be command to execute. Paste it into the " " brackets
# in the 46 string. Then uncomment the string - delete the "#" symbol.
# ==================================================================== #
#    sys.os("")
# ==================================================================== #
    if n == len(TIME_MARKS_DATETIME_FORMAT) - 1:
        n = 0
    else: n += 1

