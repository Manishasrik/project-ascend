# Type Conversion - Changing one type of data to another type

# Implicit Type Conversion - Python automatically converts one data type into another without you writing the conversion

n1=10 #int
n2= 10.1 #flaot
n3=n1+n2
print(type(n3)) # output : <class 'float'> 
                # python always convert smaller data type to larger data type 
"""
 Hierarchy of data's in Implicit Type Conversion:
                1.complex
                2.float
                3.int
                4.boolean
        Example:
                int + float → float
                int + complex → complex
                bool + int → int
        Python moves the smaller type up the ladder.
                bool
                 ↓
                int
                 ↓
                float
                 ↓
                complex
When Python mixes different numeric types in an operation, it automatically converts the smaller type into the larger type in this order
"""

x = 5
y = 2.5
print(x + y) # Python automatically converts: 5 → 5.0   #Then performs: 5.0 + 2.5 = 7.5

#Boolean in Arithmetic

print(True + 5) #1+5 = 6 as we know python converts smaller data type into larger data type
"""True = 1
False = 0"""

#Integer with Complex Numbers

x = 5
y = 2 + 3j # Python converts: 5 → 5+0j
print(x + y)# Result: 7 + 3j


# Explicit Type Conversion - user converts the data type manually 

"""
Explicit conversion is needed for:
        string ↔ numbers
        float → int
        input values
        number → string"""

a = input("Enter number: ")
b = input("Enter number: ")
print(a + b)   # Output : ab cause in python input values are strings

a = int(input("Enter number: "))
b = int(input("Enter number: "))
print(a + b) # Output :a+b cause now we have changed the value into integers

age = 21
print("Age: " + str(age)) # print("Age: " + age) <- this will show error cause we cannot concatinate values of different data types

price = 99.8
price = int(price) # output : 99

x = "10"
y = "5"
print(x + y) # 105

print(int(x) + int(y))# 15

                          # type()
"""
type()  → detective (checks type)
int()   → converter
float() → converter
str()   → converter
bool()  → converter
"""
x = 10
print(type(x))

print(type(float(5)))
print(type(int("5")))

x = "10"
y = int(x)
print(type(y))