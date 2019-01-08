
from src.application.caculator import Caculator
import unittest


class CaculatorTest(unittest.TestCase):

    def setUp(self):
        self.caculator_inst = Caculator()

    def tearDown(self):
        pass

    def test_add(self):
        result = self.caculator_inst.add(2, 1)
        self.assertEqual(result, 3)

    def test_minus(self):
        result = self.caculator_inst.minus(2, 1)
        self.assertEqual(result, 1)

    def test_multiply(self):
        result = self.caculator_inst.multiply(2, 1)
        self.assertEqual(result, 2)

    def test_devide(self):
        result = self.caculator_inst.devide(2, 1)
        self.assertEqual(result, 2)

if __name__ == "__main__":
    unittest.main(verbosity=2)
