celsius_list = [] #empty list to be used later
total_temps = 5 #number of temperatures to convert

def temp_convert(f):
    c = ((f-32)*5)/9
    return round(c, 2) #rounds the celsius value to a reasonable length

while total_temps > 0:    
    celsius_list.append(temp_convert(float(input("Enter a temperature in fahrenheit\n")))) #gets numeric value from input, runs function, adds result to list
    total_temps -=1

print(celsius_list) #prints a list of the new values in the order you input them    