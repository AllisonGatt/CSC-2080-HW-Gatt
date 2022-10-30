#HW 3.1, chapter 3 programming exercise 13
#the program will first prompt for how many numbers
#total is defined as 0
# a loop set by the input above is begun where the user is promted for a number each time
# each number entered is defined as n
# each n is added to the total
# the new total is printed

def main():
    numbers = int(input("how many numbers to sum? "))
    total = 0
    for x in range(numbers):
        n = int(input("enter a number"))
        
        total =  total + n 
    print("the sum is", total)
#how many numbers to sum? 5
#enter a number 13
#enter a number 12
#enter a number 14
#enter a number 2
#enter a number1
#the sum is 42

#HW 3.2 chapter 3 programming exercise 14
# the program prompts the user for how many numbers
# total is defined as 0
# a loop is created in the range of how many numbers, each time promting the user for a number(n)
# the program then adds the numbers(n) together
# the total dived by the original input is printed. It is // so that it will be an integer
def main():
    numbers = int(input("how many numbers to sum? "))
    total = 0
    for x in range(numbers):
        n = int(input("enter a number"))
        
        total =  total + n 
    print("the average is", total//numbers)
    
#how many numbers to sum? 4
#enter a number 5
#enter a number 6
#enter a number4
#enter a number3
#the average is 4

from graphics import *

#HW 3.3 chapter 4 discussion problem 2
# a Point(130,130) will draw a point in the upper part of the lower right quadrant (with p.draw)
# b will draw a medium blue circle with a red outline in the upper left quadrant
# c will draw a small green square/rectangle with a thick black outline in the upper left quadrant
# d will draw a red arrow whose point is in the middle of the window and whose neck/line begins at the bottom
# e will draw a very thin, black oval in the middle left portion of the window
# f will draw a very small, orange hourglass shape with a black outline in the uppermost left corner of the window 
# g will draw "hello World!" just barely below the middle of the window in size16 font and initalics

#HW 3.4 chapter 4 discussion problem 3
#this program draws a red circle that starts at the coordinates (50,50) with a radius of 20
#the user can move the circle to different coordinates in the window up to ten times by left clicking on the window  

#given program:
from graphics import *

def main():
   win = GraphWin()
   shape = Circle(Point(50,50),20)
   shape.setOutline("red")
   shape.setFill("red")
   shape.draw(win)
   for i in range(10):
       p=win.getMouse()
       c=shape.getCenter()
       dx=p.getX() - c.getX()
       dy = p.getY() - c.getY()
       shape.move(dx,dy)
       win.close

#HW 3.5 Chapter 4 programming exercise 2
# this program draws a target by drawing consecutive circles, starting with c1
# each circle's radius is 10 more units than the last

from graphics import *

def draw_square(win):
    rect = Rectangle(Point(30, 10), Point(10, 30))
    rect.draw(win)
def draw_line(win):
    line= Line(Point(40,20), Point(80,20))
    line.draw(win)
def main():
    win = GraphWin()
    c5=Circle(Point(90,90),50)
    c5.setFill("white")
    c5.draw(win)
    c4=Circle(Point(90,90),40)
    c4.setFill("black")
    c4.draw(win)
    c3=Circle(Point(90,90),30)
    c3.setFill("blue")
    c3.draw(win)
    c2=Circle(Point(90,90),20)
    c2.setFill("red")
    c2.draw(win)
    c1=Circle(Point(90,90),10)
    c1.setFill("yellow")
    c1.draw(win)
    draw_square(win)
    draw_line(win)
main()

#HW 3.6 chapter 4 prgramming exercise 3
#this program draws a yellow face that looks somewhat like " :/ " but with a straight line

from graphics import *

def main():
    win=GraphWin()
    c1=Circle(Point(100,100),50)
    c1.setFill("yellow")
    c1.draw(win)
    c2=Circle(Point(70,90),5)
    c2.setFill("black")
    c2.draw(win)
    c3=Circle(Point(130,90),5)
    c3.setFill("black")
    c3.draw(win)
    l=Line(Point(70,120),Point(130, 120))
    l.draw(win)
main()

#HW 3.7 chapter 4 programming exercise 8
# this program first prompts for the user to click the window in two spots
# these become p1=(x1,y1) and p2=(x2, y2), or p1=(p1.getX, p1.getY) p2=(p2.getX, p2.getY)
#the program then draws a black line from p1 to p2
#the program then calculates the midpoint coordinates (mpx, mpy)and then creates a cyan circle from mpx and mpy
#the length is then calculated using the distanc formula with the above points and printed
#the slope is then caluclated using the slope formula with the above points and printed

from graphics import *
import math

def main():
    print("please click the window in two different spots")
    win = GraphWin()
    p1=win.getMouse()
    p1.draw(win)
    p2=win.getMouse()
    p2.draw(win)
    l=Line(p1, p2)
    l.setOutline("black")
    l.draw(win)

    mpx=(p1.getX()+p2.getX())/2
    mpy=(p1.getY()+p2.getY())/2

    c=Circle(Point(mpx,mpy),5)
    c.setFill("cyan")
    c.draw(win)
    
    length= float(math.sqrt((p1.getX() - p2.getX())**2 + (p1.getY()-p2.getY())))
    print("the length of the line segement is ", length)

    slope = float(p2.getY()-p1.getY()/p2.getX()-p1.getX())
    print("the slope of the line segment is ", slope)
