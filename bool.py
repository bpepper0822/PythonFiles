# imports the time module for fancy effects using 'time.sleep()'
import time

# prints 30 lines
def clear_screen():
    print("\n"*30)

# comparison function that all answers run through
def compare(a,b):
    print("Comparing ", a, " and ", b, "...")
    time.sleep(.7)      # Waits 0.7 seconds
    if a > b:
        return 1
    elif a == b:
        return 0
    elif a < b:
        return -1
    else:
        return "ERROR: Please enter numeric values only!"      #for typos and anything else that might break

# * *__main__ starts here * * 

# prints 30 lines
clear_screen() 

print("Welcome to our number comparison tool!\nWe will compare two numbers.\n")

print("If the first number is larger, I'll display a 1\n")

print("If the second number is larger, I'll display a -1\n")

print("If both numbers are the same, I'll display a 0\n\n")

#user inputs numbers
num1 = input("Please enter the first number to compare\n")
num2 = input("Please enter your second number\n")

# prints 30 lines    
clear_screen()    

print(compare(5,2))

print(compare(2,5))
      
print(compare(3,3))

# Recalls the inputs
print(compare(num1,num2))      
      
