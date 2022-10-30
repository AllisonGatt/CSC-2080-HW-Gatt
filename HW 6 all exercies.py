#HW 6.1 chapter 7 discussion problem 2
#When try is used, the program goes down everything from try until an error occurs and then
#control is passed to the except clause. When if is used, the only lines of code that are executed
#are those nested in the if clause when the if comparision is true. Otherwise, the lines of code in
#the else clause (if it is there) will be executed.
#Errors will still cause the program to crash with the if statement if the if statement does not
#adress them properly. A try statement will cause the program not
#to crash but rather to go right to except and execute what is under except.
#Both cause the program to make decisions.
#Essentially, the try/except is used to capture any error whereas the if captures a specific error,
#but both do capture errors.


#HW 6.2 chapter 7 programming exercise 3
def main_grade():
    grade_number = int(input("Enter your number grade "))
    
    grade_letter = grade_number//10 #this gives an integer that will be just the first number and not rounded
    
    if grade_letter < 6: #if the above calculation gives anything below 6 this will run
        print("Your letter grade is F")
    elif grade_letter == 6: #if the calculation gives 6 this will run 
        print("Your letter grade is D")
    elif grade_letter == 7: #if the calculation gives 7 this will run 
        print("Your letter grade is C")
    elif grade_letter == 8: #if the calculation gives 8 this will run 
        print("Your letter grade is B")
    elif grade_letter == 9: #if the calculation gives 9 this will run 
        print("Your letter grade is A")
    elif grade_letter == 10: #if the calculation gives 10 this will run 
        print("Your letter grade is A")
    else:
        print("Something went wrong, make sure you ender your grade as a number") #if none of the above conditions are met something went wrong and the number should be re-entered
#Hw 6.3, chapter 7 programming exercise 7

def main_payrate():
    print("All time values must be in military time ") 
    start = str(input("Please enter your start time "))
    start_hour = start.split(":")[0] #splits the entered time at the ':' and takes the first position, which is the hour
    start_minute = start.split(":")[1] #splits the entered time at the ':' and takes the second position, which is the minute
       
    end = str(input("Please enter your end time "))
    end_hour = end.split(":")[0]
    end_minute = end.split(":")[1]

    if int(start_hour) >= 21: #since it is a single 24 hour period, if the start time is after 9 the end time will be as well
        x_after = float(start_minute)/60 #gives the minutes in a decimal format, float so that there can be decimals
        start_after = int(start_hour)+ x_after #gives start hour+minutes in decimal format so they can be added properly
        
        y_after = float(end_minute)/60 #same as above but for the end minutes
        end_after = int(end_hour)+ y_after #same as above but for the end hour+minutes

        after_total = float(end_after)-float(start_after) #gives the amount of hours and minutes. Float is used so that it stays as a decimal but still able to use subtraction
        
        print(float("Your paycheck is " (after_total)*1.75))#total of hours and minutes in decimal form times the after 9 rate
        
    elif int(end_hour) >= 21:
        x_before = float(start_minute)/60 #finding the decimal value of the minutes
        start_before = int(start_hour)+ x_before #addin that to the hour value. Int since the hour cannot be a fraction
        
        y_after = float(end_minute)/60 #finding the decimal minutes for the end after 9
        end_after = int(end_hour)+ y_after #adding the decinal minutes to the hour
        after_amount = float(end_after)-21.00 #finding the amount of hours worked after 9.
        #21:00 is 9 in military time, so taking the imput and subtracting 21 from it gives the amount of hours worked after 9
        
        pay_before = 2.5*(21.00-float(start_before)) #subtracting the starting hour and minutes (decimal) from 21 to find how many hours worked before 9. Multiplying it by the before 9 rate
        pay_after = 1.75*(float(after_amount))#the after_amount was found above. Multiplying it by after 9 rate
        pay_total = float(pay_after)+float(pay_before) #the before 9 pay plus the after 9 pay to give the final pay
        print("Your  paycheck is ", pay_total)                
    
    else: #if both start and end times are before 9
        start_x = float(start_minute)/60 #float so there can be division with decimals 
        start_after = int(start_hour)+ start_x #start hour + minutes
        
        end_y = float(end_minute)/60 #same as above but for the end
        end_after = int(end_hour)+ end_y #same as above but for the end

        after_total = float(end_after)-float(start_after) #total of hours and minutes with minutes in decimal format
        
        print(float("Your paycheck is " (after_total)*2.50)) #total times the before 9 rate
        
#HW 6.4 chapter 7 programming exercise 8

def main_eligibility():
    age = int(input("How old are you? ")) #int is used to avoid floats. The error was: "'>=' not supported between instances of 'str' and 'int'"
    citizenship = int(input("How long have you been a citizen of the US? "))

    if age >= 30 and citizenship >=9: #decision struction, if the requirements are met it will print, if not it goes on to elif
        print("You are eligible to be a US senator and a US representative")
    elif age >= 25 and citizenship >=7: #decision struction, if requirements are met it will print, if not it goes on to else. Elif is else+if. 
        print("You are only eligible to be a US representative")
    else: #if none of the above requirements are met else prints
        print("You are not eligible to be a US senator or a US representative")

#HW 6.5, redo of chapter 4 programming exercise 8
import math

def main_redo():
    x1 = input("Please enter x1 in (x1, y1) ")
    y1 = input("please enter y1 in (x1, y1) ")    
    x2 = input("Please enter x2 in (x2, y2) ")    
    y2 = input("Please enter y2 in (x2, y2) ")
        
    try: #this is solving for the error that would occur if a letter was put in since a letter is a string that could not be evaluated
        x1 = int(x1)#check if it is an int, if not it goes to the except
        y1 = int(y1)#same^
        x2 = int(x2)#same^
        y2 = int(y2)#same^
        if x1==x2: #solving for the error of division by zero. If x1=x2, then it will equal 0 in dx. It will print that there is no slope but still calculate distance
            print("There is no slope for these coordinates")
            dx = x2- x1 
            dy = y2- y1
            main_distance = distance(dx, dy) #calling distance() with the parameters dx and dy
            print(str("The distance between the coordinate pairs is "+ main_distance))
        else: #if x2 and x1 are not equal, the program will coninue normally
            dx = x2-x1 
            dy = y2-y1
            main_slope = slope(dx, dy)#calling slope() with dx and dy as the parameters
            main_distance = distance(dx, dy) #calling distance() with dx and dy as the parameters
            print(str("The slope is " + main_slope))
            print(str("The distance between the coordinate pairs is "+ main_distance))
    except: #if something in the try goes wrong (a letter is entered) only this is printed. 
        print("Only numbers are accepted")
    
   
def slope(dx, dy):
    return str(dy/dx)#returns the value of dy divided by dy, which is the slope formula. dx and dy obtained in main     
                    #needs to be a string for decimals 
def distance(dx, dy):
    return str(math.sqrt(dx**2 + dy**2)) #math was imported so the distance formula can be used. math.sqrt is square root and ** is exponents




  
 
