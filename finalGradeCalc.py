'''
Created on Mar 7, 2020

@author: ITAUser
'''
#statements welcoming and explaining program
print ("Welcome to the final grade calculator!")
print ("Use this resource to calculate what grades you need on your finals for the grades you want (:")
userChoice = input("press 's' to start: ")

#while loop so that program runs continuously and multiple calculations can be done
if (userChoice == "s"):
    contCalculating = True
    while (contCalculating == True):
        
        #asks user for information 
        course = str(input("Course?: "))
        goal = float(input("Goal?: "))
        current = float(input("Current grade?: "))
        weight = float(input("final exam weight?(enter as decimal): "))
      
        #function to do calculations calls to print results
        def gradeNeeded():
            val1 = 1-weight
            val2 = current*val1
            val3 = goal-val2
            val4 = val3/weight
            return val4
        result = gradeNeeded()
        print(course)
        print (result)
        
        #provides message based on what grade they'll need
        if (result < 30):
            print("don't even study")
        elif (result < 70):
            print("don't stress")
        elif (result < 80):
            print("you'll do great(:")
        elif (result < 100):
            print("you got this!")
        else:
            print("be realistic")
            
        userChoice = input("press enter for another class or q to quit: ")  
        
        if (userChoice =="q" ):
            print("thanks for using the final grade calculator!")
            break
    