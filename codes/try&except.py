#print("Before")
# 4/0
#print("Code After")
#only Before is printed and after 4/0 code explodes therefore we use try and catch to execute risky code'
print("Before")

try:
    4/0
except:
    print("OOPSIE!! we had an error in try which lead to execution in except block!!")
print("Code After")

#we can define our own error messages for different exceptions
try:
    print(name)
    4/0 #interpreter doesn't reach here/interpret this line as there is error in print(name) and is directed to except NameError.
except NameError as e:  #as e has the original error stored inside e
    print("Name isssue detected!!")
    print(e)
except ZeroDivisionError as e: 
    print("Division by zero error detected!!")
    print(e)
except Exception as e:  #using exception for generic type error
    print("Something went wrong!!") #this is to generalise the error if none of the previous mentioned error matches with error occurred.
    print(e)


#raising our own exceptions
def upper_case(word):
    if len(word)<=0:
        raise Exception("This word needs to have atleast one letter!!")
    return word.upper()

# print(upper_case(""))
# #the above line make the program stop due to exception

# #we can create our own errors
# class CheeseError(Exception):
#     pass
# raise CheeseError("Hi there this is an error!!")

#commenting raise of exceptions so that our program doesn't stop

