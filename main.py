import web
import repos

urls=('/','index',
      '/showFolder','ShowFolder')

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
        folder=db.FolderRepos()
        folderPictures=folder.getPicturesInFolder(i.name)
        return render.showFolder(i.name,folderPictures)

class ShowIndex:
    def GET(self):
        return 'ShowIndex'
    
if __name__ == '__main__':
    app.run()