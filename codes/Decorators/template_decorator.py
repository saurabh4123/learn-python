##template for decorator##

def my_decorator(func):
    def wrapper():
        #do something before
        print("Before")
        result=func()
        #do something after
        print("After")
        return result
    return wrapper#finally returh the wrapped output

@my_decorator
def func():
    print("Inside function!!")

func()#we can see the wrapping before and after function call