class MadLibs:
    def __init__(self, prompts, script):
        self.prompts = prompts
        self.script = script


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

superheroScript = "test"

comicSuperhero = MadLibs(superheroPrompts, superheroScript)