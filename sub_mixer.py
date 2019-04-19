import pandas as pd
from typing import List

def oneHotifyColumns(csvpath:str, newpath:str, colNames:List):
    '''
    Turns columns of choice into categorical binaries per category.
    '''
    chunksize=20000
    i=0
    for chunk in pd.read_csv(csvpath, chunksize=chunksize):
        print("Chunk",i)
        i+=1
        for colName in colNames:
            one_hot = pd.get_dummies(chunk[colName], prefix=colName)
            chunk = chunk.drop(colName,axis = 1)
            chunk = pd.concat([chunk, one_hot], axis=1)
        chunk.to_csv(newpath, mode='a', index=False)

def addDatesToCyclic(csvpath:str, newpath:str, dateColName:str):
    '''
    Extracts cyclic data from dates, including day of week, week of year, and month of year. 
    Additional insight is to look into days of earning reports, etc. 
    '''
    chunksize = 20000
    i=0
    for chunk in pd.read_csv(csvpath, nrows=3000000,  parse_dates= [dateColName], chunksize=chunksize):
        print("Chunk",i)
        i+=1
        chunk['month'] = chunk[dateColName].dt.month
        chunk['week'] = chunk[dateColName].dt.week
        chunk['day'] = chunk[dateColName].dt.day
        chunk.to_csv(newpath, mode='a', index=False)

def adjustForInflation(year:int, colNames:List):
    '''
    In years-spanning time series data, my intuition says to account for inflation and other rates, or to at least include the rate as a feature.
    Same intution goes for federal rates, etc.
    '''
    pass # Need inflation data, just a part of the thought process. 

def multiplyColumns(c1:str,c2:str,new:str):
    '''
    Multiply features together to indicate effects that score exclusively well together.
    '''
    chunksize=20000
    i=0
    for chunk in pd.read_csv(csvpath, chunksize=chunksize):
        print("Chunk",i)
        i+=1
        chunk[new] = chunk.apply(lambda row: (row[c1]*row[c2], axis=1))

def logColumns(colNames: List):
    '''
    Log scale a feature to curb growing effects (sublinear decision).
    '''
    chunksize=20000
    for chunk in pd.read_csv(csvpath, chunksize=chunksize):
        for col in colNames:
            chunk['norm'] = (1+chunk[col])/2 # (-1,1] -> (0,1]
            chunk['lognorm'] = np.log(chunk['norm'])
if __name__ == "__main__":
    # addDatesToCyclic('data/4.csv', 'new_daily_example.csv', 'date')
    # oneHotifyColumns('new_daily_example.csv', 'dummy_daily.csv', ['month','week','day'])
    addDatesToCyclic('onlyAAPL.csv', 'AAPLcyclic.csv', 'date')
    oneHotifyColumns('AAPLcyclic.csv', 'AAPLcyclic_one.csv', ['month','week','day'])