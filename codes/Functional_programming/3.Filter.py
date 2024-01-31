class Student:
    def __init__(self,name,score):
        self.name=name
        self.score=score
    
    def __repr__(self):  #repr stands for representation it means object of this class will be represented like this see line '20'
        return f"{self.name} : {self.score}"

students = [Student("Saurabh",0.8),Student("Lohit",0.7),Student("Niraj",0.75),Student("Shubham",0.65),Student("Shashi",0.6),Student("Meet",0.4)]

#filter is basically to filter things out
#suppose we want a list of failed students

#1. Without functional programming
failed_list=[]
for student in students:
    if student.score<0.7 :
        failed_list.append(student)
print(failed_list) 
#works fine but if we comment out __repr__ it prints "[<__main__.Student object at 0x000002831110A3C0>, <__main__.Student object at 0x000002831110A3F0>, <__main__.Student object at 0x000002831110A420>]"
#therefore we go for repr bcz it represents the objects pretty well

#2. With functional programming i.e filter
#used 2 args first is lambda function that returns true or false,if true add else discard and second is the thing on which we want to apply filter
filtered_list=list(filter(lambda student: student.score < 0.7,students))
print(filtered_list)

#challenge
#filter out all even number from the list using filter
nums=[1,2,3,4,8,51,20,45]
final_filtered_list=list(filter(lambda num: num%2==0 ,nums))
print(final_filtered_list)