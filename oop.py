
class TestObj:
    def __init__(self, name, location):
        self.name = name
        self.location = location

    def attributes(self):
        print("I am  "+self.name+" I am from " + self.location)
    height = 25


class OBj(TestObj):
    def __init__(self, name, location, age):
        self.age = age
        super().__init__(name, location)

    def age_print(self):
        print(" My height is " + str(self.height))


mac = TestObj("Mac", "Zimbabwe")
marion = OBj("Marion ", " Zimbabwe", 21)
mac.attributes()
marion.height
marion.age_print()
