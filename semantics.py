import random as random
import logging 
import os

if os.path.exists('semantics-log.txt'):#clears logging
    os.remove('output.txt')

logging.basicConfig(filename='semantics-log.txt', level=logging.DEBUG, format='')

#TESTINPUT[[--

uwu = ['ana', 'lulu', 'tiri', 'pira'] # List of Roots
seed = 35 # User Seed


#--]]

random.seed(seed)

def SemanticRandomizer(PreList, TypeOfRoot, NoMutations):
    PreList.sort()
    for i in PreList:
        random.randint(1, NoMutations)
        print(i)

SemanticRandomizer(uwu, verb, 3)