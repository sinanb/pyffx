import unittest

from pyffx.codecs import String, Integer


class StringTests(unittest.TestCase):
    def test_encrypt(self):
        s = String("foo", "abc")
        self.assertRaises(ValueError, s.encrypt, "abx")
        self.assertEqual(s.encrypt("cba"), "abb")
        self.assertEqual(s.decrypt(s.encrypt("ccc")), "ccc")


class IntegerTests(unittest.TestCase):
    def test_encrypt(self):
        d = Integer("foo", length=2)
        for i in range(100):
            self.assertEqual(d.decrypt(d.encrypt(i)), i)
        hist = set()
        for i in range(100):
            hist.add(d.encrypt(i))
        self.assertEqual(hist, set(range(100)))

    def test_encrypt_big_number(self):
        d = Integer("foo", length=200)
        self.assertEqual(d.decrypt(d.encrypt(1)), 1)