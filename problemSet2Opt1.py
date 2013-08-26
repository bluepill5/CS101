## Problem Set 2 (Optional 1)
## 25-08-2013, by bluepill5

def weekend(day):
	'''
	day -> Boolean
	Given an a day returns True if it's 'Saturday' or 'Sunday' and 
	False otherwise.
	>>> weekend('Monday')
	False
	>>> weekend('Saturday')
	True
	'''
	return day == 'Saturday' or day == 'Sunday'

def stamps(num):
	'''
	PosInt -> PosInt_5p PosInt_2p PosInt_1p
	Given an positive integer in pence produce the number of 5p, 2p, ansd 1p
	stamps required to make up that value.
	>>> stamps(8)
	(1, 1, 1)
	'''
	fiveP = num // 5
	twoP = (num - (5 * fiveP)) // 2
	oneP = num - (5 * fiveP) - (2 * twoP)
	return (fiveP, twoP, oneP)

def set_range(num1, num2, num3):
	'''
	num num num -> num
	Given 3 numbers produce the range of the three inputs.
	>>> set_range(10, 4, 7)
	6
	>>> set_range(1.1, 7.4, 18.7)
	17.6
	'''
	return max(num1, num2, num3) - min(num1, num2, num3)



if __name__ == 'main':
	import doctest
	doctest.testmod()






