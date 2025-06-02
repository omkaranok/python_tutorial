name = "Dave"
count = 1


def greeting(name):
    colors = "Blue"
    global count       ##it tels that this value exists in global scope by adding the global keywords
    count+= 1          ###we can't access global count here in side local it get defined in a new varible to access it we need to use global keywords
    print(colors)
    print(name)
    print(count)
    
    def greeting(name):
        # nonlocal colors    ###nonlocal keywordsis used to add the value of colors in the colrs value of parent scope 
        colors = "Red"
        print(colors)
        print(name)
    
    greeting("Bob")
    
greeting("Alice")    
    
