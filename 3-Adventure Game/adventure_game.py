name = input("Type your name: ")
print("Welcome", name, "to this adventure!")

answer = input(
    "You are on dirt road, it has come to an end and you can go left or right.Whihc way would you linke to go?")

if answer == "left":
    answer = input("You have come to a river, you can walk around or swim")

    if answer == "swim":
        print("You swam across! You saw alligator!")
    elif answer == "walk":
        print("You walked many miles! You saw a tiger")
    else:
        print("Not a valid option. Game Over")

elif answer == "right":
    answer = input("You came to waterfalls. Do you want to dive or cross")

    if answer == "dive":
        print("You saw a Tuna")

    elif answer == "cross":
        answer = input("You saw a stranger. Do you talk to them (yes/no)")

        if answer == 'yes':
            print("You talked to stranger, and they're friendly")
        else:
            print("You walk and see a pelican")

    else:
        print("Not a valid option. Game Over")
else:
    print("Not a valid option. Game Over")

print("Thank you for trying", name)
