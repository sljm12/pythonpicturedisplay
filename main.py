#!/Python25/python
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
        return render.showIndex(folderNames)
    
if __name__ == '__main__':
    app.run()