#! usr/bin/env python3

import unittest
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from sort import sort_list 

class Test(unittest.TestCase):
    def Test_sort(self):
        lista = [1, 4, 2, 3]
        self.assertEqual(sort_list(lista), [1, 2, 3, 4])

if __name__ == '__main__':
	unittest.main()