import unittest

import dict_diff


class TestCase(unittest.TestCase):
    def test_correct(self):
        d = dict_diff.dict_diff(self.a, self.b)
        print d
        self.assertEqual(self.diff, d)


class Test1(TestCase):
    a = 4
    b = 3
    diff = '\x1b[33m3\x1b[39m'


class Test2(TestCase):
    a = {'a': 4}
    b = {'a': 3}
    diff = '{a: \x1b[33m3\x1b[39m}'


class Test3(TestCase):
    a = 4
    b = {'a': 3}
    diff = "\x1b[33m{'a': 3}\x1b[39m"


class Test4(TestCase):
    a = {'a': {'b': {'c': 3}}}
    b = {'a': {'b': {'c': 6}}}
    diff = '{a: {b: {c: \x1b[33m6\x1b[39m}}}'


class Test5(TestCase):
    a = {'a': {'b': {'c': 3}}}
    b = {'a': {'b': {'d': 3}}}
    diff = '{a: {b: \x1b[33md\x1b[39m: 3}}'


class Test6(TestCase):
    a = {'a': {'b': {'c': 3}}}
    b = {'a': {'c': {'b': 3}}}
    diff = '{a: {\x1b[31mb: {c: 3}\x1b[39m, \x1b[32mc: {b: 3}\x1b[39m}}'


if __name__ == '__main__':
    del TestCase
    unittest.main()
