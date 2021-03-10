# Calculator program

def fib(n):
	first = 0
	second = 1
	num = 0
	if n == 0:
		return 0
	if n == 1:
		return 1
	else:
		for val in range(int(n)):
			num = first + second
			first = second
			second = num
		return num

def factorial(n):
    result = 1
    for num in range(int(n)):
        result *= num+1
    return result

if __name__ == "__main__":
	#give = input("Enter a num: ")
	#print(fib(give))
        give = input("Enter a num: ")
        print(factorial(give))
