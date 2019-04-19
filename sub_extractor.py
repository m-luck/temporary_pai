import csv
import pandas as pd
from typing import List

def generate_all_known_tickers():
    '''
    We have a tickers list but I just wanted to see if the tickers in there
    were different than all the tickers we've seen in the single day stats since 2011, for more learning.
    Answer: Yes, around 1400% more when looking at all single day stats.
    File of output: mj_tickers.txt 
    '''
    # Daily stats since 2011
    tickersFound, namesFound, chunksize, it= 0, {}, 10000, -1
    for chunk in pd.read_csv('data/4.csv', chunksize=chunksize):
        it+=1
        print("Chunk",it)
        for index, row in chunk.iterrows():
            tickerName = row["ticker"]
            if tickerName not in namesFound:
                namesFound[tickerName] = str(row["date"])
                tickersFound += 1
    with open('mj_tickers.txt', 'w+') as f:
        f.write("Tickers count: {count}\n".format(count=tickersFound) ) 
        f.write(str(namesFound))

def filterDimensions(csvpath:str, newcsv:str, features:List):
    '''
    Take a set of features you want to keep and isolate those.
    '''
    chunksize = 20000
    i=0
    for chunk in pd.read_csv(csvpath, chunksize=chunksize, usecols=features):
        print("Chunk",i)
        i+=1
        chunk.to_csv(newcsv, mode='a', index=False)

def filterMatch(csvpath:str, newcsv:str, feature:str, match:str):
    '''
    Only include results which match a certain value.
    '''
    chunksize = 20000
    i=0
    writeHeader = True
    for chunk in pd.read_csv(csvpath, chunksize=chunksize):
        print("Chunk",i)
        chunk = chunk.loc[chunk[feature] == match]
        i+=1
        chunk.to_csv(newcsv, mode='a', index=False, header=writeHeader)
        writeHeader = False

if __name__ == "__main__":
    # Examples of Options dimension reduction
    # Depends on problem, but the principle is to keep fields with low covariance.
    # Correlated fields don't need to be redundantly included.
    # Sometimes even low correlation can imply dependence, so we would graph them first. 
    # keep = ['Date',
    # '\tPcrVolAll',
    # '\tPcrVol10',
    # '\tPcrVol20',
    # '\tPcrVol30',
    # '\tPcrVol60',
    # '\tPcrVol90',
    # '\tPcrVol120',
    # '\tPcrVol150',
    # '\tPcrVol180',
    # '\tPcrVol270',
    # '\tPcrVol360',
    # '\tPcrVol720',
    # '\tPcrVol1080',
    # '\tCallBreakeven10',
    # '\tCallBreakeven20',
    # '\tCallBreakeven30',
    # '\tCallBreakeven60',
    # '\tCallBreakeven90',
    # '\tCallBreakeven120',
    # '\tCallBreakeven150',
    # '\tCallBreakeven180',
    # '\tCallBreakeven270',
    # '\tCallBreakeven360',
    # '\tCallBreakeven720',
    # '\tCallBreakeven1080']
    # filterDimensions('data/1.csv','new_options',keep)
    filterMatch('data/4.csv','onlyAAPL.csv','ticker','AAPL')