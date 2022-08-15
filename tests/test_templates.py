import random
from templates.prime_number import is_prime_number
from unittest import TestCase

import utils as ut
from templates.base_number import *
from templates.combination import *
from templates.cumulative_sum import *
from templates.search import *
from templates.mod import *


class TestPrimeNumber(TestCase):

    def test_prime_number(self):
        l_prime_no = []
        for i in range(2, 100, 1):
            if is_prime_number(i):
                l_prime_no.append(i)
        
        self.assertEqual(
            [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97],
            l_prime_no
        )


class TestMod(TestCase):

    def test_mod_inv_1(self):
        a = 1
        mod = 13
        expect = 1
        self.assertEqual(expect, mod_inv(a, mod))

    def test_mod_inv_2(self):
        a = 2
        mod = 13
        expect = 7
        self.assertEqual(expect, mod_inv(a, mod))

    def test_mod_inv_3(self):
        a = 3
        mod = 13
        expect = 9
        self.assertEqual(expect, mod_inv(a, mod))

    def test_mod_inv_4(self):
        a = 4
        mod = 13
        expect = 10
        self.assertEqual(expect, mod_inv(a, mod))

    def test_mod_inv_5(self):
        a = 5
        mod = 13
        expect = 8
        self.assertEqual(expect, mod_inv(a, mod))

    def test_mod_pow_2_3(self):
        a, n = 2, 3
        mod = int(1e9) + 7
        expect = 8
        self.assertEqual(expect, mod_pow(a, n, mod))

    def test_mod_pow_3_5(self):
        a, n = 3, 5
        mod = int(1e9) + 7
        expect = 243
        self.assertEqual(expect, mod_pow(a, n, mod))

    def test_mod_pow_3_45(self):
        a, n = 3, 45
        mod = int(1e9) + 7
        expect = 2954312706550833698643 % mod
        self.assertEqual(expect, mod_pow(a, n, mod))


class TestBinarySearch(TestCase):

    def test_int_no_dupl(self):
        arr = [2, 5, 8, 9, 10]
        self.assertEqual(2, binary_meguru(8, arr))

    def test_int_with_dupl(self):
        arr = [2, 5, 8, 8, 9, 10]
        self.assertEqual(2, binary_meguru(8, arr))

    def test_str_no_dupl(self):
        arr = ["a", "k", "l", "p", "r", "w"]
        self.assertEqual(2, binary_meguru("l", arr))

    def test_str_with_dupl(self):
        arr = ["a", "k", "l", "p", "r", "r", "w"]
        self.assertEqual(4, binary_meguru("r", arr))

    def test_str_not_include(self):
        arr = ["a", "k", "l", "p", "r", "r", "w"]
        self.assertEqual(-1, binary_meguru("o", arr))
    
    def test_int_any(self):
        arr = [0, 0, 4, 5, 5, 7, 7, 7, 9, 9]
        self.assertEqual(0, binary_meguru(0, arr))

    def test_int_random(self):
        num_test = 10
        N = pow(10, 1)
        # N = 6
        rand_range = (0, 3)

        timer = ut.MyTimer()
        for i in range(num_test):
            # print(f"### test {i}/{num_test} ###")
            key = random.randrange(rand_range[0], rand_range[1], 1)

            # timer.start()
            arr = [random.randrange(rand_range[0], rand_range[1], 1) for _ in range(N)]
            # print(f"time make arr = {timer.stop()}")

            # ソート
            # timer.start()
            arr.sort()
            # print(f"time sort = {timer.stop()}")

            # python 標準の index    
            py_index = -1
            time = -1
            if not key in arr:
                timer.start()
                py_index = -1
                time = timer.stop()
            else:
                timer.start()
                py_index = arr.index(key)
                time = timer.stop()
            # print(f"time py index = {time}")

            # 逐次探索
            timer.start()
            seq_actual = sequential(key, arr)
            # print(f"time seq = {timer.stop()}")
            # print(f"(py_index, seq) = ({py_index}, {seq_actual})")
            with self.subTest(name=f"test seq {i}/{num_test}", key=key, arr=arr):
                self.assertEqual(py_index, seq_actual)

            # 二分探索
            timer.start()
            bin_actual = binary_meguru(key, arr)
            # print(f"time bin = {timer.stop()}")
            # print(f"(py_index, act) = ({py_index}, {bin_actual})")
            with self.subTest(name=f"test bin {i}/{num_test}", key=key, arr=arr):
                self.assertEqual(py_index, seq_actual)
                self.assertEqual(py_index, bin_actual)

            # print("")


class TestCombination(TestCase):

    def test_11_1(self):
        n = 11
        m = 1
        self.assertEqual(11, combination(n, m))

    def test_11_11(self):
        n = 11
        m = 11
        self.assertEqual(1, combination(n, m))

    def test_199_11(self):
        n = 199
        m = 11
        self.assertEqual(366461620334848584, combination(n, m))


class TestCumulativeSum(TestCase):

    def test_get_cm_list_3(self):
        L_A = [1, 2, 3]
        cs_list = get_cumulative_sum_list(L_A)
        self.assertEqual([0, 1, 3, 6], cs_list)

    def test_get_cm_list_5(self):
        L_A = [-1, -3, 1, -2, 3]
        cs_list = get_cumulative_sum_list(L_A)
        self.assertEqual([0, -1, -4, -3, -5, -2], cs_list)

    def test_get_sum_3(self):
        L_A = [1, 2, 3]
        cs_list = get_cumulative_sum_list(L_A)

        start = 0
        stop = 2
        self.assertEqual(3, get_sum_from_cum_sum_list(cs_list, start, stop))


class TestBaseNumber(TestCase):

    def test_base_2_to_10_22(self):
        self.assertEqual(3, base_n_to_dec("11", 2))

    def test_base_3_to_10_22(self):
        self.assertEqual(8, base_n_to_dec("22", 3))

    def test_dec_to_bin_3_3(self):
        self.assertEqual([0, 1, 1], dec_to_bin(3, 3))

    def test_dec_to_bin_3_4(self):
        self.assertEqual([0, 0, 1, 1], dec_to_bin(3, 4))
