from os import system
import madLibs
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

    comicSuperhero = madLibs.createSuperHeroMadLib()
    comicSuperhero.printAndSpeak(comicSuperhero.script)

promptBeginning()