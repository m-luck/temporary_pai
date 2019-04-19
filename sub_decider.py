def isModelLinear(model):
    try:
        enumEquivalent = model.value
    except:
        print('Cannot get value. Make sure a modelBias item is being passed in.')
    else:
        if enumEquivalent > 1:
            return False
        return True

def addCombosIfModelLinear(model):
    try:
        enumEquivalent = model.value
    except:
        print('Cannot get value. Make sure a modelBias item is being passed in.')
    else:
        if isModelLinear(model):
            # multiply columns together for new nonlinear features...
            # ... 
        # Else, model can mathematically account for nonlinearities. In a network, this is choice of ReLU, sigmoid activation, etc.  
            