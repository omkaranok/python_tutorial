def hello_world():
    print("Hello world!")
    
hello_world()

def sum(num1=0,num2 = 3):   ##here num2  is a default parameter, if we don't pass the second argument it will take 3 as default
    if type(num1) is not int or type(num2) is not int:
        return
    return num1+num2
    
total = sum(5,3)    
total1 = sum("Hii","Hello")
total2 = sum()
print(total)
print(total1)     ###here the value is none because the function does not return anything if the type is not int
print(total2)     ###here the value is 3 because the default value of num2 is 3

def multiple_items(*args):    ###args is a tuple of all the arguments passed
    print(args)       ###here it will print a tuple of all the argument passed
    print(type(args))
    
multiple_items(1,2,3,4,5,"Car","Jaguar")    


def mult_named_items(**kwargs):    ###keyword arguments
    print(kwargs)
    print(type(kwargs))
    
mult_named_items(first = "Jaguar",last = "Ford")    ###it will return a dictionary of the keywords key value pairs data
    