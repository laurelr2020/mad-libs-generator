from os import system
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
    madLib0 = "Meet our hero {}, a super intelligent {}.".format(inputs[0], inputs[1])
    printAndSpeak(madLib0)

    madLib1 = "A run-in with the military of {} leads him to create his alter-ego, {}, a {}, {} giant, capable of great destruction.".format(inputs[2], inputs[3], inputs[4], inputs[5])
    printAndSpeak(madLib1)

    madLib2 = "He {} battles the military with his girlfriend {}.".format(inputs[6], inputs[7])
    printAndSpeak(madLib2)

    madLib3 = "Eventually it is discovered that long-time colleague of our hero, {}, distinguished by his {}, is trying to turn {} into a weapon, leading to a climatic, if pointless, battle in downtown {} with an evil version of the same giant alter-ego called {}.".format(inputs[8], inputs[9], inputs[3], inputs[10], inputs[11])
    printAndSpeak(madLib3)

    madLib4 = "Eventually the enemy is subdued by {} him with a {}.".format(inputs[12], inputs[13])
    printAndSpeak(madLib4)

    madLib5 = "In the final reel, {} joins him in a {}.".format(inputs[14], inputs[15])
    printAndSpeak(madLib5)


def printAndSpeak(sentence):
    print(sentence)
    system("say " + sentence)

promptBeginning()
