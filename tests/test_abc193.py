# -*- coding: utf-8 -*-

from unittest import TestCase
import random as rd

# import tests.utils as utils
# import utils

import abc193.a.main as a
import abc193.b.main as b
import abc193.c.main as c
import abc193.d.main as d
import abc193.e.main as e
import abc193.f.main as f


class Test_abc193_b(TestCase):

    def test_get_answer_1(self):
        pass


class Test_abc193_c(TestCase):

    def test_get_answer_8(self):
        self.assertEqual(6, c.get_answer(8))

    def test_get_answer_10(self):
        self.assertEqual(7, c.get_answer(10))

    def test_get_answer_10(self):
        self.assertEqual(7, c.get_answer(100))

    def test_get_answer_1e5(self):
        self.assertEqual(99634, c.get_answer(int(1e5)))


    def test_get_answer_1e10(self):
        self.assertEqual(10, c.get_answer(int(1e10)))


class Test_abc193_d(TestCase):

    def test_get_answer_1(self):
        pass
