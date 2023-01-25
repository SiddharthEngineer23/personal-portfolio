import pandas as pd

"""
Class for taking input and output for xmas list
"""
class Xlist(object):

    def __init__(self):
        
        self.data = pd.read_csv("data/xmas.csv")

    def save(self):

        self.data.to_csv("data/xmas.csv")
    
    