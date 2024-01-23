import random as rd
class human:
    # pass #keyword to just move to next line
    info= "This is all what we are whoever can read this code."
    nationality= "Indian."

    def __init__(self):
        print("I'm in inti i.e Initialization or constructor in other languages.")
        self.lucky_number=rd.randint(1,100)  #this is how we create instance/object/local variables
        
#accessing info
print(human.info,human.nationality)

#creating instances/objects of class
h1=human()
h2=human()
h3=human()
print(h1.lucky_number)
print(h2.lucky_number)
print(h3.lucky_number)

#we can create new instance variables on the fly in python
h1.name="Saurabh"
h2.last_name="Mishra"
print(h1.name)
print(h2.last_name)
# print(h2.name) error prone code since h2 has no instance variable named "name"


#parameterised constructor
class Dog:
    def __init__(self,name,breed):
        self.name=name
        self.breed=breed


#error if we dont pass params at the time of object creation
d1=Dog("Tom","Labra")
d2=Dog("Jerry","German")

print(f"Dog's name -> {d1.name} and breed -> {d1.breed}")
print(f"Dog's name -> {d2.name} and breed -> {d2.breed}")
        