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
# Time marks HAVE TO BE writed in the ascending order.
# ==================================================================== #
# ==================================================================== #
TIME_MARKS = []
for i in range (23):
    TIME_MARKS.append("{}:00:00".format(i))

#TIME_MARKS = ["12:00:00", "18:00:00", "00:00:00", "06:00:00"]
# ==================================================================== #
# ==================================================================== #


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
print("Next time mark:\t{}".format(next_time_mark))

while True:
    time_now = datetime.datetime.now()
    sleep((next_time_mark - time_now).total_seconds())
# ==================================================================== #
# Here will be code to execute. Paste it into the " " brackets.
# Then uncomment the string with the command and comment the other one.
# ==================================================================== #
#    sys.os("")
    print("2 + 2  = 4", datetime.datetime.now())
# ==================================================================== #
    if n == len(TIME_MARKS_DATETIME_FORMAT) - 1:
        n = 0
    else: n += 1
    if time_now > TIME_MARKS_DATETIME_FORMAT[n]:
        for datetime_item in TIME_MARKS_DATETIME_FORMAT:
            datetime_item += datetime.timedelta(days=1)
            
    next_time_mark = TIME_MARKS_DATETIME_FORMAT[n]
    print("Next time mark:\t{}".format(next_time_mark))
        
        
        
        
        
        
        