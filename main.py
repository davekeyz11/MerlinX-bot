# Import Libaries and Initialize
import sys
import pyttsx3
engine = pyttsx3.init()
greetings = ["hi", "hello", "hey", "good morning", "good afternoon", "good evening"]
mergedGreetings = ", ".join(greetings)

engine.say("Enter your message.")
engine.runAndWait()
user_input = input("Enter your message: ")

if user_input in greetings:
    engine.say("Greeting detected")
    engine.runAndWait()
    print("Greeting detected")
else:
     engine.say("Invalid Input")
     engine.runAndWait()
     print("Invalid Input")
     sys.exit()
     engine.say("What is your name?")
     engine.runAndWait()
userName = input("What is your name?: ")
engine.say("Welcome " + userName + " I am here to ask you a few questions about yourself")
engine.runAndWait()
print ("Welcome " + userName + " I am here to ask you a few questions about yourself")
engine.say("Do you like sports?")
engine.runAndWait()
user_input2 = input("Do you like sports?: ")
if user_input2 == "Yes":
    engine.say("That's nice")
    engine.runAndWait()
    print("That's nice")

elif user_input2 == "No":
    engine.say("That's okay")
    engine.runAndWait()
    print("That's okay")

else:
     engine.say("Invalid input")
     engine.runAndWait()
     print("Invalid input")
     sys.exit()
hobbies = ["Playing Piano", "Playing Guitar", "Drawing", "Coding", "Content creating", "Creating 3D Models", "Drawing and animating items"]
mergedHobbies = ", ".join(hobbies)
engine.say("What is your hobby?")
engine.runAndWait()
userInput3 = input("What is your hobby?: ")
if userInput3 in hobbies:
        engine.say("I also like " + userInput3)
        engine.runAndWait()
        print("I also like " + userInput3)
else:
     engine.say("That's okay")
     engine.runAndWait()
     print("That's okay")