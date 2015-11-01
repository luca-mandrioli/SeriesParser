'''
Created on 9 Dec 2013

@author: Luca.Mandrioli
'''

import os, re

class FileRenamer(object):
    
    def __init__(self, basePath, seriesName, seasonName, seasonNumber):
        self.basePath = basePath
        self.seriesName = seriesName
        self.seasonName = seasonName
        self.seasonNumber = seasonNumber
        
    def renameSeries(self, seriesDict):
        path = os.path.join(self.basePath, self.seriesName, self.seasonName +' ' + str(self.seasonNumber))

        if os.path.exists(path) == False:
            print('path does not exist', path)
            return
        
        for file in os.listdir(path):
            fileName, fileExtension = os.path.splitext(file)
            nums = re.findall(r'\d+', fileName)
            newFileName = ''

            for num in nums:
                frontZero = '' 
#                if num == self.seasonNumber:
                user_input = input('Is '+ str(num) + ' the number of episode (y/n)?')
                if(user_input.lower() == 'y' or user_input.lower() == 'yes'):
                    num = num.lstrip('0')

                    if (str(num) in seriesDict and seriesDict[str(num)] != ''):
                        if(int(num) < 10):
                            frontZero = '0'
                             
                        newFileName = self.seasonNumber + 'x' + frontZero + num + ' - ' + seriesDict[str(num)].replace('"','') + fileExtension
                        break

            if newFileName != '':
                newPath = os.path.join(path, newFileName)
                oldPath = os.path.join(path, file)

                if(newPath != oldPath):
                    newFileName = self.removeUnwantedChar(newFileName, '\/:*?"<>|\n\r')
                    print(newFileName)
                    os.rename(os.path.join(path, file), os.path.join(path, newFileName))
                    
    def removeUnwantedChar(self, value, deletechars):
        return ''.join(ch for ch in value if ch not in deletechars) 
#         for c in deletechars:
#             value = value.replace(c,'_')
#             return value;