##Computer Abbreviations | Quiz Game

score = 0
print("Welcome to my Computer Abbreviations Quiz game!")

play = input("Do you want to start the quiz game? [y/n]: ")
if play.lower() != "y":    
    print("We are sorry to see you leave. Please come back next time.")
    quit()
else: 
    print("Ready! Go!")

    qstn = input("What does CPU stand for? ")
    if qstn.lower() == "central processing unit":
        print("Kuddos! You got it correct!")
        score += 1
    else:
        print("You got it incorrect!")
    
    qstn = input("What does RAM stand for? ")
    if qstn.lower() == "random access memory":
        print("Kuddos! You got it correct!")
        score += 1
    else:
        print("You got it incorrect!")
    
    qstn = input("What does ROM stand for? ")
    if qstn.lower() == "read only memory":
        print("Kuddos! You got it correct!")
        score += 1
    else:
        print("You got it incorrect!")
    
    qstn = input("What does PSU stand for? ")
    if qstn.lower() == "power supply":
        print("Kuddos! You got it correct!")
        score += 1
    else:
        print("You got it incorrect!")
    
    qstn = input("What does SSD stand for? ")
    if qstn.lower() == "solid state drive":
        print("Kuddos! You got it correct!")
        score += 1
    else:
        print("You got it incorrect!")
    
    qstn = input("What does HDD stand for? ")
    if qstn.lower() == "hard disk drive":
        print("Kuddos! You got it correct!")
        score += 1
    else:
        print("You got it incorrect!")
    
    qstn = input("What does USB stand for? ")
    if qstn.lower() == "universal serial bus":
        print("Kuddos! You got it correct!")
        score += 1
    else:
        print("You got it incorrect!")
    
    if (score >= 4):
        print("Congratulations! You passed with a score of "+str(score)+" points.")
    else:
        print("Failed! You got a score of "+str(score)+" points.")
        
quit()