class vehicle:
    def __init__(self,make,model):
        self.make = make
        self.model = model
        
    def  moves (self):
        print("Moves along....")
        
    def get_make_model(self):
        print(f"I' m a {self.make} model name {self.model}")    
        
        
my_car = vehicle('Tesla','Model 3')
print(my_car.model)
print(my_car.make)
my_car.moves()  
my_car.get_make_model()   

your_car = vehicle("Cadillac","Escalade")
print(your_car.model)   
print(your_car.make)


class Airplane(vehicle):
    def __init__(self,make,model,faa_id):
        super().__init__(make,model)  ###This tell that we are going to inherits from the parent class vehicle
        self.faa_id = faa_id
        
    def moves(self):
        print("Files Along .....")
        
class Helicopter(vehicle):
    def moves(self):
        print("Hovers along....")
        
class GolfCart(vehicle):
    pass  ###pass it is going to inherit the things as ait is from the parent class vehicle      

cessna = Airplane("Cessna","172 Skyhawk",123)
mack = Helicopter("Mack","Helicopter")
golf_cart = GolfCart("Yamaha","Drive2")

cessna.get_make_model()
cessna.moves()
mack.get_make_model()   
mack.moves()
golf_cart.get_make_model()
golf_cart.moves()  #it will call the moves method from the parent class vehicle

print("\n\n")

for v in (my_car,your_car,cessna,mack,golf_cart):    ###for loop can be applied for tuple also 
    v.get_make_model()
    v.moves()  #it will call the moves method from the child class if it is defined otherwise it will call the parent class method
    # print(type(v))  #it will tell the type of object we are dealing with
    # print(isinstance(v,vehicle))  #it will tell whether this object is instance of vehicle or not
    # print() 
                