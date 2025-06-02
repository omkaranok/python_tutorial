#String data type

#literal assignment
first = "Dave"
last = "Gray"
# print(type(first))
# print(type(last) == str)
# print(isinstance(first, str))

#constructor function
# pizza = str("Pepperoni")
# print(type(pizza))
# print(type(pizza) == str)
# print(isinstance(pizza, str))


#Concatenation
fullname = first + " " + last
print(fullname)
fullname += "!"
print(fullname)

#TypeCasting a number to string
decade = str(2020)
# print(type(decade))
# print(decade)
# var = True
# print(type(var))

statement = "I like rock music from the " + decade + "s"
print(statement)
print(type(statement))

#multiline lines
multiline = '''
Hey,My name is Om
This is a multiline string.
         All good
         '''
print(multiline)

#Esacping special characters we can put special character in our sentences using backlash
escaped = 'I\'m back at work!\tHey!\n\nWhere\'s this at \\located?'
print(escaped)

#methods on strings
print(first)
print(first.upper())
print(first.lower())
print(first)

print("repalicng")

first = first.upper()
print(first)

print(multiline.title())
print(multiline.replace("ok","ok"))
print(multiline)
print(len(multiline))  #length of string
multiline += "                         "
multiline = "            " + multiline
print(len(multiline))  #length of string


####Remove whitespace
# print(len(multiline.strip()))  #remove whitespace from both ends
# print(len(multiline.lstrip()))
# print(len(multiline.rstrip()))

# print("Hello world") if 8 > 10 else print("Goodbye world")

#Build a menu
title = "menu".upper()
print(title.center(20,"="))
print("Coffee".ljust(16,".") + "$1".rjust(4))
print("Muffin".ljust(16,".") + "$2".rjust(4))
print("Cheesecake".ljust(16,".") + "$4".rjust(4))

##string index values
print(first[0])
print(first[-1])
print(first[1:-1])   #it will not provide the range 
print(first[1:])

#Some methods return boolean data
print(first.startswith("D"))
print(first.endswith("e"))

#boolena data type 
myvalue = True
print(type(myvalue))
x= bool(False)
print(isinstance(x, bool))


#numeric data type
#integer
price = 100
best_price = int(100)
print(type(price))
print(isinstance(price, int))

#float type
gpa = 8.25
y = float("1.14")
print(type(gpa))
print(isinstance(gpa, float))
print(isinstance(y, float))
#complex type
comp_value = 1+2j
print(type(comp_value   ))

#Built function for numbers
print(abs(gpa))  #absolute value doesn't print negative numbers
print(abs(gpa*-1))
print(round(gpa))
print(round(gpa, 1))  #round to one decimal place


#there are some modules which provides us pretty good math functions
import math
print(math.pi)  #pi value
print(math.sqrt(64))  #pi value
print(math.ceil(gpa))  #pi value
print(math.floor(gpa))  #pi value

###casting string to number
zipcode = "12345"
zip_value = int(zipcode)
print(type(zip_value))

##Error if you attempt to convert a string that is not a number
# zipcode = int("New car is joaguar")
# print(zipcode)  #this will give error because it is not a number