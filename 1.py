#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import date
import sys

if __name__ == '__main__':
    school = {'1a': 16, '1б': 22, '2б': 29, '6а': 30, '7в': 25,
              '10б': 26, '11a': 33, '11б': 26}
    print(school)

    school['10б'] += 1
    school['6в'] = 10
    school.pop('11б')

    s = 0
    for item in school.values():
        s += item
    print(school)
    print("Количество учеников во всех классах", s)
