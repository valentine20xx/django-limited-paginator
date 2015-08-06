from limited_paginator.limitpaging import LimitedPaginator
import unittest


class Test(unittest.TestCase):
    def setUp(self):
        pass

    def test_add_by_one(self):
        def test_case(array, amount, per_page, page_num, r_array, r_has_last, r_has_first):
            """
            Simple testcase

            :param array:
            :param amount:
            :param per_page:
            :param page_num:
            :param r_array:
            :param r_has_last:-
            :param r_has_first:
            :return: no return, no tomorrow, just nothing
            """
            paginator = LimitedPaginator(array, amount=amount, per_page=per_page)
            page = paginator.page(page_num)
            self.assertEqual(page.main_range, r_array)
            self.assertEqual(page.has_last, r_has_last)
            self.assertEqual(page.has_first, r_has_first)

        test_case(range(0, 0), 5, 1, 1, [], False, False)
        test_case(range(0, 1), 5, 1, 1, [1], False, False)
        test_case(range(0, 2), 5, 1, 1, [1, 2], False, False)

        test_case(range(0, 3), 5, 1, 1, [1, 2, 3], False, False)
        test_case(range(0, 3), 5, 1, 2, [1, 2, 3], False, False)
        test_case(range(0, 3), 5, 1, 3, [1, 2, 3], False, False)

        test_case(range(0, 4), 5, 1, 1, [1, 2, 3, 4], False, False)
        test_case(range(0, 5), 5, 1, 1, [1, 2, 3, 4, 5], False, False)
        test_case(range(0, 6), 5, 1, 1, [1, 2, 3, 4, 5], True, False)
        test_case(range(0, 6), 5, 1, 6, [2, 3, 4, 5, 6], False, True)
        test_case(range(0, 7), 5, 1, 4, [2, 3, 4, 5, 6], True, True)


if __name__ == '__main__':
    unittest.main()

    # class Test(unittest.TestCase):
    # def test1(self):
    # assert(True == True)
    #
    # if __name__ == "__main__":
    # suite = unittest.TestSuite()
    # suite.addTest(Test('test1'))
    # unittest.TextTestRunner().run(suite)