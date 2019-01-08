
import os
import sys
import unittest
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(CURRENT_DIR, "tests"))
import test_caculator
import test_str_cmp
from test_caculator import CaculatorTest
from test_str_cmp import StrCmpTest


def method1():
    suites = unittest.TestLoader().discover("./tests", pattern="test*.py")
    print("test cases:{}".format(suites.countTestCases()))
    unittest.TextTestRunner().run(suites)


def method2():
    suite = unittest.TestLoader().loadTestsFromTestCase(CaculatorTest)
    suite2 = unittest.TestLoader().loadTestsFromTestCase(StrCmpTest)
    suites = unittest.TestSuite((suite, suite2))
    print("test cases:{}".format(suites.countTestCases()))
    excutor = unittest.TextTestRunner()
    excutor.run(suites)


def method3():
    suites = unittest.TestSuite()
    suites.addTests((CaculatorTest("test_add"), CaculatorTest("test_minus")))
    print("test cases:{}".format(suites.countTestCases()))
    excutor = unittest.TextTestRunner()
    excutor.run(suites)


def method4():
    suites = unittest.TestSuite()
    suites.addTest(CaculatorTest("test_add"))
    suites.addTest(CaculatorTest("test_minus"))
    print("test cases:{}".format(suites.countTestCases()))
    excutor = unittest.TextTestRunner()
    excutor.run(suites)


def method5():
    suite = unittest.TestLoader().loadTestsFromModule(test_caculator)
    suite2 = unittest.TestLoader().loadTestsFromModule(test_str_cmp)
    suites = unittest.TestSuite((suite, suite2))
    print("test cases:{}".format(suites.countTestCases()))
    excutor = unittest.TextTestRunner()
    excutor.run(suites)

if __name__ == "__main__":
    method1()
    method2()
    method3()
    method4()
    method5()
