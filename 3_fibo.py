#Creating lambda function to generate fibonnacci series
fibonacciNumber = lambda n: n if n <= 1 else fibonacciNumber(n - 1) + fibonacciNumber(n - 2)

# Initiating numbers of  series to print
num_series = 50 
#Looping series to the given limit
fib_series = [fibonacciNumber(i) for i in range(num_series)]

print("Fibonacci series ", fib_series)
