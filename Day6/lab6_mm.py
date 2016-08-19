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

def stack(arr, new_item):
	if (len(arr)>0):
		if (arr[-1]<new_item):
			print "ERROR - out of order stacking"
			print "end of array: " + str(arr[-1]) + ", new item: " + str(new_item)
			return
	arr.append(new_item)
	
def tower(disks, st=0, dest=2,t = [[],[],[]]):
	if (disks<=2):
		return
# 	if three disks: 

# 	
## d1 = smallest, d3 = heaviest, etc
## hardcoding for now - FIX
	nums = [0,1,2]
	st_dest = [st, dest]
	for num in nums:
		if not num in st_dest:
			open = num

	if (disks==3):
		t[st] = ['d3', 'd2', 'd1']
		#t[st].append('d3')
		#t[st].append('d2')
		#t[st].append('d1')

		t[open] = []
		t[dest] = []
# 		first move -> top from st to destination
		print 'first'
		print t

		mover = t[st].pop()
		stack(t[dest],mover)
# 		second move -> middle from st to open
		print 'second'
		print t
		mover = t[st].pop()
		stack(t[open],mover)
# 		third -> top from dest to open
		print 'third'
		print t
		mover = t[dest].pop()
		stack(t[open],mover)
# 		fourth -> bottom from st to destination
		print 'fourth'
		print t

		mover = t[st].pop()
		stack(t[dest],mover)
# 		fifth -> top from open to start
		print 'fifth'
		print t

		mover = t[open].pop()
		stack(t[st],mover)
# 		sixth -> middle from open to destination
		print 'sixth'
		print t

		mover = t[open].pop()
		stack(t[dest],mover)
# 		seventh -> top from start to destination
		print 'seventh'
		print t

		mover = t[st].pop()
		stack(t[dest],mover)
		
		print t
		return t
		
# 	if disks>3:
# 		call tower(disks-1, start=start, destination=open)
# 		move real_bottom from start to destination
# 		call tower(disks-1, start=open, destination=destination)
# 	
	if (disks>3):
		start_pile = []
		for num in range(disks)[::-1]:
			start_pile.append(str('d'+str(num+1)))
		print "start pile when disks = %s: %s" %(disks,str(start_pile))
		begin_t = [start_pile,[],[]]
#		begin_t= [ [], [], [] ]
		t_ = tower(disks-1, st, open, begin_t)
		print "successful first tower(disks-1) call \n"
		print "tower after first tower() call: \n"
		print str(t)
		mover = t[st].pop()
		stack(t[dest],mover)
		tt = tower(disks-1, open, dest, t_)
		print "successful second tower(disks-1) call \n"

			

tower(5)

