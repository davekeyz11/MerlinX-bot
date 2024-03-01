import sys
import pyttsx3
engine = pyttsx3.init()
greetings = ["Hi", "Hello", "Hey", "Good morning", "Good afternoon", "Good evening"]
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
     quit()
engine.say("What is your name?: ")
engine.runAndWait()
userName = input("What is your name?: ")

engine.say("Welcome " + userName + " I am here to ask you a few questions about yourself and test your Intellectual Quotient.")
engine.runAndWait()
print ("Welcome " + userName + " I am here to ask you a few questions about yourself and and test your Intellectual Quotient.")
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
     quit()
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
      engine.say("I also like " + userInput3)
engine.runAndWait()
print("I also like " + userInput3)


engine.say("Thank you for answering the first section of questions, now it is time to move to the final one")
engine.runAndWait()
print("Thank you for answering the first section of questions, now it is time to move to the final one")

engine.say("Who is the father of computers?: ")
engine.runAndWait()
userInputnextsec= input("Who is the father of computers?: ")

if userInputnextsec == "Charles Babbage":
     engine.say("That is correct")
     engine.runAndWait()
     print("That is correct")
else:
     engine.say("That is incorrect, program ended")
     engine.runAndWait()
     print("That is incorrect, program ended")
     quit()
     



engine.say("Who is the musician that burnt his hair in a Pepsi Cola commercial?: ")
engine.runAndWait()
userInputnextsec2 = input("Who is the musician that burnt his hair in a Pepsi Cola commercial?: ")

if userInputnextsec2 == "Michael Jackson":
     engine.say("That is correct")
     engine.runAndWait()
     print("That is correct")
else:
     engine.say("That is incorrect, program ended")
     engine.runAndWait()
     print("That is incorrect, program ended")
     quit()

engine.say("	What animal’s foot is said to be a good luck charm?")
engine.runAndWait()
user_in = input("What animal's foot is said to be a good luck charm?: ")

if user_in == "Rabbit":
     engine.say("That is correct")
     engine.runAndWait()
     print("That is correct")
else:
     engine.say("That is incorrect, program ended")
     engine.runAndWait()
     print("That is incorrect, program ended")
     quit()

engine.say("Thank you for allowing me to test your Intellectual Quotient and for helping me to know more about you, Enjoy your day and star the MerlinX-bot GitHub repo at github.com/davekeyz11")
engine.runAndWait()
print("Thank you for allowing me to test your Intellectual Quotient and for helping me to know more about you, Enjoy your day and star the MerlinX-bot GitHub repo at github.com/davekeyz11")