print(" Tests fr ML")
class TestObj:
    def __init__(self, name,location):
        self.name=name
        self.location=location

        self.attributes=print("I am  "+self.name+" I am from "+ location) 
class OBj(TestObj):
    def __init__(self,name,location,age,attributes):
        self.age=age
        super().__init__(attributes)
                     
        

mac =TestObj("Mac","Zimbabwe")  
marion=OBj("Marion "," Zimbabwe",21)
mac.attributes   
marion.attributes  
