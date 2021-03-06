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
		if len(nums)==1:
			return nums
		if len(nums)==2:
			if left[0]>right[0]:
				return [right[0], left[0]]
			else: return [left[0], right[0]]
		# else:
# 			mini = nums[0]
# 			for i in nums:
# 				if i<mini:
# 					mini = i
# 			maxi = mini
# 			for i in nums:
# 				if i>maxi:
# 					maxi = i
# 			middle = nums[0]
# 			for i in nums:
# 				if i!=mini and i!=maxi:
# 					middle = i
# 			return [mini, middle, maxi]
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
	
	