'''
Command line admin tool
'''
import db
from optparse import OptionParser


if __name__ == '__main__':
    parser=OptionParser()
    parser.add_option("--drop-and-create",action="store_true",default="False",dest="drop_create",help="Drop and recreate the DB")
    
    parser.add_option("-c","--crawl",action="store",type="string",dest="directory",
                      help="Crawl the Directory and add information to the db")
    
    args=['']
    (options,arg)= parser.parse_args(args)
    parser.print_help()
    
    if options.drop_create:
        db.Base.metadata.drop_all(db.engine)
