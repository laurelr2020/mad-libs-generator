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
    sillyName4 = input("One More Silly Name: ")
    facialFeature = input("Facial Feature: ")
    verb = input("Verb: ")
    noun = input("Noun: ")
    actor = input("Actor: ")
    noun2 = input("Noun: ")

    madLibList = [sillyName, unrealisticProfession, country, sillyName2, color, adjective, adverb, sillyName3, sillyName4, facialFeature, verb, noun, actor, noun2]

promptBeginning()
