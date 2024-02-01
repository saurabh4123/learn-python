# +---------+
# |         |
#  Fibonacci 
# |         |
# +---------+

#apply decorator to make a function that returns Fibonacci print output like above

def deco(func):
    def wrapper():
        print("+---------+")
        print("|         |")
        # res=func()
        func()
        print("|         |")
        print("+---------+")
        # return res
    return wrapper

@deco
def func():
    print(" Fibonacci")

func()

