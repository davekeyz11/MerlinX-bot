import sys
greetings = ["hi", "hello", "hey", "good morning", "good afternoon", "good evening"]
mergedGreetings = ", ".join(greetings)

user_input = input("Enter your message: ")

if user_input in greetings:
    print("Greeting detected")
else:
     print("Invalid Input")
     sys.exit()
userName = input("What is your name?: ")
print ("Welcome " + userName + " I am here to ask you a few questions about yourself")
user_input2 = input("Do you like sports?: ")
if user_input2 == "Yes":
    print("That's nice")

elif user_input2 == "No":
    print("That's okay")

else:
     print("Invalid input")
     sys.exit()
hobbies = ["Playing Piano", "Playing Guitar", "Drawing", "Coding", "Content creating", "Creating 3D Models", "Drawing and animating items"]
mergedHobbies = ", ".join(hobbies)
userInput3 = "What is your hobby?: "
if userInput3 in hobbies:
        print("I also like " + hobbies)
else:
     print("That's okay")