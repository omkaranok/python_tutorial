##while loopp execute block of code until it is true
import random
value =1
while(value<10):
    value+=1
    if value == 5:
        continue
    print(value)
else:
    print("Value is now equal to "+ str(value))    
    
names = list(["Neil","John","dave","Jimmy"])

for x in names:
    print(x) 
    
for x in "Mississippi":
    print(x)  
    print(type(x))  
    
    
for x in range(0,100,5):
    print(x)
else:
    print("Glad that\'s over!")  
    
names = ["Neil","John","dave","Jimmy"]
action = ["sing","play","drum","guitar"]

for name in names:
    for act in action:
        print(name + " will " + act)      

hehe = random.choice(action)
print(hehe)       
        
    