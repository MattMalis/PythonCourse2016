# for numbers divisible by 3, print "Fizz"
# for numbers divisible by 5, print "Buzz"
# for numbers divisible by 3 and 5, print "FizzBuzz"
# otherwise, print the number

def FizzBuzz(i):
  try:
    if i % 15 == 0:
      raise Exception, "Divisible by 3 and 5!"    
    if i % 3 == 0:
      return "Fizz"
    if i % 5 == 0:
      return "Buzz"
    print "finally1"
  except:
    if i % 15 == 0:
      return "FizzBuzz"
  else:
    return str(i)
  finally:
    print "finally2"
  

for i in range(18):
  print str(i) + ": " + FizzBuzz(i) + '\n'
