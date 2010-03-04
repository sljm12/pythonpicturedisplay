import utils

class ReposFactory:
    '''
    Factory for creating various repositories
    '''
    @staticmethod
    def getFolderRepos():
        return FolderRepos()

class FolderRepos:
    def getRealFolderPath(self,id):
        '''
        Returns the actual folder path in the system
        '''
        return 'C:/Resources/HtmlPopup/images'
    
    def getWebFolderPath(self,id):
        '''
        Returns the web folder path as defined by the id
        '''
        
        return '/test'
    
    def getPicturesInFolder(self,id):
        '''
        Get the pictures from a particular path
        '''
        realPath=self.getRealFolderPath(id)  
        fileFinder=utils.FileFinder(realPath)
        files=fileFinder.findFile('jpg')
        return self.convertToWebpath(id,files)
    
    def convertToWebpath(self,id,files):
        filesList=[]
        webPath=self.getWebFolderPath(id)
        for f in files:
            filesList.append(webPath+'/'+f)
        return filesList

if __name__ == '__main__':
    f=ReposFactory.getFolderRepos()
    files=f.getPicturesInFolder(1)
    print files