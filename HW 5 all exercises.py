#HW 5.1
#this program defines 5 functions for five animals. It then calls each function with the specific parameter
#it then prints each verse of Old MacDonald with each animal and its corresponding noise
#the parameter is inserted depending on what is put in the (" ")
def farm():
    print("Old Macdonald had a farm, Ee-Igh, Ee-igh, Oh!") 
def First_Verse(animal):
    farm()
    print("And on that farm he had a", animal + ", Ee-Igh, Ee-igh, Oh!")#the parameter is animal, which is placed in the string 
def Animal_Sound(sound): #sound is the parameter that is added to the text 
    print("With a", sound + ",", sound + " here and a", sound + ",", sound + " there. Here a ", sound + " there a", sound + ", everywhere a", sound + ",", sound)
    farm()
def main1():
    First_Verse("cow")
    Animal_Sound("moo")

    First_Verse("horse")
    Animal_Sound("neigh")

    First_Verse("cat")
    Animal_Sound("meow")

    First_Verse("pig")
    Animal_Sound("oink")

    First_Verse("sheep")
    Animal_Sound("ba")

#HW 5.2
#the input is the number of numbers, which is then the parameter for how many times the loop in avergae() will prompt
#in average(), the total is a variable that is set at 0 and then adds to 0 each of the inputs in the range of numbers
#it then returns the average which is total/numbers, which is defined as final in main(). Final is then printed

def main2():
    numbers = input("how many numbers do you want to sum? ") #number of times it will be summed
    final = average(int(numbers)) #defines the average with the parameter of numbers as final 
    print("the average of your numbers is " + str(final)) #prints final as a string
    
def average(numbers):
    total = 0 #start at 0
    for i in range(numbers):
        total += int(input("please enter a number ")) #definite loop that adds the input to the variable total
    return total/numbers #returns the value of the total divided by the input in main

#HW 5.3
#this program first gets x1, y1, x2, y2 and calculates dx and dy
#it then calls slope(dx,dy) which returns the slope to main3()
#it then calls distance(dx,dy) and returns the distance between the points to main3()
#the slope and distance are printed

import math
def main3():
    x1 = int(input("Please enter x1 in (x1, y1) ")) 
    y1 = int(input("Please enter y1 in (x1, y1) "))
    x2 = int(input("Please enter x2 in (x2, y2) "))
    y2 = int(input("Please enter y2 in (x2, y2) "))
    dx = x2-x1 #formula
    dy = y2-y1 #formula
    main_slope = slope(dx, dy) #calling slope() with dx and dy as the parameters
    main_distance = distance(dx, dy) #calling distance() with dx and dy as the parameters 
    print(str("The slope is " + main_slope))
    print(str("The distance between the coordinate pairs is "+main_distance))
    
def slope(dx, dy):
    return str(dy/dx)#returns the value of dy divided by dy, which is the slope formula. dx and dy obtained in main     

def distance(dx, dy):
    return str(math.sqrt(dx**2 + dy**2))#returns the value of the distance formula

#HW 5.4
#this program has an established list defined as my_list
#total_list is defined as the sum of my_list
#total list is printed
def main4():
    my_list = [8,3,1,9] #list
    total_list = sum(my_list) #summing the list and naming it total_list
    print(total_list) #printing the sum

#HW 5.5
#this program returns a list of strings that are obtained from the input
def main5():
    number = int(input("How many strings? ")) #how many times the loop will be executed 
    string_final = get_some_strings(number) #naming the function get_some_strings
    print(string_final) #printing the list of strings
    
def get_some_strings(number):
    string_list = [] #empty list to start
    for i in range(number): #definite loop, number obtained from input in main
        x = input("please enter a string ") 
        string_list.append(x) #stores and adds together the strings 
    return string_list #returns the list 
        
    
