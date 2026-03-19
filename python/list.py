                          #LIST         #Lists are mutable
#A list stores multiple values in one variable.
               #Syntax:
# list_name = [value1, value2, value3]

numbers = [1, 2, 3, 4, 5]
print(numbers)

data = [10, "Python", True, 3.5]
print(data)

                           #Indexing
numbers = [10, 20, 30, 40]
print(numbers[0])

numbers = [10,20,30,40]
print(numbers[-1])

                           #Slicing
#Slicing extracts a part of the list.
              # Syntax:
# list[start:end]

numbers = [10,20,30,40,50]
print(numbers[1:4])

numbers = [10,20,30,40,50]
print(numbers[:3])
print(numbers[2:])

                            #append()
numbers = [1,2,3]
numbers.append(4)
print(numbers)

                            #insert()
#Adds an element at a specific position.
               #Syntax:
#  list.insert(index, value)

numbers = [1,2,4]
numbers.insert(2,3)
print(numbers)

                            #remove()
# Removes a value from the list.

numbers = [1,2,3,4]
numbers.remove(3)   #remove() removes the value, not the index
print(numbers)


                            #Iterating Through a List
numbers = [10,20,30]
for n in numbers:
    print(n)

numbers = [1,2,3]
numbers.append(4)
numbers.insert(1,10)
numbers.remove(3)
for n in numbers:
    print(n)

                            #len()
numbers = [10,20,30,40]
print(len(numbers))

                            #in Operator
#Used to check if an element exists in the list.

numbers = [10,20,30]
print(20 in numbers)  #output : TRUE
print(50 in numbers)  #output : FALSE

                            #Modifying List Elements
    #Lists are mutable, meaning you can change values

numbers = [10,20,30]
numbers[1] = 25
print(numbers)

numbers = [10,20,30] 
numbers.append(40)
numbers[1] = 25
print(len(numbers))
print(numbers)

                            #pop()

        # pop() removes an element from the list.

numbers = [1,2,3,4]
numbers.pop() # Remove last element
numbers.pop(1) # Remove element at index
print(numbers)

n=[10,30,40,20]
x=n.pop() # pop() can also return removed value
y=n.pop(1)
print(x) #output : 20
print(y) #output : 30

