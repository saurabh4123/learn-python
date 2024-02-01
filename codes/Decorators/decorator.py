'''This is a program to learn about decorators'''

def fib(n):
    '''Return the nth number in the Fibonacci sequence.'''
    if n<2:
        return n
    else:
        return fib(n-1)+fib(n-2)

print(fib(3)) #printing the third term

help(fib)  #return the string inside '''........'''

#decorator
#a decorator is a callable that takes another function as an argument,extending the behaviour of the function without explicitly modifying that function.
#decorator are used to add statements before and after functions without modifying them
#suppose we have 50 functions and we want to add logs before every function so instead of modifying each funtion we can use decorators

def my_decorator(func):
    '''Decorator function'''
    def wrapper():
        '''Returns string F-I-B-O-N-A-C-C-I'''
        return "F-I-B-O-N-A-C-C-I"
    return wrapper

def printfib():
    '''Returns fibonacci'''
    return "Fibonacci"

pfib = my_decorator(printfib)  #equivalent to @my_decorator before function
print(pfib) #we can see this is a reference to my_decorator func
print(pfib()) #we can see this calls wrapper

@my_decorator
def ppfib():
    '''Return Fibo'''
    return "Fibo"

print(ppfib())#we can see this has same output as line 32




