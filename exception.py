x = 2

class JustNotCoolError(Exception):
    pass
try:
    raise JustNotCoolError("This is not cool man!")  ###we can raise our own error
    # print(x / 0)
    # if not type(x) is str:
    #     raise TypeError("only strings are allowed")
except NameError:   ###if we define the special error then it will only catch that error not the other errors
    print("NameError is not defined.")  
except ZeroDivisionError:  ###if we define the special error then it will only catch that error not the other errors
    print("Please do not divide by zero.")   
except Exception as error:    
    print("An error occurred:", error)
else:       ###else block will run if tere is no error 
    print("No error occurred.")   
finally:
    print("This will always run.")  ###finally block will run always no matter what happens in the try block      
          