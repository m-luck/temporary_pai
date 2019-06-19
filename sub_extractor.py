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

# from SEP
# sicsector
# sicindustry
# sector
# industry
# famaindustry
# scalemarket
# Hybrid: sector, scalemarket
# sep
# ^^
# for each company value - Mean (of all columns) and value - Median .... 

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
        filterDimensions('SHARADAR_TICKERS_6cc728d11002ab9cb99aa8654a6b9f4e.csv','tickers_w_sicind-sicsect-ind-sect.csv',["ticker","sicsector", "sicindustry", "sector", "industry"])
        s_sec = {}
        s_ind = {}
        sec = {}
        ind = {}
        chunksize = 20000
        i=0
        for chunk in pd.read_csv(csvpath, chunksize=chunksize, usecols=features):
                print("Chunk",i)
                i+=1
                chunk.to_csv(newcsv, mode='a', index=False)