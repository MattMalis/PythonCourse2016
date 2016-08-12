import unittest
import lab3_

class lab3_tests(unittest.TestCase):

	def test_shout(self):
		self.assertEqual("WORD", lab3_.shout("word"))
		self.assertEqual("I DON'T KNOW WHAT WE'RE YELLING ABOUT!", lab3_.shout("I don't know what we're yelling about!"))
		with self.assertRaises(Exception):
			lab3_.shout("HELLO!")
	def test_reverse(self):
		self.assertEqual("backwards", lab3_.reverse("sdrawkcab"))
	def test_reversewords(self):
		with self.assertRaises(Exception):
			lab3_.reversewords(-18.8)
		self.assertEqual("third second first", lab3_.reversewords("first second third"))
		self.assertEqual("six equals 2 times 3", lab3_.reversewords(str(4-1) + " times 2 equals six"))
	def test_reversewordletters(self):
		with self.assertRaises(Exception):
			lab3_.reversewords("reverse_this")
		self.assertEqual("siht si a lamron ecnetnes", lab3_.reversewordletters("this is a normal sentence"))
	def test_piglatin(self):
		with self.assertRaises(Exception):
			lab3_.reversewords(100, 100, 20)
		self.assertEqual("et's-lay o-day e-thay ig-pay atin-lay oh-ay eah-yay", lab3_.piglatin("let's do the pig latin oh yeah"))
	

if __name__ == '__main__':
  unittest.main()
