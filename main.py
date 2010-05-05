#!/usr/bin/python.exe
import web
import repos

urls=('/','index',
      '/showFolder','ShowFolder',
      '/showIndex','ShowIndex')

app=web.application(urls,globals())
render=web.template.render('template/');

class index:
    def GET(self):
        name='Bob'
        name1='Test'
        return render.index(name,name1)

class ShowFolder:
    def GET(self):
        i=web.input(name=None)
        folder=repos.ReposFactory.getFolderRepos()
        folderPictures=folder.getPicturesInFolder(i.name)
        return render.showFolder(i.name,folderPictures)

class ShowIndex:
    def GET(self):
        folder=repos.ReposFactory.getFolderRepos()
        folderNames=folder.getAllFolders()
        folderMap={}
        for fName in folderNames:
            picture=self.getFirstPictureInFolder(fName)
            folderMap[fName]=picture
        return render.showIndex(folderMap)
    
    def getFirstPictureInFolder(self,folderName):
        folder=repos.ReposFactory.getFolderRepos()
        pictures=folder.getPicturesInFolder(folderName.id)
        if len(pictures) > 0:
            return pictures[0]
        else:
            return ''
    
if __name__ == '__main__':
    app.run()