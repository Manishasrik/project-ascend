# INTEGER

age= 12
quantity = 5
player=4

print(f"your age is : {age}")
print(f"in total there are {quantity} items")
print(f"in the team there are {player} players")

# FLOAT
 
price=10.99
gpa=3.0  # even if the decimal value is 0 its still float
distance=12.5

print(f"the apples are {price} dollars")
print(f"i scored {gpa} gpa in last sem ")
print(f"the hotel is {distance} KM away from here")

# STRING

"""Strings are sequence of characters within quotes"""
name= "lexi"
place="LA"
email="lexi202gmail.com"  #it can also contain numbers as long as its within the quotes

print(f"The student {name} is from {place}")

# BOOLEAN

on=True    # Boolean values does not need ""(Ex: x=True) unlike strings (Ex: x="on")
off=False
inside=False
out=True

print(f"on:{on},off:{off}")

if inside:  #boolean is commonly used in conditions here the elif part will print cause out=True so as in conditions when its true it gets executed
    print("its in")
elif out:
    print("its out")
else:
    print("nothing")