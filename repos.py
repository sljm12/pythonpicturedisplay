import utils,db

class ReposFactory:
    '''
    Factory for creating various repositories
    '''
    @staticmethod
    def getFolderRepos():
        return FolderRepos(db.DaoFactory.getDirDao())

class FolderRepos:
    def __init__(self,dirDao):
        self.dirDao=dirDao
        
    def getAllFolders(self):        
        return self.dirDao.getAll()
    
    def getRealFolderPath(self,id):
        '''
        Returns the actual folder path in the system
        '''
        dir=self.dirDao.getDirById(id)
        return dir.real_path
    
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