# it is difficult for beginner to uinderstand these concepts
#closure is a function having access to the scope of its parent function aftre the parent function has returnrd some value

def parent_function(person,coins):      ##passing parameter as input to function does th same as it has been defined inside the function
    # coins = 3
    
    def play_games():
        nonlocal coins
        coins -= 1
        
        if coins > 1:
            print("\n" + person + " is playing games with " + str(coins) + " coins left.")
        elif coins == 1:
            print("\n" + person + " is playing games with " + str(coins) + " coins left.")
        else:
            print("\n" + person + " has no coins left to play games.")
    
    
    return play_games

tommy = parent_function("Tommy",3)
jeeny = parent_function("Jeeny",3)    
tommy()  
tommy() 
tommy()    
jeeny()     
            