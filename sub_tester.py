# This file has unit tests.
import sys
from sub_parser import *

def test_model_map(args):
    res = model_map(args)
    # print(res)
    return res
    
if __name__ == "__main__":
    print("Welcome to the test suite for the Prospero Sharadar extractor.")
    # Test model_map.
    assert test_model_map('linear') == ModelBias.LINEAR
    assert test_model_map('gp') == ModelBias.GP
    # Test command line input.
    modelStr, typeStr, debug, ticks = read_args(sys.argv)
    model = model_map(modelStr)
    type = type_map(typeStr)
    print(model, type, "Debug:",debug)