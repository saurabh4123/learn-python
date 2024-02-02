# +---------+
# |         |
#  Fibonacci 
# |         |
# +---------+

#apply decorator to make a function that returns Fibonacci print output like above

from functools import wraps
def deco(func):
    ''''This is a function decorator'''
    @wraps(func)  #use on line 21,22,23
    def wrapper():
        print("+---------+")
        print("|         |")
        # res=func()
        func()
        print("|         |")
        print("+=========+")
        # return res
    # wrapper.__name__=func.__name__
    # wrapper.__doc__=func.__doc__  #doing this inorder to make help(fun) same as help(fun) after applying decorator since decorator changes it to this is a functio decorator
    #or we can use wraps module to the above two things 
    return wrapper

@deco
def func1():
    '''This is used to print fibonacci'''
    print(" Fibonacci")

func1()
help(func1)

#make a bold and italic html tag decorator for text fibonacci

def bold(func):
    '''Decorator for bold'''
    @wraps(func)
    def wrapper():
        print("<b>",end="")
        func()
        print("</b>")
    return wrapper

def italic(func):
    '''Decorator for italic'''
    @wraps(func)
    @bold
    def wrapper():
        print("<i>",end="")
        func()
        print("</i>",end="")
    return wrapper

@italic
def func2():
    print("Fibonacci",end="")

func2()

# we can use two decorators independently
def italic_ind(func):
    '''Decorator for italic'''
    @wraps(func)
    def wrapper():
        print("<i>",end="")
        func()
        print("</i>",end="")
    return wrapper

@bold
@italic_ind
def func3():
    print("Fibonacci",end="")

func3()

