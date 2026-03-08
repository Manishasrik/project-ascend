#A function is a block of code that performs a specific task

                           #defining a function
def name():  #def is the key word to create a function and name is the name of the function
    print("name function is running")


                           #calling the function
name() #calling the function  # Defining a function does not run it. You must call it.


                           #Functions with Parameters
# Parameters allow a function to receive input values
def name(a):     #Parameter = a
    print(a)
name("Manisha")  #Argument = Manisha


       #Default Argument
def name(a="Sri"):
    print(a)
name()
name("Manisha")

                  #return
def add(a,b):
    return a+b   #send result back

x=int(input("Enter a number:"))
y=int(input("Enter a number:"))
r= add(x,y)
print(r)

                          #LAMBDA FUNCTION

#A lambda function is a small anonymous function.
"""
                 Syntax
     lambda parameters : expression
 """

add=lambda a,b:a+b #lambda function

print(add(2,2))