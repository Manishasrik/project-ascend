# A variable is a container that stores data.

# METHOD 1
age=19
name="Manisha"  # we need to add "" for string values
height=162

print(age)
print(name)
print(height)

# METHOD 2
age,name,height,weight =19,"Manisha",162,63
print(age,name,height,weight)

#printing a variable 

print("you are",age,"years old")
print(f"you are {age} years old")  #f-string 
print("you are"+str(age)+"years old")