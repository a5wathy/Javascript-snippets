import gc
print(gc.get_threshold())

class Car:
    "Name of the class is Car"

    #class variables
    totalNumber = 0

    def __init__(self,make,model,year):#constructor/Instantiation method
        Car.totalNumber+=1
        self.make = make # to access class variable, use classname.variablename
        self.model = model
        self.year = year
        print("Instance object of the class is created")
        #print("Total number of car is ",Car.totalNumber)

    #Garbage collector
    def __del__(self):
        Car.totalNumber-=1

        
    def displayParameters(self):
        print("Make :", self.make)
        print("Model :", self.model)
        print("Year :", self.year)
        

#object_name = class_name(Parameters)
car1 = Car("A", "B", 2014)
#car1.displayParameters()
#print(car1.make)

car2 = Car("C", "D", 2000)
#car2.displayParameters()
#print(car2.year)
car3 = Car("E", "F", 2011)      
print("Total number of car is ",Car.totalNumber)
del car3
print("Total number of car is ",Car.totalNumber)
print(car3.make)#error:Car3 is not defined
