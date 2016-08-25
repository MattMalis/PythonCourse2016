import time
import math
import random
import matplotlib.pyplot as plt
import numpy

from hw4_sorts_mm import mergeSort, bubbleSort
	
	
huns = map(lambda x: 100*x, range(1,10))
## inputs greater than 1000 give max recursion depth error...

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
	result = merge_trials(n, 10)
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
	result = bub_trials(n, 10)
	bub_results.append(result)





plt.plot(huns, bub_results, label = "Bubble Sort")
plt.plot(huns, merge_results, label = "Merge Sort")
plt.xlabel('input size')
plt.ylabel('run time')
plt.legend(loc = 'upper left')
plt.show()
