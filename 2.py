#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import date
import sys

if __name__ == '__main__':
    nums_1 = {3: 'three', 2: 'two', 1: 'one'}
    nums_2 = dict(map(reversed, nums_1.items()))

    print(nums_1)
    print(nums_2)
