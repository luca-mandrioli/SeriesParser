'''
Created on 9 Dec 2013

@author: Luca.Mandrioli
'''

import urllib.request
from bs4 import BeautifulSoup
import re

class Crawler(object):
    def __init__(self, baseUrl, seasonNumber, wikiPath, seasonAnchor):
        self.baseUrl = baseUrl
        self.seasonNumber = str(seasonNumber)
        self.wikiPath = wikiPath
        self.seasonAnchor = seasonAnchor
    

    def pullData(self):
        if self.wikiPath != '' and self.seasonAnchor != '': 
            response = urllib.request.urlopen(self.baseUrl + self.wikiPath + '#' + self.seasonAnchor)
            html = response.read()
            parser = BeautifulSoup(html)
            print(self.baseUrl + self.wikiPath + '#' + self.seasonAnchor, self.seasonAnchor, parser.find('span', attrs = {'id': self.seasonAnchor}))

            table = parser.find('span', attrs = {'id': self.seasonAnchor}).parent.findNextSibling('table')
            parsedTable = BeautifulSoup(str(table))
            indexOfTitle = self.getTitleIdx(parsedTable)
            return self.getSeasonTitles(parsedTable, indexOfTitle)

    def getTitleIdx(self, bsTable):
        titleIdx = 0
        pattern = re.compile(r'Title')
        element = bsTable.findAll('th', text = pattern)
    
        if element != '':
            # this is findingAll again the same thing excluding the pattern
            titleIdx = bsTable.findAll('th').index(element[0])
            
        return titleIdx

# returns a map with key = episode number, value = episode title
    def getSeasonTitles(self, bsTable, titleIdx):
        titles = bsTable.findAll('tr', attrs = {'class': 'vevent'})
        titlesDict = dict()
        
        for title in titles:
            row = BeautifulSoup(str(title))
            #TODO depending on which column is the episode number of the season, 
            #    we need to access the first or the second column
            #key = row.find('th').text
            key = row.findAll('td')[0].text

            value = row.findAll('td')[titleIdx -1].text
            re.sub('<[^<]+?>', '', value)
            titlesDict[key] = value
                
        return titlesDict
    
