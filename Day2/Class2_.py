#A silly function that prints an integer.

def print_int(int):
	print 'Here is an integer: %s' %int
	
print_int(1)
print_int('b')

import random

#Function that returns the product of random draws from a uniform distribution.
# def random_product(lower,upper):
# 	random1
# 	random2
# 	return random1 * random2
# 	
# print random_product(0,1)

#NameError: global name 'random1' is not defined

#We need to define numbers random1 and random2.
#We need to import the module random.
from random import uniform

def random_product(lower,upper):
	random1=uniform(lower,upper)
	random2=uniform(lower,upper)
	return random1 * random2
	
print random_product(0,1)

#NameError: global name 'uniform' is not defined

#We need to add the module name before the global name.

#import random

def random_product(lower,upper):
	random1=random.uniform(lower,upper)
	random2=random.uniform(lower,upper)
	return random1 * random2
	
print random_product(0,1)

#Alternatively, we can import a particular function.

from random import uniform

def random_product(lower,upper):
	random1=uniform(lower,upper)
	random2=uniform(lower,upper)
	return random1 * random2
	
print random_product(0,1)

#Use the following to import all functions of a module.

from random import *


class human(object):

	latin_name='homo sapien' #Attribute for the class
	
	#Add attributes for the instances.
	def __init__(self, age, sex, name=None): #initializer or constructor
		self.age = age 
		self.name = name
		self.sex = sex
	
	#Add some functions
	
	def speak(self, words):
		return words

	def introduce(self):
		if self.sex=='Female': return self.speak("Hello, I'm Ms. %s" % self.name)
		elif self.sex=='Male': return self.speak("Hello, I'm Mr. %s" % self.name)
		else: return self.speak("Hello, I'm %s" % self.name)

	def sayHi(self, otherHuman):
		print '%s says hi to %s' % (self.name, otherHuman.name)

	def writeFunc(self, func_type):
		print 'I wrote a %s function' % (func_type)
	
	def __str__(self):
		return 'Human: %d year-old %s.' % (self.age, self.sex)
	
	@classmethod
	def class_introduce(cls):
		return 'Here is humanity!'
	
	def sayHi(self, otherHuman):
		return "Hi %s my name is %s" %(otherHuman.name, self.name)

me = human("24", "male")
print me.speak("Here's what I have to say")
print me.introduce()
me.sex = 'Male'
print me.introduce()
#me.sex = 3
#print me.introduce()
me.age = 100
print me
me.name = 'Matt'
buddy = human(age="30", sex='male', name='bruh')
print buddy.introduce()

print me.sayHi(buddy)
