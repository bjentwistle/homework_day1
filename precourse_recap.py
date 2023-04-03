# Setting up some string variables and concatenating them
word_1 = "dinosaur"
word_2 = "Ladybird"
print(word_1.upper() + " " + word_2)
print(word_1)
# changing case of strings
word_1 = word_1.upper()
print(word_1)

# Making a function to ask how your first day on the course.
def day_one():
    mood = input("How was your first day in one word?: ")
    if mood == "good":
        print("Glad you had a ", mood , " first day :0)!")
    elif mood == "bad":
        print("Sorry to hear you've had a ", mood, " first day :(")
    else:
        print("Interesting first day then!")

day_one()    
        
