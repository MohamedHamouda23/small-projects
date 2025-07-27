# Program starter
Guidance = str(input("Assistance with deposit process (Deposit Help Request 1): "))
if Guidance == "1":  # starts with 1.
    print("Hello user, please answer some questions to help you in deposit.\n(symbols and letters not allowed)")
    print("Note, you have three attempts to enter the valid data.\n")
else:  # Any other input shows a message and ends the program.
    print("Sorry, our help is in deposits only.")
    exit()

# Variable for 3 attempts
max_attempts = 2
attempts = 0
print("\nThe deposit amount starts from 100 pounds")  # display aware message of valid variables

# Loop for 3 attempts
while attempts <= max_attempts:
    try:
        deposit_amount = float(input("Enter a valid deposit amount: "))
        if deposit_amount >= 100:  # correct input print continue and exit from loop
            print("Continue")
            break
        else:  # every time the user enters a wrong input, the attempts increases by 1 and display the message
            print("acceptable value from 100")
            attempts += 1
    except ValueError:  # if the user enters a symbol or letter, the attempts increases by 1 and display the message
        print("acceptable value from 100")
        attempts += 1
else:  # when reached 3 attempts display the message and exit from program
    print("\nYou reached the maximum attempts. Please restart the program again.")
    exit()

# Variable for 3 attempts
max_attempts1 = 2
attempts1 = 0
print("\nInterest rate should be between 0 and 26 (%)")  # display aware message of valid variables

# Loop for 3 attempts
while attempts1 <= max_attempts1:
    try:
        interest_rate = float(input("Enter a valid interest rate: "))
        if 0 < interest_rate <= 25:
            print("Continue")  # correct input print continue and exit from loop
            break
        else:  # every time the user enters a wrong input, the attempts increases by 1 and display the message
            print("Value out of range")
            attempts1 += 1
    except ValueError:  # if the user enters a symbol or letter, the attempts increases by 1 and display the message
        print("Value out of range")
        attempts1 += 1
else:  # when reached 3 attempts display the message and exit from program
    print("\nYou reached the maximum attempts. Please restart the program again.")
    exit()

# Variable for 3 attempts
max_attempts2 = 2
attempts2 = 0
print("\nThe interest period is from 0 to 10 (years): ")  # display aware message of valid variables

# Loop for 3 attempts
while attempts2 <= max_attempts2:
    try:
        interest_period = int(input("Enter a valid interest period: "))
        if 0 < interest_period <= 10:
            print("Continue")  # correct input print continue and exit from loop
            break
        else:  # every time the user enters a wrong input, the attempts increases by 1 and display the message
            print("Value out of range")
            attempts2 += 1
    except ValueError:  # if the user enters a symbol or letter, the attempts increases by 1 and display the message
      print("Value out of range")
      attempts2 += 1
else:  # when reached 3 attempts display the message and exit from program
    print("\nYou reached the maximum attempts. Please restart the program again.")
    exit()

# Display strings with inputs from the user
print("\nThe plan:\nDeposit amount =", deposit_amount)
print("Interest rate =", interest_rate, "%\nInterest period =", interest_period, "years\n")

# Loop through to calculate yearly interest
year = 0
for year in range(interest_period):
    results = deposit_amount * (1 + interest_rate / 100)
    year += 1
    print("Year", year, "=", round(results, 2))
    deposit_amount = results

# Display prompts and gather user input, rounding to two decimal places
print("\nThe balance at the end of the period =", round(deposit_amount, 2))
print("\nWith an interest rate of", interest_rate, "% and an interest period of", interest_period, "years")
