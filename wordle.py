import re
print("Pleae enter your age:")
# age=int(input("age in years : "))
# fav_car=input("what is your fav car: ")
cars=["mazda","landrover","Jeep", "Ford", "Toyota"]
people={"mac":{"name":"Macdonald Kawara","age":35}}
""" 
if age>people["mac"]["age"]:
    print("You are getting old my guy")
    for car in cars:
        matches=re.findall(car,fav_car)
        if len(matches)>0:
            print("congratulations we have a car for you")
        else:
            print(matches)

print(people) """
people.update({"mac2":{"name":"Mac2"}})
print(people)

data_range=range(len(cars))
for data in data_range:
    print(cars[data])



