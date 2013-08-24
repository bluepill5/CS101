## Problem Set 2
## 23-08-2013, by bluepill5

def udacify(s):
	'''
	String -> String
	Given an string, produce an string: 'U' + string
	>>> udacify('dacians')
	'Udacians'
	>>> udacify('turn')
	'Uturn'
	>>> udacify('boat')
	'Uboat'
	'''
	return 'U' + s

def bigger(a,b):
    if a > b:
        return a
    else:
        return b

def biggest(a,b,c):
    return bigger(a,bigger(b,c))

def median(num1, num2, num3):
	'''
	Number Number Number -> Number
	Produce the median of the inputs.
	>>> median(1, 2, 3)
	2
	>>> median(9, 3, 6)
	6
	>>> median(7, 8, 7)
	7
	>>> median(1, 2, 2)
	2
	'''
	return bigger(num2, num3) if num1 == biggest(num1, num2, num3) else bigger(num1, min(num2, num3))

def countdown(num):
	'''
	Int -> String
	Produce the countdown from num to 1 and display "Blastoff".
	>>> countdown(3)
	3
	2
	1
	Blastoff!
	'''
	assert num >= 0
	while num > 0:
		print num
		num -= 1
	print "Blastoff!"

def find_last(s1, s2):
	'''
	Strin String -> Int
	Produce the last position of s2 in s1 if exist, otherwise -1.
	>>> find_last('aaaa', 'a')
	3
	>>> find_last('aaaaa', 'aa')
	3
	>>> find_last('aaaa', 'b')
	-1
	>>> find_last("111111111", "1")
	8
	>>> find_last("222222222", "")
	9
	>>> find_last("", "3")
	-1
	>>> find_last("", "")
	0
	'''
	index = s1.find(s2)
	n1 = len(s1)
	n2 = len(s2)

	if n2 == 0:
		return n1
	
	if index < 0 or n1 <= n2:
		return index
	
	i = index + 1
	while i <= n1:
		track = s1.find(s2, i)
		if track > 0:
			index = track
			i = index + 1
		else:
			break
	return index

def print_multiplication_table(num):
	'''
	posInt -> String
	takes as input a positive whole number, and prints out a multiplication,
	table showing all the whole number multiplications up to and including the
	input number.
	>>> print_multiplication_table(3)
	1 * 1 = 1
	1 * 2 = 2
	1 * 3 = 3
	2 * 1 = 2
	2 * 2 = 4
	2 * 3 = 6
	3 * 1 = 3
	3 * 2 = 6
	3 * 3 = 9
	'''
	assert num > 0
	i = 1
	while i <= num:
		j = 1
		while j <= num:
			print str(i) + ' * ' + str(j) + ' = ' + str(i * j)
			j += 1
		i += 1



if __name__ == '__main__':
	import doctest
	doctest.testmod()