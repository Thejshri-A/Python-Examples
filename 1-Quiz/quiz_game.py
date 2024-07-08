print("Welcome to my Computer Quiz")

playing = input("Do you want to play? ")

print("\n Your response is ", playing)

if playing.lower() != "yes":
    quit()

print("Okay Lets Play :)")
score = 0

answer1 = input("What does CPU stand for ? ")

if answer1.lower() == "central processing unit":
    print("Correct! ;)")
    score += 1
else:
    print("Incorrect!")

answer1 = input("What does GPU stand for ? ")

if answer1.lower() == "graphics processing unit":
    print("Correct! ;)")
    score += 1
else:
    print("Incorrect!")

answer1 = input("What does RAM stand for ? ")

if answer1.lower() == "random access memory":
    print("Correct! ;)")
    score += 1
else:
    print("Incorrect!")

answer1 = input("What does PSU stand for ? ")

if answer1.lower() == "power supply unit":
    print("Correct! ;)")
    score += 1
else:
    print("Incorrect!")

print("You got " + str(score) + " questions correct")
print("You got " + str((score/4)*100) + "y%")
