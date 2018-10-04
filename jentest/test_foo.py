#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = 'Rohit Choramle'


import unittest
from foo import sum


class FooTestCase(unittest.TestCase):
    def test_sum1(self):
        self.assertEqual(sum(3,4), 7)

    def test_sum2(self):
        self.assertEqual(sum(-3,-4), -7)

    def test_sum3(self):
        self.assertEqual(sum(0, -2), -2)

    def test_sum4(self):
        self.assertEqual(sum(1,3), 4)

    def test_sum5(self):
        self.assertEqual(sum(0,0), 0)

if __name__ == "__main__":
    unittest.main()
