import random as rd

class Animal:
    info="an organism made up of muscle,tissues and bones"

    def __init__(self,name):
        print(f"Animal that is created -> {name}")
        self.name=name

class Dog(Animal):  #inheriting from animal class
    def __init__(self,name,breed):
        super().__init__("Dog")  #used to refere to parent class init
        print("DOg object created!!")
        self.name=name
        self.fur=""
        self.breed=breed
        self.lucky_number=rd.randint(1,50)
    
    def bark(self):
        print("Woof!!!")

dog1=Dog("Tommy","Labra")

#using inheritance
print(dog1.info)

class BullDog(Dog):
    def __init__(self, name):
        super().__init__(name,"BULL")
        print(f"Lucky number is {self.lucky_number}")

dog2=BullDog("Timmy")
