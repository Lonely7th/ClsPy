#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'JN Zhang'
__mtime__ = '2018/9/13 0013'
"""


class RiskBean(object):
    def __init__(self, min_risk, max_risk, probability):
        self.min_risk = min_risk
        self.max_risk = max_risk
        self.probability = probability
