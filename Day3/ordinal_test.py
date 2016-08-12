import unittest
import ordinal

class make_ordinal_test(unittest.TestCase):

	def test_first(self):
		self.assertEqual("1st", ordinal.make_ordinal(1))
		self.assertEqual("31st", ordinal.make_ordinal(31))
	def test_second(self):
		self.assertEqual("2nd", ordinal.make_ordinal(2))
		self.assertEqual("152nd", ordinal.make_ordinal(152))
	def test_third(self):
		self.assertEqual("3rd", ordinal.make_ordinal(3))
	def test_fourth(self):
		self.assertEqual("5th", ordinal.make_ordinal(4))
	def test_type(self):
		self.assertRaises(TypeError, ordinal.make_ordinal("a string") )
		self.assertRaises(TypeError, ordinal.make_ordinal(3.14159) )
		self.assertRaises(CustomException, ordinal.make_ordinal(-3)) 
		
	