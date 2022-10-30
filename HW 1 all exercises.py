#HW 1.2, chapter 1 exercise 1
print("hello, world!")
print("hello", "world!")
#part a prints hello world with a comma between, part b prints hello world without a comma
print(3)
print(3.0)
#part c prints 3 alone, part d prints 3.0
print(2 + 3)
print(2.0 + 3.0)
print("2" + "3")
#e prints just 5, f prints 5.0, g prints 23
print(2 * 3)
print(2 ** 3)
#i prints 6 j prints 8
print(7/3)
print(2//3)
#k prints 2.33333333333333335, print(2//3) prints 0

#HW 1.3, chapter 1 exercise 5
#file: chaos.py
#A simple program illustrating chaotic behavior
def main():
    print("this program illustrates a chaotic function")
    x = eval(input("enter a number between 0 and 1:"))
    n = eval(input("how many numbers should I print? "))
    for i in range(n):
        x = 3.9 * x * (1-x)
        print(x)
#HW 1.4, chapter 2 exercise 10
# a program that converts distance measured in kilometers to miles
#1 km = 0.62 miles
def main():
    kilometers = eval(input("how many kilometers?")) #input
    miles = 0.62 * kilometers #conversion
    print("The distance is", miles, "miles") #printing conversion
#HW 1.5, chapter 2 exercise 5
#interest
def main():
    t = eval(input("how many years?"))#input
    p = 10000 #given
    n = 12 #given
    r = 0.08 #given
    A = p*(1+(r/n))**(n*t) #equation and calculation
    print("The amount is", A) #printing calculation

