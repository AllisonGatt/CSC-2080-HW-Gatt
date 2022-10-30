#HW 7.1 chapter 8 discussion problem 1 (all)
#Compare and contrast the following pairs of terms:
#a) definite loop vs. indefinite loop
# In a definite loop, the number of iterations is determined before the loop even starts,
#therefore the number must already be known. In an indefinite loop, the number of iterations
#will continue until a certain condition is met. They both are loops that do not require
#direct interaction with the user while the loop is being iterated.

#b) for loop vs. while loop
#The for loop is a definite loop that will iterate a predetermined number of times.
#The while loop is an indefinite loop that iterates until a predetermined condition
#is met. Again, they are both loops that are not interactive.

#c) interactive loop vs. sentinel loop
#An interactive loop iterates as long as the user continues to prompt it to do so.
#The number of iterations is dependent on the user either repeating the loop or stopping it.
#A sentinel loop on the other hand allows the user to continue to ender data until a special
#value(or sentinel) is entered. Where the interactive loop will ask each time if the loop should
#iterate, the sentinel does not ask. It will end when the sentinel is entered. Both are loops whose
#number of iterations are dependent on the user in the loop itself and thus are called interactive.

#d) sentinel loop vs. end -of-file loop
#A sentinel loop will iterate with values that are entered by the user and will end once the sentinel.
# is entered. The end -of -file loop iterates values that are in a specific file that is entered by the
#user. Similar to the sentinel loop, it will end once a specific value is returned. Both loops iterate
#until the sentinel is entered or returned. 

#HW 7.2 chapter 8 discussion problem 2 (all)
#Give a truth table that shows the Boolean value of each of
#the following Boolean expressions,
#for every possible combination of "input" values.
#Hint: Including columns for intermediate expressions is helpful.

#a) not (P and Q)
# P | Q | not (P and Q)
# T | T | F
# T | F | T
# F | T | T
# F | F | T

#b) (not P) and Q
# P | Q | (not P) and Q
# T | T | F
# T | F | F
# F | T | T
# F | F | F

#c) (not P) or (not Q)
# P | Q | (not P) or (not Q)
# T | T | F
# T | F | T
# F | T | T
# F | F | T

#d) (P and Q) or R
# P | Q | R |(P and Q) or R
# T | T | T | T
# T | T | F | T
# T | F | T | T
# T | F | F | F
# F | T | T | T
# F | T | F | F
# F | F | T | T
# F | F | F | F

#e) (P or R) and (Q or R)
# P | Q | R |(P or R) and (Q or R)
# T | T | T | T
# T | T | F | T
# T | F | T | T
# T | F | F | F
# F | T | T | T
# F | T | F | F
# F | F | T | T
# F | F | F | F

#HW 7.3 chapter 8 discussion question 3 (a) and (c).
#Write a while loop fragment that calculates the following values:
#a) Sum of the first n counting numbers: 1 + 2 + 3 + ... + n

    #initial = 0
    #x = 0
    #while initial <= n: #n is the number of counting numbers summed, and must be defined elsewhere
        #initial = initial + 1 #adding 1 to 0 to get 1, then adding 1 to 1 to get 2 and so on
        #x = x + initial #adding 1 to 0 to get 1, adding 1 to 2(initial)
        #print(x)

#c) Sum of a series of numbers entered by the user until the value 999 is
#entered. Note: 999 should not be part of the sum.

    #summation = 0.0 #start at 0.0 so numbers can be added
    #x = float(input("Please enter a number to sum, or 999 to quit "))
    #while x != 999: #!= means not equal, thus the loop will terminate if 999 is entered
        #summation = summation + x #adding input to 0.0
        #x = float(input("Please enter a number to sum, or 999 to quit ")) #senteniel
    #print("The sumamtion of the numbers is", summation) #prints once senteniel is entered
              


#HW 7.4 chapter 8 programming exercise 1

def main_fibonacci():
    a = 1
    b = 1
    f = 1
    count = 3 #since the addition starts after the first two numbers in the sequence
    n = int(input("Please enter the nth Fibonacci number you would like "))
    while count <= n: #loop ends if the count is greater than the desired number in the Fibonacci sequence
        f = a + b #f is the Fibonacci number
        a = b #a becomes b
        b = f #f = a + b, and this value becomes b
        #when a = 1 b = 1 and f = 2. The loop iterates and a = 1 (since a=b) b = 2 (since b=f) and f = 3, etc.
        count = count + 1 #the Fibonacci sequence number 
        
    print(f)

main_fibonacci()

#HW 7.5 chapter 8 programming exercise 4.
#Write a program that gets a starting value from the user and then prints
#the Syracuse sequence for that starting value.

def main_syracuse():
    x = int(input("Please enter a natural number ")) 
    print(x) #first number in sequence

    y = x/2 #finding if input is even
    if y == int(y): #if even is true then this calculation is done
        s = y #y is defined above
    else:
        s = int((3*x) +1) #if odd then this calculation is done
    print(int(s))  #second number of sequence
    
    while s > 1: #if the first calculation =1 this will not run. Iterates until s = 1
        if s/2 == int(s/2): #if this is true the number is even 
            s = s/2  #calculation 
        else:
            s = int((3*s)+1) #calculation

        print(int(s)) #int so output is only natural numbers, finishes sequence 

main_syracuse()
