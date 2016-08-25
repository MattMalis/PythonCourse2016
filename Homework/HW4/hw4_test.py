import unittest
import random
from hw4_sorts_mm import bubbleSort, mergeSort

class hw4_tests(unittest.TestCase):

	def test_random_100(self):
		for j in range(100):
			randoms = []
			for i in range(100):
				randoms.append(random.random())
			tim_sorted = sorted(randoms)
			bub_sorted = bubbleSort(len(randoms), randoms, 0, False)
			merge_sorted = mergeSort(len(randoms), randoms, False)
			self.assertEqual(bub_sorted, merge_sorted)
			self.assertEqual(bub_sorted, tim_sorted)

if __name__ == '__main__':
  unittest.main()
