def promptBeginning():
    answer = input("Would you like to do a Mad Lib? (yes/no) ")

    if answer == "yes":
        generateMadLib()
    elif answer == "no":
        print("okay...byee")
    else:
        print("not a valid input")

def generateMadLib():
    print("\n*******  Welcome  ********")
    print("You will be prompted for different types of words from the English language.")
    print("Enter a word for each prompt and at then end you will have a story.")
    print("\n")

    sillyName = input("Silly Name: ")
    unrealisticProfession = input("Unrealistic Profession: ")
    country = input("Country: ")
    sillyName2 = input("Another Silly Name: ")
    color = input("Color: ")
    adjective = input("Adjective: ")
    adverb = input("Adverb: ")
    sillyName3 = input("Third Silly Name: ")
    sillyName4 = input("Fourth Silly Name: ")
    facialFeature = input("Facial Feature: ")
    city = input("US City: ")
    sillyName5 = input("Fifth Silly Name: ")
    verb = input("Verb ending in -ing: ")
    noun = input("Noun: ")
    actor = input("Actor: ")
    noun2 = input("Noun: ")

    madLibList = [sillyName, unrealisticProfession, country, sillyName2, color, adjective, adverb, sillyName3, sillyName4, facialFeature, city, sillyName5, verb, noun, actor, noun2]
    populateMadLib(madLibList)

def populateMadLib(inputs):
    print("Meet our hero " + inputs[0] + ", a super intelligent " + inputs[1] + ".")
    print("A run-in with the military of " + inputs[2] + " leads him to create his alter-ego, " + inputs[3] + ", a " + " " + inputs[4] + " " + inputs[5] + " giant, capable of great destruction.")
    print("He " + inputs[6] + " battles the military with his girlfriend " + inputs[7] + ".")
    print("Eventually it is discovered that our hero's long-time colleague, " + inputs[8] + ", distinguished by his " + inputs[9] + ", is trying to turn " + inputs[3] + " into a weapon, leading to a climatic (if pointless) battle in downtown " + inputs[10] + "  with an evil version of the same giant alter-ego called " + inputs[11] + ".")
    print("Eventually the enemy is subdued by " + inputs[12] + " him with a " + inputs[13] + ".")
    print("In the final reel, " + inputs[14] + " joins him in a " + inputs[15] + ".")

promptBeginning()
