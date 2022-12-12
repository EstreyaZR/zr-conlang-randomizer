import random
import logging
import os
import configparser

config = configparser.ConfigParser()

with open('example.ini', 'w') as configfile:

    config['SYNTAX'] = {
        'Word Order' : 'R',
        'Head of Phrase' : 'R'}
    config ['NP'] = {'head' : 'x', 'allowedParts' : ['x', 'y', 'z'], 'Classes': ''}
    config ['VP'] = {'head' : 'x', 'allowedParts' : ['x', 'y', 'z'], 'maxTransivity' : '3'} 
    config ['x'] = {'head' : 'x', 'allowedParts' : ['x', 'y', 'z']} 
    config ['y'] = {'head' : 'x', 'allowedParts' : ['x', 'y', 'z']} 
    config ['z'] = {'head' : 'x', 'allowedParts' : ['x', 'y', 'z']} 

    config.write(configfile)

##SyntaxMaker(WordOrder, PredefinedWordClasses):
#    pass

if os.path.exists('syntax-log.txt'):#clears logging
    os.remove('syntax-log.txt')

logging.basicConfig(filename='syntax-log.txt', level=logging.DEBUG, format='')

class SemanticStructure:

    allowedParts = []
    allowedStructures = {}

    def setAllowedConstituents(self, constituent): # SETS PARTS FOR THE STRUCTURES TO ALLOW
        self.allowedParts.clear()

        self.allowedParts.extend(constituent)

        logging.debug('replaced PoPh with', constituent)

    def listAllowedConstituents(self):
        print('PartsOfPhrase include:', self.allowedParts)

    def addAllowedStructures(self, maxIterations): # RANDOMIZES STRUCTURES
        for i in range(maxIterations):
            random.shuffle(self.allowedParts)

            self.allowedStructures.update({len(self.allowedStructures): self.allowedParts.copy()}) 
            
    def listAllowedConstructions(self):
        print(self.allowedStructures) 

class Phrase(SemanticStructure):

    def __init__(self, name, head):
        self.name = name
        self.head = head    

class Clause(SemanticStructure):
    def __init__(self, name, type, head):
        self.name = name
        self.type = type
        self.head = head ### ONLY PHRASE CLASS

NP = Phrase('NP', 'n')
NP.setAllowedConstituents(['n', 'adj', 'num'])
NP.addAllowedStructures(2)
NP.listAllowedConstructions()
VP = Phrase('VP', 'v')
TemP = Phrase('TemP', 'adPos')