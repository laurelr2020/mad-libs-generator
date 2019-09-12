from os import system
class MadLibs:
    def __init__(self, prompts, script):
        self.prompts = prompts
        self.script = script

    def printAndSpeak(self, script):
        for line in script:
            print(script[line].values)
            script("say " + script[line].values)

def createSuperHeroMadLib():
    superheroPrompts = {}
    superheroPrompts['sillyName'] = input("Name: ")
    superheroPrompts['unrealisticProfession'] = input("Unrealistic Profession: ")
    superheroPrompts['country'] = input("Country: ")
    superheroPrompts['sillyName2'] = input("Name: ")
    superheroPrompts['color'] = input("Color: ")
    superheroPrompts['adjective'] = input("Adjective: ")
    superheroPrompts['adverb'] = input("Adverb: ")
    superheroPrompts['sillyName3'] = input("Name: ")
    superheroPrompts['sillyName4'] = input("Name: ")
    superheroPrompts['facialFeature'] = input("Facial Feature: ")
    superheroPrompts['city'] = input("US City: ")
    superheroPrompts['sillyName5'] = input("Name: ")
    superheroPrompts['verb'] = input("Verb ending in -ing: ")
    superheroPrompts['noun'] = input("Noun: ")
    superheroPrompts['actor'] = input("Actor: ")
    superheroPrompts['noun2'] = input("Noun: ")

    superheroScript = {}
    superheroScript[0] = ("Meet our hero {}, a super intelligent {}.".format(superheroPrompts['sillyName'], superheroPrompts['unrealisticProfession']))
    superheroScript[1] = ("A run-in with the military of {} leads him to create his alter-ego, {}, a {}, {} giant, capable of great destruction."
        .format(superheroPrompts['country'], superheroPrompts['sillyName2'], superheroPrompts['color'], superheroPrompts['color']))
    superheroScript[2] =("He {} battles the military with his girlfriend {}.".format(superheroPrompts['adjective'], superheroPrompts['adverb']))
    superheroScript[3] =("Eventually it is discovered that long-time colleague of our hero, {}, distinguished by his {}, is trying to turn {} into a weapon, leading to a climatic, if pointless, battle in downtown {} with an evil version of the same giant alter-ego called {}."
        .format(superheroPrompts['sillyName3'], superheroPrompts['sillyName4'], superheroPrompts['facialFeature'], superheroPrompts['city'], superheroPrompts['sillyName5']))
    superheroScript[4] =("Eventually the enemy is subdued by {} him with a {}.".format(superheroPrompts['verb'], superheroPrompts['noun']))
    superheroScript[5] =("In the final reel, {} joins him in a {}.".format(superheroPrompts['actor'], superheroPrompts['noun2']))

    return MadLibs(superheroPrompts, superheroScript)
