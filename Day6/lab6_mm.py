#Exercise 1
#Write a function to calculate the greatest common divisor of two numbers

def gcf(a, b, divisor=0): ## just don't provide an argument for divisor and this will work out ok...
	if (a==b): return a
	if (a<b):
		low = a
		high = b
	else:
		low = b
		high = a
	if (high%low == 0):
		return low
	if (divisor==0): divisor = (low/2)+1
	if (a%divisor==0 and b%divisor==0):
		return divisor
	else: return gcf(a, b, divisor-1)
	
#Exercise 2
#Write a function that returns prime numbers less than 121
def primes_less_than(n):
	#primes = []
	if n<=1:
		return
	if n==2:
		print '2'
		return
	n_prime = True
	for num in range(2,n/2+1):
		if n%num==0:
			n_prime = False
	if n_prime: print n
	return primes_less_than(n-1)
	
	
	# for num in range(n):
# 		prime = True
# 		for possible_prime in range(2,(num/2+1)):
# 			if (num%possible_prime == 0):
# 				prime = False
# 				break;
# 		if prime: primes.append(num)
# 	return primes



#Exercise 3
#Write a function that gives a solution to Tower of Hanoi game
#https://www.mathsisfun.com/games/towerofhanoi.html



