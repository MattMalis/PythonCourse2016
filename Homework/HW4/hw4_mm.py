import time
import math
import random
import matplotlib.pyplot as plt
import numpy

def mergeSort(n, nums=[], begin=True):
	#print "nums when n = %s: %s" %(n, nums)
	if begin:
		for i in range(n):
			nums.append(random.random())
	mid = n//2
	left = nums[:mid]
	right = nums[mid:]
	if mid>1:
		left = mergeSort(len(left), left, False)
		right = mergeSort(len(right), right, False)
	else:
		if len(nums)==2:
			if left[0]>right[0]:
				return [right[0], left[0]]
			else: return [left[0], right[0]]
		else:
			min = nums[0]
			for i in nums:
				if i<min:
					min = i
			max = min
			for i in nums:
				if i>max:
					max = i
			middle = nums[0]
			for i in nums:
				if i!=min and i!=max:
					middle = i
			return [min, middle, max]
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
	
	
	
	
	
	
huns = map(lambda x: 10*x, range(10))

bub_results = []
merge_results = []

for n in huns:
	n_trials = []
	for i in range(10):
		start = time.time()
		bubbleSort(n)
		end = time.time()
		elapsed = end-start
		n_trials.append(elapsed)
	avg = numpy.mean(n_trials)
	bub_results.append(avg)

for n in huns:
	n_trials = []
	for i in range(10):
		start = time.time()
		mergeSort(n)
		end = time.time()
		elapsed = end-start
		n_trials.append(elapsed)
	avg = numpy.mean(n_trials)
	merge_results.append(avg)

f, axarr = plt.subplots(2, sharex=True, sharey=True)
f.suptitle('Sharing both axes')
axarr[0].plot(huns, bub_results)
axarr[1].plot(huns, merge_results)
# Bring subplots close to each other.
f.subplots_adjust(hspace=0)
# Hide x labels and tick labels for all but bottom plot.
for ax in axarr:
    ax.label_outer()

f.show()
