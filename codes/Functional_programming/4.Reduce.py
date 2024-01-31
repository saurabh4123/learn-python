#map->takes a list and manipulates it to change the data
#filter->takes a list and shrinks it down to 0,1,2...size
#reduce->takes a list and bring it down to single value or object

class Student:
    def __init__(self,name,score):
        self.name=name
        self.score=score
    
    def __repr__(self):  #repr stands for representation it means object of this class will be represented
        return f"{self.name} : {self.score}"
    
students = [Student("Saurabh",0.8),Student("Lohit",0.7),Student("Niraj",0.75),Student("Shubham",0.65),Student("Shashi",0.6),Student("Meet",0.4)]

#we can understand this using average score
score_total=0
for student in students:
    score_total+=student.score
print(f"Average score -> {score_total/len(students)}")

#now using reduce 
#to use reduce we have to import it
from functools import reduce
#Three params- 
#1.lambda func
#2. object to work on
#3. initial value of param in lambda func
reduced_total = reduce(lambda total,student: student.score + total , students , 0)
print(f"Average score -> {reduced_total/len(students)}")

#multiply all number in list using reduce
nums=[1,2,3,4]
product = reduce(lambda prod,num:prod*num,nums,1) #initial value of prod is set to 1
#we can even skip third param since reduce takes first element in list as initial value
#we didn't do it above because first element was an object
print(f"Final product id -> {product}")