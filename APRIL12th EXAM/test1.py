# -*- coding: utf-8 -*-
"""
Created on Thu Apr 12 13:54:07 2018

@author: user
"""

input1 = input("first student name:")
input2 = input("first student age:")
input3 = input("first student gender:")
input4 = int(input("first student height in INCHES WHOLE NUMBER:"))
input5 = int(input("first student weight in POUNDS WHOLENUMBERS:"))
input6 = input("second student name:")
input7 = input("second student age:")
input8 = input("second student gender:")
input9 = int(input("second student height in INCHES WHOLE NUMBER:"))
input10 = int(input("second student weight in POUNDS WHOLENUMBERS:"))
input11 = input("third student name:")
input12 = input("third student age:")
input13 = input("third student gender:")
input14 = int(input("third student height in INCHES WHOLE NUMBER:"))
input15 = int(input("third student weight in POUNDS WHOLENUMBERS:"))
input16 = input("fourth student name:")
input17 = input("fourth student age:")
input18 = input("fourth student gender:")
input19 = int(input("fourth student height in INCHES WHOLE NUMBER:"))
input20 = int(input("fourth student weight in POUNDS WHOLENUMBERS:"))
input21 = input("fifth student name:")
input22 = input("fifth student age:")
input23 = input("fifth student gender:")
input24 = int(input("fifth student height in INCHES WHOLE NUMBER:"))
input25 = int(input("fifth student weight in POUNDS WHOLENUMBERS:"))
file = open("textbmi.txt", "w")
#for i in range(1,25):
file.write(input1 + "\n")
file.write(input2 + "\n")
file.write(input3 + "\n")
file.write(str(input4) + "\n")
file.write(str(input5) + "\n")
file.write(input6 + "\n")
file.write(input7 + "\n")
file.write(input8 + "\n")
file.write(str(input9) + "\n")
file.write(str(input10) + "\n")
file.write(input11 + "\n")
file.write(input12+ "\n")
file.write(input13 + "\n")
file.write(str(input14) + "\n")
file.write(str(input15)+ "\n")
file.write(input16 + "\n")
file.write(input17 + "\n")
file.write(input18 + "\n")
file.write(str(input19) + "\n")
file.write(str(input20) + "\n")
file.write(input21 + "\n")
file.write(input22 + "\n")
file.write(input23+ "\n")
file.write(str(input24) + "\n")
file.write(str(input25)+ "\n")
#calculating BMI of Each student
bmi1 = int(input5 * 703 )/(int(input4)*int(input4))
bmi2 = int(input10 * 703 )/(int(input9)*int(input9))
bmi3 = int(input15* 703 )/(int(input14)*int(input14))
bmi4 = int(input20* 703 )/(int(input19)*int(input19))
bmi5 = int(input25* 703 )/(int(input24)*int(input24))
print("BMI OF FIRST STUDENT IS")
print((bmi1))
print("BMI OF SECOND STUDENT IS")
print((bmi2))
print("BMI OF THIRD STUDENT IS")
print((bmi3))
print("BMI OF FOURTH STUDENT IS")
print((bmi4))
print("BMI OF FIFTH STUDENT IS")
print((bmi5))
file.write(str(bmi1) + "\n") 
file.write(str(bmi2)+ "\n")
file.write(str(bmi3)+ "\n")
file.write(str(bmi4)+ "\n")
file.write(str(bmi5)+ "\n")
file.close()


#sorting height

# List of HEIGHTS
numbers = [input4 , input9 , input14, input19, input24]
 
# Sorting list of students height
numbers.sort()
print("The students height in Ascending order")
print(numbers)

#PRINTING STUDENTS WHO ARE OBESE OVERWEIGHT AND NORMAL
#check for 1st student
if bmi1 > 18.5 and bmi1 < 25:
        print('Student 1 %s is normal', input1)
elif bmi1 > 25 and bmi1 < 30:
        print('Student 1 %s is overweight', input1)
elif bmi1 > 30:
        print('Student 1 %s is obese', input1)
else:
        print('There is an error with your input')
        print('Please check you have entered whole numbers\n'
              'and decimals were asked.')

#check for 2nd student
if bmi2 > 18.5 and bmi2 < 25:
        print('Student 2 %s is normal', input6)
elif bmi2 > 25 and bmi2 < 30:
        print('Student 2 %s is overweight', input6)
elif bmi2 > 30:
        print('Student 2 %s is obese', input6)
else:
        print('There is an error with your input')
        print('Please check you have entered whole numbers\n'
              'and decimals were asked.')

#check for 3rd student
if bmi3 > 18.5 and bmi3 < 25:
        print('Student 3 %s is normal', input11)
elif bmi3 > 25 and bmi3 < 30:
        print('Student 3 %s is overweight', input11)
elif bmi3 > 30:
        print('Student 3 %s is obese', input11)
else:
        print('There is an error with your input')
        print('Please check you have entered whole numbers\n'
              'and decimals were asked.')

#check for 4th student
if bmi4 > 18.5 and bmi4 < 25:
        print('Student 4 %s is normal', input16)
elif bmi4 > 25 and bmi4 < 30:
        print('Student 4 %s is overweight', input16)
elif bmi4 > 30:
        print('Student 4 %s is obese', input16)
else:
        print('There is an error with your input')
        print('Please check you have entered whole numbers\n'
              'and decimals were asked.')

#check for 5th student
if bmi5 > 18.5 and bmi5 < 25:
        print('Student 5 %s is normal', input21)
elif bmi5 > 25 and bmi5 < 30:
        print('Student 5 %s is overweight', input21)
elif bmi5 > 30:
        print('Student 5 %s is obese', input21)
else:
        print('There is an error with your input')
        print('Please check you have entered whole numbers\n'
              'and decimals were asked.')        
#file = open('textbmi.txt','w')

#file.close()

#file = open('textbmi.txt','w')

#file.close()

#file = open('textbmi.txt','w')

#file.close()

#file = open('textbmi.txt','w')

#file.close()

#file = open('textbmi.txt','w')

#file.close()


