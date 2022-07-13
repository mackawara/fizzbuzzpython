print("Pleae enter your age:")
age=int(input("age in years : "))
fav_car=input("what is your fav car: ")
cars=["mazda","landrover","Jeep", "Ford", "Toyota"]
people={"mac":{"name":"Macdonald Kawara","age":35}}

if age>people["mac"]["age"]:
    print("You are getting old my guy")
    for car in cars:
        if fav_car==car:
            print("congratulations we have a car for you")
        else:
            print("no car for you my guy")

