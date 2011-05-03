import itertools
nums = [3, 4, 9, 14, 15, 19, 28, 37, 47, 50, 54, 56, 59, 61, 70, 73, 78, 81, 92, 95, 97, 99]
count = 0
for i in range(len(nums)):
	temp = nums[0:i+1]
	print "list of" + str(temp)
	for j in range(2,len(temp)):
		combinations = itertools.combinations(temp,j)
		for combo in combinations:
			if sum(combo) == temp[i]:
				count = count + 1
				
print count