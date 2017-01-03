# implementation of canditate Generation Algorithm
# Dataset is trivial numeric data
import numpy as np 
import pandas as pd 

nonUnique = [[1,2,3,4],[2,3,4,5],[2,3,4,6],[1,3,3,4],[1,3,4,5],[2,3,5,6]]

candidates = []

k = len(nonUnique[0])
print 'k:',k


for i in range(0, len(nonUnique)):
	for j in range(i + 1, len(nonUnique)):
		non_unique1 = nonUnique[i];
		non_unique2 = nonUnique[j];

		if cmp(non_unique1[0:k-2], non_unique2[0:k-2]):
			candidate = [None]*(k+1)
			
			for n in range(0, k - 1):
				candidate[n] = non_unique1[n]

			if non_unique1[k-1] < non_unique2[k-2]:
				candidate[k-1] = non_unique1[k-1]
				candidate[k] = non_unique2[k-1]
			else:
				candidate[k-1] = non_unique2[k-1]
				candidate[k] = non_unique1[k-1]

			# if isNotMinimal(candidate) is true:
			# 	continue
			candidates.append(candidate)
print candidates	 

				
