#needed in quick_check()
import time 
 
#valid operations for comparison 
valid_oper = ["+","-","*","/"]

#decribes function and limitations of program
def welcome_message():
    print("\n"*20)
    print("WELCOME TO OUR CALCULATOR!\n")
    print("*   *   *   *   *   *   *   *   *   *   *   *   *\n")
    print("We can add, subtract, multiply or divide any two numbers.\n\n")
    first_number()

#input first number    
def first_number(): 
    global num1
    num1 = int(input("Please enter your first number:\n"))
    if num1 == 0:
        print("ERROR: Please enter a numeric value not equal to 0\n")        
        first_number()    #tries again for correct value
    else:
        operator()

#input, check and store operator    
def operator(): 
    global oper
    oper = input("ENTER + , - , * or / \n")
    #checks the valid_oper list for correct value
    if oper not in valid_oper:    
        print("\nERROR: Please enter the one of the symbols: + , - , * or / \n")
        operator()
    else:
        second_number()

#input second number        
def second_number():
    global num2
    num2 = int(input("Please enter your second number:\n"))
    if num2 == 0:
        print("\nERROR: Please enter a numeric value not equal to 0\n")
        second_number()
    else:
        calculation()

#calculates based on operator input
def calculation():
    global calc
    if oper == "+":
        calc = num1 + num2 #add
        quick_check()
    elif oper == "-":
        calc = num1 - num2 #subtract
        quick_check()
    elif oper == "*":
        calc = num1 * num2 #multiply
        quick_check()
    elif oper == "/":
        calc = num1 / num2 #divide
        quick_check()
    else:
        #this should logically never happen
        print("\nERROR: Calculation failed. Please try again.\n")
        welcome_message()

#accuracy check, and reminder of what user entered.        
def quick_check():
    print("\n\nCalculating " + str(num1) + oper + str(num2) + "...\n")
    time.sleep(1)    #waits for one second for dramatic effect
    print(calc)      #displays answer


#starts the program!
welcome_message()