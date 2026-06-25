# import random

# range_limit = input("Type a number: ")

# if range_limit.isdigit():
#     range_limit = int(range_limit)  #typecasting the range_limit input 

#     if range_limit <= 0:
#         print("Please type a number larger than zero.")
#         quit()

# else:
#     print("Please type a number next time.")
#     quit()

# random_number = random.randrange(0, range_limit)        #one argument can be passed.

# guesses = 0

# while True:
#     guesses+=1
#     user_guess = input("Make a guess: ")
#     if user_guess.isdigit():
#         user_guess = int(user_guess)  #typecasting the range_limit input 
#     else:
#         print("Please type a number next time.")
#         continue

#     if user_guess == random_number:
#         print("You got it!")
#         break
#     elif user_guess > random_number:
#         print("You're above the number.")
#     else:
#         print("You're below the number.")

# print(f"You got it in {guesses} guess(es)")
    
# # random.randint(-5, 11)
