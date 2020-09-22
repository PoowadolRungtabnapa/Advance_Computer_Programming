from models import Base, Member
from sqlalchemy import create_engine, update
from sqlalchemy.orm import sessionmaker, query
import datetime

db_uri = 'sqlite:///Ex2.db'
engine = create_engine(db_uri, echo=False)

#Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()
'''
user = Member(
    name='Ftoddy',
    description='im testing this',
    vip=True,
    join_date=datetime.datetime.today(),
    number=45.0
)
session.add(user)

print(user)

#for Delete in session.query(Member).order_by(Member.id) :
Delete = session.query(Member).filter(Member.id==3).first()
session.delete(Delete)'''

#session.update(Member).where(Member.id==2).value(name='JSON')

session.query(Member).filter(Member.id == 2).update({Member.name:"JohnSon"})

session.commit()
