import utils,db

class ReposFactory:
    '''
    Factory for creating various repositories
    '''
    @staticmethod
    def getFolderRepos():
        return FolderRepos(db.DaoFactory.getDirDao(),RealPathWebConvert())

class FolderRepos:
    def __init__(self,dirDao,pathConverter):
        self.dirDao=dirDao
        self.pathConverter=pathConverter
        
    def getAllFolders(self):        
        return self.dirDao.getAll()
    
    def getRealFolderPath(self,id):
        '''
        Returns the Dir object as specificed by the id
        '''
        dir=self.dirDao.getDirById(id)
        return dir
    
    def getWebFolderPath(self,id):
        '''
        Returns the web folder path as defined by the id
        '''
        directory=self.getRealFolderPath(id)
        
        
        return self.pathConverter.convertRealToWeb(directory.real_path)
    
    def getPicturesInFolder(self,id):
        '''
        Get the pictures from a particular path
        '''
        directory=self.getRealFolderPath(id)  
        fileFinder=utils.FileFinder(directory.real_path)
        files=fileFinder.findFile('jpg')
        return self.convertToWebpath(id,files)
    
    def convertToWebpath(self,id,files):
        filesList=[]
        webPath=self.getWebFolderPath(id)
        for f in files:
            filesList.append(webPath+'/'+f)
        return filesList

class RealPathWebConvert:
    def convertRealToWeb(self,path):
        webpath=path.replace('c:/temp/pics','http://localhost/pics',1)
        return webpath.replace('\\','/')
    
if __name__ == '__main__':
    f=ReposFactory.getFolderRepos()
    files=f.getPicturesInFolder(1)
    print files