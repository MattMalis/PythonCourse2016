import time
import math
import random
import matplotlib.pyplot as plt
import numpy

def mergeSort(n, nums=[], begin=True):
	#print "nums when n = %s: %s" %(n, nums)
	if n==0:
		return
	if begin:
		for i in range(n):
			nums.append(random.random())
	mid = n//2
	left = nums[:mid]
	right = nums[mid:]
	if n>2:
		left = mergeSort(len(left), left, False)
		right = mergeSort(len(right), right, False)
	else:
		if len(nums)==2:
			if left[0]>right[0]:
				return [right[0], left[0]]
			else: return [left[0], right[0]]
		else:
			mini = nums[0]
			for i in nums:
				if i<mini:
					mini = i
			maxi = mini
			for i in nums:
				if i>maxi:
					maxi = i
			middle = nums[0]
			for i in nums:
				if i!=mini and i!=maxi:
					middle = i
			return [mini, middle, maxi]
	left_head = 0
	right_head = 0
	copy = []
	while (left_head < len(left) and right_head<len(right)):
		if left[left_head]<right[right_head]:
			copy.append(left[left_head])
			left_head+=1
		else: 
			copy.append(right[right_head])
			right_head+=1
	if right_head<len(right):
		copy.extend(right[right_head:])
	else:
		copy.extend(left[left_head:])
	return copy
	
	
	
	
	
def bubbleSort(n, nums=[], end_sorted = 0, begin = True):
	if n==0:
		return
	if begin:
		for i in range(n):
			nums.append(random.random())
	if len(nums)-end_sorted>2:
		for i in range(0, len(nums)-end_sorted-1):
			if nums[i]>nums[i+1]:
				temp = nums[i+1]
				nums[i+1] = nums[i]
				nums[i] = temp
		end_sorted = 0
		for j in range(1,len(nums)-1)[::-1]:
			if nums[j]>=nums[j-1]:
				end_sorted+=1
			else: break
		bubbleSort(n, nums, end_sorted, False)
	return nums
	
	
	
	
	
	
huns = map(lambda x: 100*x, range(1,10))

bub_results = []
merge_results = []

def merge_trials(n, trials):
	n_trials = []
	for i in range(trials):
		start = time.time()
		mergeSort(n,[],True)
		end = time.time()
		elapsed = end-start
		n_trials.append(elapsed)
	return numpy.mean(n_trials)
		
for n in huns:
	time.sleep(1)
	result = merge_trials(n, 1)
	merge_results.append(result)


def bub_trials(n, trials):
	n_trials = []
	for i in range(trials):
		start = time.time()
		bubbleSort(n,[],0,True)
		end = time.time()
		elapsed = end-start
		n_trials.append(elapsed)
	return numpy.mean(n_trials)
	
		
for n in huns:
	time.sleep(1)
	result = bub_trials(n, 1)
	bub_results.append(result)

# for n in huns:
# 	time.sleep(1)
# 	n_trials = []
# 	#for i in range(5):
# 	start = time.time()
# 	mergeSort(n)
# 	end = time.time()
# 	elapsed = end-start
# 		#n_trials.append(elapsed)
# 	#avg = numpy.mean(n_trials)
# 	merge_results.append(elapsed)





plt.plot(huns, bub_results, label = "Bubble Sort")
plt.plot(huns, merge_results, label = "Merge Sort")
plt.xlabel('input size')
plt.ylabel('run time')
plt.legend(loc = 'upper left')
plt.show()

# 
# f, axarr = plt.subplots(2, sharex=True, sharey=True)
# f.suptitle('Bubble Sort (top) and Merge Sort (bottom)')
# axarr[0].plot(huns, bub_results)
# axarr[1].plot(huns, merge_results)
# # Bring subplots close to each other.
# f.subplots_adjust(hspace=0)
# # Hide x labels and tick labels for all but bottom plot.
# for ax in axarr:
#     ax.label_outer()
# 
# f.show()
# 
