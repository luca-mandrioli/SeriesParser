'''
Created on 9 Dec 2013
'''
import sys
from com.mandrocker.series.db import MongoDb

if __name__ == '__main__':
    if len(sys.argv) < 5:
        exit(1) 
    
    seriesName = sys.argv[1] #'Supernatural' 
    seasonNumber = sys.argv[2] #1 
    wikiPath = sys.argv[3] #"List_of_Supernatural_episodes"
    seasonAnchor = sys.argv[4] #"Season_1:_2005.E2.80.9306"
    
    db = MongoDb.MongoDb('localhost', 27017)
    db.pushSeries(seriesName, seasonNumber, wikiPath, seasonAnchor)