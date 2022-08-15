# -*- coding: utf-8 -*-

from unittest import TestCase
import random as rd

# import tests.utils as utils
# import utils

import abc182.a.main as a
import abc182.b.main as b
import abc182.c.main as c
import abc182.d.main as d
import abc182.e.main as e
import abc182.f.main as f


class Test_abc182_c(TestCase):

    def test_get_answer_1(self):
        N = "35"

        self.assertEqual(1, c.get_answer(N))

    def test_get_answer_2(self):
        N = "369"

        self.assertEqual(0, c.get_answer(N))

    def test_get_answer_3(self):
        N = "6227384"

        self.assertEqual(1, c.get_answer(N))


    def test_get_answer_4(self):
        N = "11"

        self.assertEqual(-1, c.get_answer(N))

    def test_get_answer_big(self):
        N = str(55563070497907260)
        # 途中でreturnがあるから、そこをコメントアウトして速度計測すること
        ans = c.get_answer(N)
        self.assertTrue(True)
