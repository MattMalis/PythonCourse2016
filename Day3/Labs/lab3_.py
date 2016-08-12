import string
#write a custom exception, then an inclusive test, then write the code for the following functions:

class CustomException(Exception): # inherits from Exception
  def __init__(self, value):
    self.value = value
  def __str__(self):
    return self.value

def shout(txt):
	if txt.isupper():
		raise CustomException("YOU'RE ALREADY SHOUTING")
	return txt.upper()

def reverse(txt):
	return txt[::-1]
  
def reversewords(txt):
	if not isinstance(txt, str):
		raise CustomException("That's not a string!")
	if (len(str.split(txt))==1):
		raise CustomException("Can't reverse words with only one word")
	return ' '.join(str.split(txt)[::-1])
  
def reversewordletters(txt):
	txt_split = str.split(txt)
	for i in range(0,len(txt_split)):
		txt_split[i]=reverse(txt_split[i])
	return ' '.join(txt_split)
  
def piglatin(txt):
	if not isinstance(txt, str):
		raise CustomException("That's not a string!")
	vowels = {'a','e','i','o','u'}
	words = str.split(txt)
	for w in range(len(words)):
		for i in range(len(words[w])):
			if words[w][i] in vowels:
				first_vowel_index = i
				break
		else:
			first_vowel_index = 0
		words[w] = words[w][first_vowel_index:] + "-" + words[w][:first_vowel_index] + "ay"
	return ' '.join(words)
	
print reversewordletters("one two three four")	
