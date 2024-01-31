#supported in python 3.10 or above
number =int(input("Enter a number : "))

match number:
    case 1:
        print("ONE!!")
    case 2:
        print("TWO!!")
    case 3:
        print("THREE!!")
    case 4:
        print("FOUR!!")
    case 5:
        print("FIVE!!")
    case 6:
        print("SIX!!")
    case 7:
        print("SEVEN!!")
    case 8:
        print("EIGHT!!")
    case 9:
        print("NINE!!")
    case 0:
        print("ZERO!!")
    case _:
        print("Default!!")