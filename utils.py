import os.path
import os

class FileFinder:
    def __init__(self,folderPath):
        self.folderPath=folderPath
    
    def getFiles(self):
        if os.path.exists(self.folderPath) and os.path.isdir(self.folderPath):
            return os.listdir(self.folderPath)
        else:
            return ()
            
    def findFile(self,extension):
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