# Quizzes (some, starting from unit 2) from CS101:

def biggest(num1, num2, num3):
	return num1 if num1 >=num2 and num1 >=num3 else biggest(num2, num3, num1)

# This was modified: 23-08-2013
# by bluepill5

def print_numbers(num):
	i = 1
	while i <= num:
		print(i)
		i += 1

def factorial(n):
	def facAcc(n, acc):
		if n == 0:
			return acc
		else:
			return facAcc(n - 1, n * acc)
	return facAcc(n, 1)




