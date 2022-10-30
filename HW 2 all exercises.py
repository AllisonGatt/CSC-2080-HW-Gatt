#HW 2.1, chapter 2, discussion problem 4
#question 4a, this program prints 0, 1, 4, 9, 16.
#It multiplying the numbers 0-4 by themselves

for i in range(5):
    print (i * i)
    
# question 4b, this prints 3 1 4 1 5
# It prints exactly what is in the brackets

for d in [3,1,4,1,5]:
    print(d, end=" ")

#question 4c prints hello 4 times
# it is a loop for hello in the range of 4 

for i in range(4):
    print("hello")
    
#question 4d prints 0 1, 1 2, 2 4, 3 8, 4 16.
#for the number 0-4, it is printing the number and 2 raised to that number

for i in range(5):
    print(i, 2**i)

#HW 2.2 chapter 3 discussion problem 1
# a, 4.0 / 10.0 + 3.5 * 2 gives the result of 7.4 which is <class 'float'>
# c, abs(4-20//3)**3 results in 8, <class 'int'>
# e, 3*10//3+10%3 results in 11, <class 'int'>

#HW 2.3 chapter 3 discussion problem 2
# b will give an answer to the equation n(n-1)/2 depending on the input n
#the answer is given as a float
import math
n = eval(input("what is n" ))
answer = (n*(n-1))/2
print ("the answer is", answer)

#c will evaluate the expression based on the input of radius
#math.pi is able to be used because of import math
#the answer is given as a float

r = eval(input("what is the radius?"))
x = 4* math.pi * (r**2)
print (x)

#HW 2.4 chapter 3 discussion problem 4
for i in [1,3,5,7,9]:
    print(i, ":", i**3)
    print(i)
# b, this code is a loop that prints i : i squared, then prints just i
# it does this for the numbers in the brackets, starting with 1 and ending with 9
# 1 : 1
#1
#3 : 27
#3
#5 : 125
#5
#7 : 343
#7
#9 : 729
#9

x=2
y=10
for j in range(0, y, x):
    print(j, end=" ")
    print(x+y)
    print("done")
#c, this code is a loop where it prints 0-8 followed by 12, which is x+y, followed by the word done
#the 0-8 is determiend by the range 
#0 12
#done
#2 12
#done
#4 12
#done
#6 12
#done
#8 12
#done

#HW 2.5 chapter 3 programming exercise 6
#calculating the slope of a line passing through 2 points
import math
def main():
    print ("this program finds the slope of a line through two points")
    x1, y1 = eval(input("enter the first pair of coordinates separated by a comma")) #input first set 
    x2, y2 = eval(input("enter the second pair of coordinates separated by a comma")) #input second set
    slope = (y2 - y1)/(x2-x1) #formula and calculation
    print("the slope is", slope)

#HW 2.6 chapter 3 programming exercise 7
#a program that finds the distance between 2 points

import math
def main():
    print("this program finds the distance between 2 points")
    x1, y1 = eval(input("enter the first point, separated by a comma" )) #input first set 
    x2, y2 = eval(input("enter the second point, separated by a comma" )) #input second set
    distance = math.sqrt(((x2-x1)**2)+((y2-y1)**2)) #formula and calculation 
    print("the distance is ", distance)
