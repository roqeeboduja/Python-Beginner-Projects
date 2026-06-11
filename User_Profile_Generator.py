name = input("Enter your name: ")
age = int(input(("Enter your age: ")))
height = float(input("Enter your height: "))
fav = input("Enter your favorite programming language: ")


print("------------USER------------")
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Height: {height}")
print(f"Age in Months: {age * 12}")
print(f"Age in Days: {age * 365}")
print(f"Favorite language: {fav}")
print(f"Age datatype: {type(age)}")
