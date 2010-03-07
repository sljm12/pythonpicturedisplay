'''
Command line admin tool
'''
import db
from optparse import OptionParser
import os.path

def crawl(dir):
    '''
    Crawl each of the dir 
    '''
    if os.path.exists(dir) and os.path.isdir(dir):
        os.path.walk(dir,visit,"")

def visit(arg,dirname,names):
    '''
    Processes the dir, looking for tag.json and adding that dir to the database
    '''
    print 'Processing '+dirname
    dirDao=db.DaoFactory.getDirDao()
    dirDao.save(db.Dir(dirname))

if __name__ == '__main__':
    parser=OptionParser()
    parser.add_option("--drop-and-create",
                      action="store_true",
                      default="False",
                      dest="drop_create",help="Drop and recreate the DB")
    
    parser.add_option("-c","--crawl",action="store",type="string",dest="directory",
                      help="Crawl the Directory and add information to the db")
    
    args=['-c','c:\\temp\\pics']
    (options,arg)= parser.parse_args(args)
    parser.print_help()
    db.Base.metadata.create_all(db.engine)
    
    if options.drop_create == True:
        print 'Dropping tables'
        db.Base.metadata.drop_all(db.engine)
    if options.directory != None:
        print 'Crawling'
        crawl(options.directory)
        dirDao=db.DaoFactory.getDirDao()
        db.Base.metadata.create_all(db.engine)
        
        
