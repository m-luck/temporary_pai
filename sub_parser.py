# All code below specifically written for Prospero.ai starting 7:30am Wednesday.
# I'm coming from an angle of graduate math, and theoretical mastery, but with a product-minded personality. 
# Code is meant to be readable by team, not obscure (maybe at the cost of a couple extra lines).

# This file relates to input and formatting of output.

from enum import Enum

# This answers: What type of model do we have? This is the first step of understanding. Different models, different data preferences.

class ModelBias(Enum):
    LINEAR=1 # Can also be a GLM.
    TREE=2 # Decision tree, default assumption is ensemble of stochastic trees resulting in a forest.
    NEUR=3 # Network with weighted neurons and 1 to many hidden layers. 
    BN=4 # Bayesian network. 
    GMM=5 # Gaussian mixture model.
    GP=6 # Gaussian process.

# This answers: What type of problem is this? 
class Modality(Enum):
    REG=1 # Regression
    BIN=2 # Binary classification
    MULTI=3 # Multiclass 

def model_map(mod:str):
    '''
    Returns concrete enum values from human-language. Good practice. 
    '''
    str_to_enum = {
        'linear': ModelBias.LINEAR,
        'forest': ModelBias.TREE,
        'net': ModelBias.NEUR,
        'bayes': ModelBias.BN,
        'mixture': ModelBias.GMM,
        'gp': ModelBias.GP
    }
    try:
        res = str_to_enum[mod]
        return res
    except: 
        print("Try model options such as: linear, forest, net, bayes, mixture, gp.")
    else: 
        return res

def type_map(type:str):
    '''
    Returns regression or binary / multi classification enum values.
    '''
    str_to_enum = {
        'regression': Modality.REG,
        'binary': Modality.BIN,
        'multi': Modality.MULTI
    }
    try:
        res = str_to_enum[type]
        return res
    except: 
        print("Try problem type options such as: regression, binary, multi.")
    else: 
        return res

def read_args(args):
    '''
    Reads input.
    '''
    try: 
        modelStr = args[1]
        typeStr = args[2]
    except:
        print("Trouble reading in the arguments. Try process.py <Model> <RegOrClass> [--verbose].")
    else: 
        specificTicks = None
        debug_mode = False
        if len(args) > 3:
            if args[3] == "--verbose":
                concise = debug_mode = True
        if len(args) > 4:
            specificTicks = []
            path = sys.argv[4]
            with open(path, 'r') as f:
                for line in f:
                    specificTicks.append(str(line))

        return modelStr, typeStr, debug_mode, specificTicks
    