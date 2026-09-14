

#Create a python program that identifies age group 

name = input("Enter your name: ")
age = int(input("Enter your age: "))

if age >= 1 and age <= 2:
    print("The age is considered as toddler")

elif age >= 3 and age <= 5:
    print("The age is consiered as preschool/middle Childhood")

elif age >= 7 and age <= 11:
    print("The age is considered as Middle Childhood") 
    
elif age >= 14 and age <= 18:
    print("The age is considered as Teenager")
    
elif age >= 21 and age <= 38:
    print("The stage is considered as Early Adulthood")
    
elif age >= 41 and age <= 58:
    print("The satge is considered as Midlle Adulthood")
    
elif age >= 60:
    print("The age is considered as Seniority/Older Adulthood")