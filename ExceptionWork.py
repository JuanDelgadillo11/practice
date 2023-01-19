try:
    user_input1 = input("Please enter first number: ")
    user_input2 = input("Please enter first number: ")

    c = int(user_input1) + int(user_input2)
    print(c)
except:
    print(" Your input is incorrect, please enter correct data")
finally:
    print("This code is executed always at the end no matter if result is correct or not")
# Error during execution needs to be captured and handled
