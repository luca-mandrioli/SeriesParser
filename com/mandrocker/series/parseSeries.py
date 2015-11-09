'''
Created on 9 Dec 2013
'''

import sys, configparser
from com.mandrocker.series.crawler import Crawler
from com.mandrocker.series.db import MongoDb
from com.mandrocker.series import FileRenamer

if __name__ == '__main__':
    
    if len(sys.argv) < 1:
        exit(1) 
   
    config = configparser.ConfigParser()
    config.read(sys.argv[1])
    
    settings = config['Settings']
    db = MongoDb.MongoDb(settings['database.host'], int(settings['database.port']))
    
    for section in config.sections():
        if section.lower() != 'settings':
            escapedName = config[section]['seriesName'].replace('"', '').replace(' ', '')

            series = db.getSeries(config[section]['seriesName'], config[section]['seasonNumber'])
            print('http://en.wikipedia.org/wiki/', config[section]['seasonNumber'], series['wikiPath'], series['seasonAnchor'])

            crawler = Crawler.Crawler('http://en.wikipedia.org/wiki/', config[section]['seasonNumber'], series['wikiPath'], series['seasonAnchor'])
            
            titlesDict = crawler.pullData()
            db.pushData(titlesDict, escapedName, config[section]['seasonNumber'])

            fileRenamer = FileRenamer.FileRenamer(config[section]['basePath'], config[section]['seriesName'], 
                                                  config[section]['seasonNameString'], config[section]['seasonNumber'])
            fileRenamer.renameSeries(titlesDict)