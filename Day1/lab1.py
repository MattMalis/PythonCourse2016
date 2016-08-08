import math

def binarify(num):
  	if num<=0: return '0'
	digits = []
	cur = num
	while(cur>0):
		digits.append(str(cur%2))
		cur/=2
	digits.reverse()

	return ''.join(digits)
		
	
def int_to_base(num, base):
  """convert positive integer to a string in any base"""
  if base<=0:  return '0' 
  digits = []
  if (num <0):
  	cur= -num
  else: cur = num
  while(cur>0):
		digits.append(str(cur%base))
		cur/=base
  if (num <0): digits.append('-')
  digits.reverse()

  
  
  return ''.join(digits)

def base_to_int(string, base):
  """take a string-formatted number and its base and return the base-10 integer"""
  if string=="0" or base <= 0 : return 0 
  result = 0 
  flip = False;
  if string[0]=='-':
  	flip=True;
  	string = string[1:]
  pow = len(string)-1
  for letr in string:
  	letrNum = int(letr)
  	result+= letrNum*(base**pow)
  	pow-=1
  if flip:
  	result= -result
  return result 

def flexibase_add(str1, str2, base1, base2):
  """add two numbers of different bases and return the sum"""
  n1 = base_to_int(str1, base1)
  n2 = base_to_int(str2, base2)
  #result = int_to_base(tmp, base1)
  return n1+n2

def flexibase_multiply(str1, str2, base1, base2):
  """multiply two numbers of different bases and return the product"""
  n1 = base_to_int(str1, base1)
  n2 = base_to_int(str2, base2)  
  return n1*n2 

def romanify(num):
  """given an integer, return the Roman numeral version"""
  result = ""
  onesDict = {1:"I", 2: "II", 3: "III", 4: "IV", 5: "V", 6: "VI", 7: "VII", 8: "VIII", 9: "IX", 0:""}
  ones = num%10
  num-=num%10
  result = onesDict[ones] + result
  tensDict = {10:"X", 20: "XX", 30: "XXX", 40:"XL", 50:"L", 60:"LX", 70: "LXX", 80: "LXXX", 90: "XC", 0:""}
  tens = num%100
  num-=num%100
  result = tensDict[tens] + result
  hunsDict = {100:"C", 200: "CC", 300: "CCC", 400:"CD", 500:"D", 600:"DC", 700: "DCC", 800: "DCCC", 900: "CM", 0:""}
  huns = num%1000
  num-=num%1000
  result = hunsDict[huns] + result
  thous = num/1000
  result = "M"*thous + result
  
  return result
  
# Copyright (c) 2014 Matt Dickenson
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.