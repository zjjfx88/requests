#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'zhangjingjun'
__mtime__ = '2017/2/9'
# ----------Dragon be here!----------
              ┏━┓      ┏━┓
            ┏━┛ ┻━━━━━━┛ ┻━━┓
            ┃       ━       ┃
            ┃  ━┳━┛   ┗━┳━  ┃
            ┃       ┻       ┃
            ┗━━━┓      ┏━━━━┛
                ┃      ┃神兽保佑
                ┃      ┃永无BUG！
                ┃      ┗━━━━━━━━━┓
                ┃                ┣━┓
                ┃                ┏━┛
                ┗━━┓ ┓ ┏━━━┳━┓ ┏━┛
                   ┃ ┫ ┫   ┃ ┫ ┫
                   ┗━┻━┛   ┗━┻━┛
"""
import pytest
import random

def f(num):
	y = num%2
	return y

def test_f():
	num = random.randint(0, 100)
	assert f(num)==1

if __name__ == '__main__':
	pytest.main('-q test_2.py')
