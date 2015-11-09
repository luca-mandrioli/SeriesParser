'''
Created on 9 Dec 2013
'''

from pymongo import MongoClient

class MongoDb(object):
    '''
    classdocs
    '''
    def __init__(self, host, port):
        self.client = MongoClient(host, port)
        
    def pushData(self, titlesDict, seriesName, seasonNumber):
        db = self.client[seriesName]
        self.saveToDatabase(db['Season' + str(seasonNumber)], titlesDict)

    def saveToDatabase(self, collection, titlesDict):
        for episode in titlesDict.keys():
            existingDocument = collection.find_one(episode)
            if not existingDocument:
                data = {'_id': episode,
                        'title': titlesDict.get(episode)}
    
                collection.insert(data)  
            
    def pushSeries(self, seriesName, seasonNumber, wikiPath, seasonAnchor):
        db = self.client['series-list']
        collection = db[seriesName]
        
        data = {'_id': seasonNumber, 
                'wikiPath': wikiPath,
                'seasonAnchor': seasonAnchor
                }
        
        collection.insert(data)           
    
    def getSeries(self, seriesName, seasonNumber): 
        db = self.client['series-list']
        return db[seriesName].find_one({'_id': str(seasonNumber)})
    