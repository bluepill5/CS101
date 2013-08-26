## Problem Set 2 (Optional 2)
## 25-08-2013, by bluepill5

def fix_machine(debris, product):
	'''
	String String -> String
	Given two Strings returns the 2nd input string as the output if all of
	its characters can be found in the 1st input and "Give me something that's
	not useless next time." if it's impossible.
	>>> fix_machine('wsx0-=mttrhix', 't-shirt')
	t-shirt
	>>> fix_machine('UdaciousUdacitee', 'Udacity')
	"Give me something that's not useless next time."
	'''
	return product if set(debris).intersection(set(product)) == set(product) else "Give me something that's not useless next time."

def daysBetweenDates(year1, month1, day1, year2, month2, day2):
	'''
	year month day year month day -> days
	Given a 'date' and a posterior 'date' calculate the difference in days.
	Assume that the given dates are correct.
	>>> daysBetweenDates(2012,1,1,2012,2,28)
	58
	>>> daysBetweenDates(2012,1,1,2012,3,1)
	60
	>>> daysBetweenDates(2011,6,30,2012,6,30)
	366
	>>> daysBetweenDates(2011,1,1,2012,8,8)
	585
	>>> daysBetweenDates(1900,1,1,1999,12,31)
	36523
	'''
	def isLeapYear(year):
		'''
		year -> Boolean 
		Given a year return True if is a leap year else False.
		>>> isLeapYear(1999)
		False
		'''
		return ((year % 4 == 0 and not year % 100 == 0) or (year % 400 == 0))

	def accumulator(year1, month1, day1, year2, month2, day2, acc):
		daysOfMonthsLeap    = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
		daysOfMonthsNotLeap = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

		if year1 == year2:
			if month1 == month2:
				return acc + (day2 - day1)
			else:
				if isLeapYear(year1):
					return accumulator(year1, month1 + 1, day1, year2, month2, day2, acc + daysOfMonthsLeap[month1 - 1])
				else:
					return accumulator(year1, month1 + 1, day1, year2, month2, day2, acc + daysOfMonthsNotLeap[month1 - 1])
		else:
			if isLeapYear(year1):
				return accumulator(year1 + 1, 1, 1, year2, month2, day2, acc + sum(daysOfMonthsLeap[month1 - 1:]) - day1 + 1)
			else:
				return accumulator(year1 + 1, 1, 1, year2, month2, day2, acc + sum(daysOfMonthsNotLeap[month1 - 1:]) - day1 + 1)
	return accumulator(year1, month1, day1, year2, month2, day2, 0)


if __name__ == 'main':
	import doctest
	doctest.testmod()
