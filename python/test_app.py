import unittest
from app import App

class TestReadInput(unittest.TestCase):
    def testCashboxAmount(self):
        a = App()
        a.cashboxBal = 200000
        a.emps = [
            (1, 1, 5000, 5000, 300),
            (2, 1, 9000, 0, 1000),
            (3, 1, 20000, -400, 0),
            (4, 2, 10000, 0, 100),
            (5, 3, 110000, 0, 0)
        ]
        a.process()
        self.assertEqual(a.cashbox, 47210.00)
        self.assertEqual(a.cashShort, 0.00)
        print("----")

    def testCashShortAmount(self):
        a = App()
        a.cashboxBal = 100000
        a.emps = [
            (1, 1, 5000, 5000, 300),
            (2, 1, 9000, 0, 1000),
            (3, 1, 20000, -400, 0),
            (4, 2, 10000, 0, 100),
            (5, 3, 110000, 0, 0)
        ]
        a.process()
        self.assertEqual(a.cashbox, 0.00)
        self.assertEqual(a.cashShort, -52790)
        print("----")
