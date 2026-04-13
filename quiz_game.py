print("Welcome to the Quiz Game!")

playing = input("Do you want to play? (yes/no): ")
if playing != "yes":
    quit()

print("Let's play!")
score = 0 

answer = input("What does CPU stand for?").lower()
if answer == "central processing unit":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What does GPU stand for?")
if answer == "graphics processing unit":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What does RAM stand for?")
if answer == "random access memory":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What does PSU stand for?")
if answer == "power supply":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

print(f"Score: {score}")