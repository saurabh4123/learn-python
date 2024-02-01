# In Python, the special variable __name__ is used to determine if the Python script is being run as the main program or
# if it is being imported as a module into another script. 
# When the Python interpreter runs a script, it assigns the __name__ variable a value of "__main__" if the script is the main program being executed.


def some_function():
    print("Function in __name__==__main__.py")

if __name__ == "__main__":
    # This code will only run if __name__==__main__.py is the main program
    print("This script is being run directly.")
    some_function()
else:
    # This code will run if __name__==__main__.py is imported as a module in another script
    print("This script is being imported as a module.")


# If you run this script directly (python __name__==__main__.py), it will print "This script is being run directly."
# If you import it as a module in another script, the code inside the else block will be executed, 
# and it will print "This script is being imported as a module."
# This construct is commonly used to write reusable code that can be both run as a standalone script and 
# imported as a module into other scripts without the code inside the if __name__ == "__main__": block running when imported