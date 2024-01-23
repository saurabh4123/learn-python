print("Hello World")

#variables
wallet =41 #int
print(wallet)

day=21

temp=-15  #integer

weight=72.5   #float

shirt = 'blue'  #string

is_light_on = True  #boolean

print(3+3)

print(type(day))

print(type(temp))

print(type(weight))

print(type(shirt))

print(type(is_light_on))

quote = "Hey there, it's \"party\" time"   #use \ if you dont want ' or " to be treated as end line

print(quote)

#using variables inside string ->use f inside print

print(f"Today is {day} October and it's {temp} degrees outside.")

#if else
if(is_light_on):
    print("Light is on!!!")
    print("Party hard!!!")
else:
    print("Light off....")

if(weight<70):
    print("You are underweight.")
elif(weight<80):
    print("You are fit!!!")
else:
    print("You are obese.")


# if else without ()
if weight<70:
    print("You are underweight.")
elif weight<80:
    print("You are fit!!!")
else:
    print("You are obese.")

#intoducing random numbers into module
    
import random

print(random.randint(1,99)) #gives random integer between 1 and 99

print(random.random()) #gives float between 0 and 1

#List
fav_sports=["Cricket","Badminton","Hockey"]
#list can be heterogeneous i.e. it can hold more than 1 different datatypes
fav=[1,2,3.2,4.1,'hi',"hello",True]
print(fav)

#to get first item in list
print(fav_sports[0])

#get len of fav_sports
print(len(fav_sports))

#add items to list
fav_sports.append("Chess")
print(fav_sports)

#add to list on 2nd position i.e. index 1
fav_sports.insert(1,"Polo")
print(fav_sports)

#add to list on 2nd position i.e. index 1
del(fav_sports[1])
print(fav_sports)

#for loop
for x in range(10):
    print(x)  #prints 0 to 9

for sport in fav_sports:
    print(sport)  #prints every item in list

#print even number from 0 to 40(inclusive)
for y in range(41):
    if(y%2==0):
        print(y)

#dictionary is key value pair {}
dict={"Jane":6,"Tom":5,"Jerry":2} #Jane is key and 6 is value
print(dict)
print(dict["Jerry"]) #getting value with exact key
dict["Bruno"]=9
print(dict)

del(dict["Jerry"]) #delete Jerry key value from dict
print(dict)
print(len(dict))

#int key and boolean value dict
ints_and_bools={5:False,7:True,9:True}
print(ints_and_bools)
print(ints_and_bools[5])

#to take large string as input we use triple/three quotes

text="""Lakshmi Kant Dixit, a priest from Varanasi, will perform the ‘Pran Pratishtha’ ceremony at 12.20pm. The 51-inch tall Ram Lalla idol to be consecrated, has been crafted by Mysuru-based sculptor Arun Yogiraj. The idol also contains carvings of all ten incarnations of Lord Vishnu, Hindu Gods like Lord Hanuman and other major Hindu religious symbols. Seven-day rituals for the consecration ceremony began on January 16.
Full coverage of Ram Temple inauguration: Ayodhya Ram Mandir Opening Ceremony
Here is a list of VVIPs and celebrities who have been invited to attend consecration ceremony of the Ram janmbhoomi temple in Ayodhya
Virat Kohli (Cricketer and former India captain), Anil Kumble (Former India cricketer and captain), Venkatesh Pradesh (Former India fast bowler), Sachin Tendulkar (Indian cricket legend)
MS Dhoni (Former India cricketer and captain), R Ashwin (India spin bowler), Mithali Raj ( Former India women cricketer)
Ayodhya Ram Mandir: Temple set to become the largest in India, stands at a height of 161
Indian film stars
Reached Ayodhya
Rajinikanth ( Superstar actor), Anupam Kher (Actor), Kangana Ranaut (Film star and national award winner), Vivek Oberoi (Actor), Shefali Shah (Actress), Randeep Hooda (Actor)
Invited
Amitabh Bachchan(Superstar actor), Abhishek Bachchan(Actor), Ranbir Kapoor(Actor), Alia Bhatt(Actress and national awardee), Ayushmann Khurrana(Actor), Tiger Shroff(Actor), Vicky Kaushal(Actor), Katrina Kaif (Actress), Akshay Kumar(Actor), Chiranjeevi (Superstar actor), Ajay Devgn (Actor), Sunny Deol (Actor)
Politicians
Reached Ayodhya
Hema Malini (BJP leader and actress)
Invited
Meera Kumar (Former Lok Sabha speaker)
Religious leaders and sages
Reached Ayodhya
Bageshwar Dham's Dhirendra Shastri (Religious Guru)
Other VVIPs
Reached Ayodhya
Prasoon Joshi ( Indian poet, lyricist and writer), Sonu Nigam (Singer), Madhur Bhandarkar (Filmmaker), Anu Malik (Singer), Sanjeev Kapoor (Celebrity chef)
Industrialists
Invited
Ratan Tata (former chairman of the Tata Group), Mukesh Ambani ( Chairman of Reliance Industries), Anil Ambani (Businessman), Kumar Mangalam Birla(Chairperson of Aditya Birla Group), Ajay Piramal(Chairperson of Piramal Group), Anand Mahindra(Industrialist), K Krithivasan (CEO of TCS), Gautam Adani (Chairperson of Adani Group),
Meanwhile, the Ayodhya city has been decked up with saffron flags, huge cutouts of Lord Ram and posters bearing religious slogans related to Lord Ram. Massive security arrangements are in place in view of the consecration ceremony. The Ram temple will be opened for 'darshan' by devotees and pilgrims from January 23 onwards.
"""
print(len(text)) #tells number of characters

print(text.split()) #splits string into words list

print(len(text.split())) #gives number of words in the string not characters

#code to get frequency of words
word_count={} #dictionary to store word frequency
for word in text.lower().split():  #to change text to lower case to get priest and Priest wordcount same 
    # print(word)
    if word in word_count:
        word_count[word]+=1
    else:
        word_count[word]=1

print(word_count)

#function use def keyword so that python knows we are defining a function
def meow():
    print("Cat meowing")

#calling meow
meow()
for x in range(10):
    print(f"{x} cat {meow()}")  #it prints none at last as there are two print statements and meow function return None

for x in range(10):  #printing in same line
    print(f"{x+1}",end=" ")
    meow()

#using params
def name_calling(name):
    print(f"Hi, {name}")
name_calling("Saurabh")

def add(n1,n2):
    print(n1+n2)
add(4,8)
add(4.8,5)
add(4.8,5.2)

#returning from a function-return double
def double(num):
    return num*2

print(double(5))
no=double(5)
print(no)

#function to return a string in upper case
def upperCase(str):
    return str.upper()

str="Hello World!!"
new_str=upperCase(str)
print(new_str)

#taking input
ip_str=input("Enter some string :")
print(ip_str)

#taking input number
num=input("Enter a number to double : ")
print(f"Doubled vaue of number is {int(num)*2}")


    








