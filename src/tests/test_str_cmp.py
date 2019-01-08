
from unittest import TestCase
from src.application.str_cmp import StrCmp


class StrCmpTest(TestCase):

    def setUp(self):
        self.str_cmp_inst = StrCmp()

    def tearDown(self):
        pass

    def test_cmp(self):
        str1 = "abcd"
        str2 = "abcd"
        self.assertEqual(self.str_cmp_inst.cmp(str1, str2), True)

    def test_cmp2(self):
        str1 = "abcd"
        str2 = "abc"
        self.assertEqual(self.str_cmp_inst.cmp(str1, str2), False)
