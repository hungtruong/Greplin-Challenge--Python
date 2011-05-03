fibs = {1:0,2:1,3:1}

def isPrime(num):
	i = 3
	if num == 1:
		return False
	if num % 2 == 0:
		return False
	else:
		while i < num:
			if num % i == 0:
				return False
			i = i+1
		return True

def fib(x,fibs=fibs):
	if x not in fibs:
		fibs[x] = fib(x-1,fibs) + fib(x-2,fibs)
	return fibs[x]

x = 100
i = 2
found = False
while not found:
	x = fib(i)
	i = i+1
	if x > 227000 and isPrime(x):
		print x
		found = True
		
"""(I did the prime factorization by hand)"""
"""answer=352"""