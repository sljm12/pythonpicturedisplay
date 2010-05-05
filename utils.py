import os.path
import os

class FileFinder:
    def __init__(self,folderPath):
        self.folderPath=folderPath
    
    def getFiles(self):
        '''
        get the list of files in the folderPath
        '''
        if os.path.exists(self.folderPath) and os.path.isdir(self.folderPath):
            return os.listdir(self.folderPath)
        else:
            return ()
            
    def findFile(self,extension):
        '''
        Find a file with a specific extention ie. like jpg
        extention = extention of the file that you want to find
        '''
        filesList=[]
        files=self.getFiles()
        
        for file in files:
            splits=file.split('.',1)
            if len(splits) == 2:
                if splits[1].upper() == extension.upper():
                    filesList.append(file)
        return filesList
            
            
if __name__ == '__main__':
    a=FileFinder('C:/Documents and Settings/stephen/Desktop/Chloe')
    print a.findFile('jpg')