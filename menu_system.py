print("Hello!, Welcome to your menu system.")

name = input("Enter your name? ")

print(f"Hello! {name}")

menu = ["1. Say Hello", "2. Tell a joke", "3. Exit"]

for i in menu:
    print(i)

choice = int(input("Enter your choice: "))

if choice == 1:
    print("Hello")
elif choice == 2:
    print("A fool will laugh when nothing is funny.")
elif choice == 3:
    print("Thank you.")
else:
    print("Invalid input")
