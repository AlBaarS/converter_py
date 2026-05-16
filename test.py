#!/bin/python3

import convert
import unittest

class TestBaseConverObject(unittest.TestCase):

    def test_doubling(self):
        input_number: float = 21
        output_expect: float = 42
        output_test: float = convert.BaseConverter().convert(input_number, "base", "double")
        self.assertEqual(output_expect, output_test)

    # def test_upper(self):
    #     self.assertEqual('foo'.upper(), 'FOO')

    # def test_isupper(self):
    #     self.assertTrue('FOO'.isupper())
    #     self.assertFalse('Foo'.isupper())

    # def test_split(self):
    #     s = 'hello world'
    #     self.assertEqual(s.split(), ['hello', 'world'])
    #     # check that s.split fails when the separator is not a string
    #     with self.assertRaises(TypeError):
    #         s.split(2)

if __name__ == '__main__':
    unittest.main()
