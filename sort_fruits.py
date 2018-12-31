# Creating empty lists
fruit = []
sort_fruit = []
sorted_fruit = []
# Opening source file, then creating new empty file for sorted fruits
old_file = open("E:/Desktop/UoPeople/IntroProgramming/unsorted_fruits.txt", "r")
new_file =  open("E:/Desktop/UoPeople/IntroProgramming/sorted_fruits.txt", "w+")

# Reads original file into list 'fruit'. Each line becomes new list item
fruit = old_file.readlines()

# Copies all lines that aren't empty to new list 'sort_fruit' for sorting
for each in fruit:
    if each != "\n":
        sort_fruit.append(each)

##########################
# SORTING LOOP STARTS HERE
##########################

while len(sort_fruit) > 0:                  # While there are still items in sort_fruit...
    for each in sort_fruit:
        if each == min(sort_fruit):         # Identifies the minimum value (closest to 'a')
            sorted_fruit.append(each)       # Adds value to empty list 'sorted_fruit'
            sort_fruit.remove(each)         # Removes value from list 'sort_fruit"
        else:
            pass    

# Prints the sorted_fruit list as a string, then writes it to the new file 'sorted_fruits.txt' created on line 7
print(''.join(sorted_fruit))
new_file.write(''.join(sorted_fruit))

# Closes both .txt files
old_file.close()
new_file.close()