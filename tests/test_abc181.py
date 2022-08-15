# -*- coding: utf-8 -*-

from unittest import TestCase
import random as rd

# import tests.utils as utils
# import utils

import abc181.a.main as a
import abc181.b.main as b
import abc181.c.main as c
import abc181.d.main as d
import abc181.e.main as e
import abc181.f.main as f


class Test_abc181_c(TestCase):

    def test_get_answer_big(self):
        N = 100

        L_XY = [[rd.randrange(-1000, 1000, 1), rd.randrange(-1000, 1000, 1)] for _ in range(N)]

        print(c.get_answer(N, L_XY))

        self.assertTrue(True)
