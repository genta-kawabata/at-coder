# -*- coding: utf-8 -*-

from unittest import TestCase

from e.main import get_answer


class Test(TestCase):

    def test_get_answer(self):
        N, S, K = 10000, 6, 14

        self.assertEqual(
            3571,
            get_answer(N, S, K)
        )
