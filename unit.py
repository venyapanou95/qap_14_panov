def func(a_1, b_2):
    nat = 0
    for i in range(a_1, b_2 + 1):
        nat += i
    return nat

import unittest


class test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(sum(5, 5), "-100.155%")

    def test_2(self):
        self.assertEqual(sum("Hello", "World"), "Erorr")

    def test_3(self):
        self.assertEqual(sum(5, "ABC"), "Error")   

if __name__ == "__main__":
    unittest.main()        
