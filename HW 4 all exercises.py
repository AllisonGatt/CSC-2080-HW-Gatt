#Homework 4

#4.1 Discussion problem 1c will print 'p', 1e will print 'ani' and g will print 'SPAM'

#4.2 Discussion problem 2a, to get "NI" the opperation would be print(s2.upper()[:2])
#Discussion problem 2d, to get "spam" the opperation would be print(s1.lower()) or simply print(s1)
#Discussion problem 2e, to get ["sp","m"] the opperation would be print(s1[0:2], s1[3:4])

#4.3 discussion problem 3 b, the output would be:
#a
#a
#r
#d
#v
#a
#r
#k
#discussion problem 3 c, the output would be "M ss ss pp"
#discussion problem 3 e, the output would be " tfdsfu"

#4.4 problem 4,Write a program that uses five definite loops to produce the following single line of output exactly as specified below: grades = "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFDDDDDDDDDDCCCCCCCCCCBBBBBBBBBBAAAAAAAAAA"
#I used len() to find how many of each letter in an interactive python shell.
#each loop prints the specified letter the number of times in the range. end='' keeps it on one line. Print('"') prints parentheses at the end.
def main():
    print('grades="', end='')
    for i in range (60):
        print ("F",end='')
    for i in range(10):
        print ("D",end='')
    for i in range(10):
        print ("C",end='')
    for i in range(10):
        print ("B", end='')
    for i in range(10):
        print ("A", end='')
    print('"')
    
#4.5, chapter 5 programming exercise 3.
#This program creates a string where 0-59 corresponds to F, 60-69 to D, 70-79 to C, 80-89 to B, 90-100 to A.
#The result is essentially the output of the above problem. Therefore, for every number entered the string index, grades[n], writes the letter than corresponds to the range given.
#the int keeps it as an integer.    
def main():
    grades = 60*"F" + 10 * "D" + 10 * "C" + 10 * "B" + 10 * "A"
    n = int(input("enter a number grade"))
    print("your letter grade is", grades[n])

#4.6, chapter 5 programming exercise 4.
#Phrase is an input and a string. Acronym is phrase split between the spaces in the words.
#Final is a string varibale that is meant to be empty.
#In the loop, the first letters that have been stored in 'acronym' are sliced off
#each letter is saved and added to the empty 'final'.
#.upper captilizes all letters. final is printed as the empty variable plus each capitalized letter.
def main():
    phrase = str(input("please enter a phrase"))
    acronym = phrase.split()
    final = ""
    for i in acronym:
        final = final + i[0].upper()
    print("the acronym is", final)

#4.7, chapter 5 programming exercise 5.
#this program first asks for an input "name." It then defines "total" as 0. It then loops for each letter in "name" and adds each letter to the total "0"
#ord returns the numerical code of each letter, which start at a=97. Therefore, the value of each number needs to have 96 subtracted from it in order for it to correspond to a=1, b=2, etc.
#Essentially, the program is returning the numerical value of each letter in a loop, subtracting 96 from each value, and adding each final value to 0 then printing the final number   
def main():
    name = input("please enter your name ")
    total = 0
    for ch in name:
        total = total + (ord(ch)-96)
    print(total)
