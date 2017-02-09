#!/usr/bin/env python
# -*- coding: utf-8 -*-

__title__ = ''
__author__ = 'zhangjingjun'
__mtime__ = '2017/2/9'

import pytest

def test_main():
	assert 5 != 5
if __name__ == '__main__':
	pytest.main('-q test_1.py')