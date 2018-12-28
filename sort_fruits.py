sort_fruit = []
sorted_fruit = []

old_file = open("E:/Desktop/UoPeople/IntroProgramming/unsorted_fruits.txt", "r")
new_file =  open("E:/Desktop/UoPeople/IntroProgramming/sorted_fruits.txt", "w+")

fruit = old_file.readlines()

for each in fruit:
    if each != "\n":
        sort_fruit.append(each)       

while len(sort_fruit) > 0:    
    for each in sort_fruit:
        if each == min(sort_fruit):
            sorted_fruit.append(each)
            sort_fruit.remove(each)
            new_file.write('%s' % each)
        else:
            pass    

print(sorted_fruit)
