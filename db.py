import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
import settings

engine=create_engine(settings.sql_connection,echo=False)

Base=declarative_base()

Session = sessionmaker(bind=engine)



class DaoFactory:
    @staticmethod
    def getDirDao():
        return DirDao.Instance()

class Dir(Base):
    __tablename__='dirs'
    
    id=Column(Integer,primary_key=True)
    real_path=Column(String)
    
    def __init__(self,real_path):
        self.real_path=real_path
    
    def __repr__(self):
        return "<Dir '%s')>" % (id)

class DirDao:
    __instance__=None
    
    @staticmethod
    def Instance():
        if DirDao.__instance__ == None:
            DirDao.__instance__=DirDao()
        return DirDao.__instance__
            
    def save(self,dir):
        '''
        Saves a dir instance, returns the id when done
        '''
        session=Session()
        session.add(dir)
        session.commit()
        return dir.id
    
    def getAll(self):
        session=Session()
        results=session.query(Dir).all()
        return results
    
    def getDirById(self,id):
        session=Session()
        dir=session.query(Dir).filter(Dir.id == id).first()
        return dir

#Last line to init all the DB, dont think its a good place to put this    
Base.metadata.create_all(engine)

if __name__ == '__main__':
        
    session=Session()
    
    user=Dir('c:/test')
    session.add(user)
    session.commit()
    print user.id
    
    newDir=session.query(Dir).all()
    print newDir
    
    print DirDao.Instance().save(Dir('c:/fun'))
    print DirDao.Instance()