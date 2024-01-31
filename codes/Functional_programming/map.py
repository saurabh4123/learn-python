#short hand operations to manipulate data
class Student:
    def __init__(self,name,score):
        self.name=name
        self.score=score

students = [Student("Saurabh",0.8),Student("Lohit",0.7),Student("Niraj",0.75),Student("Shubham",0.65),Student("Shashi",0.6),Student("Meet",0.4)]

student_res=[]
for student in students:
    # if student.score>=0.7:
    #     student_res.append(f"{student.name} Passed")
    # else:
    #     student_res.append(f"{student.name} Failed")

    #one liner for above code
    student_res.append(f"{student.name} Passed") if student.score>=0.7 else student_res.append(f"{student.name} Failed")


print(student_res)

#doing same above logic using map
map_res=map(lambda student:student.name,students)  #first argument is what you want to perform and second is on what thing u want to perform that operation
print(map_res)

#used list since map is an object itself
map_res=list(map_res)
print(map_res) 

#now the same logic of for loop in map
map_result=list(map(lambda student: f"{student.name} Passed" if student.score>=0.7 else f"{student.name} Failed",students))
print(map_result)

#challenge double the numbers in list using map
num=[1,4,9,21,54]
double_list=list(map(lambda number:number*2,num))
print(double_list)