#!/usr/bin/python.exe
import web
import repos
import os.path
import dircache

urls=('/','index',
      '/showFolder','ShowFolder',
      '/showIndex','ShowIndex',
      '/showDirectory','ShowDirectory')

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

class ShowDirectory:
    def GET(self):
        i=web.input(Dir=None)
        print i
        path='c:/temp/pics'
        if i.Dir != None:
            path=os.path.join(path,i.Dir)
        print path
        dirfiles=dircache.listdir(path)
        files=[]
        dirs=[]
        for df in dirfiles:
            df_path=os.path.join(path,df)
            if os.path.isdir(df_path):
                dirs.append(df)
            else:
                files.append(df)
        return render.showDirectory(i.Dir,path,files,dirs)
    
    
if __name__ == '__main__':
    app.run()