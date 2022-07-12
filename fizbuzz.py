
numbers=range(1,100)
print(numbers)
for number in numbers:
     if number % 5==0 and number%3==0:
        print("FIZZ BUZZ ")
     elif number % 5 ==0:
        print("BUZZ")
     elif number%3==0:
        print("FIZZ")
     else :
        print(number)
