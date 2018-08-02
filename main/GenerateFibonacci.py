#!/usr/bin/python
#FileName: GenerateFibonacci.py
#Author: Adivikolanu Teja Priyanka
#Purpose: Calculates the fibonacci sequence for the given size.

#import statements
import logging

#setting the logging properties
logging.basicConfig(filename='fibonacci.log',level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

#FunctionName: Generate_Fibonacci
#Purpose: Calculates the fibonacii sequence with Size(passed as argument) numbers in it
#Arguments: Accepts one argument on type int
#			1) Size - type int - number of fibonacii numbers to be calculated.
#Return Value: Returns the list which contains the fibonacci sequence

def Generate_Fibonacci(Size):
	#fibonacci numbers are only calculated if the size is greater than 2. first and second numbers are assumed to be 0 and 1 respectively.
	logging.info('Generating fibonacci...')
	Fib=[0,1]
	if Size <= 2:
		return Fib[0:Size]
	else:
		for i in range(2,Size):
			#adding the previous two numbers in series and appending the result to list
			Fib.append( Fib[i-2] + Fib[i-1] ) 
	return Fib