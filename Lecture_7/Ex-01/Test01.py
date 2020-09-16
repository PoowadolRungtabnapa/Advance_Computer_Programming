import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, User

engine = create_engine('sqlite://user.db', echo=False)

#Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

user1 = User(name='user1', fullname='Ed Jones', nickname='ed')
'''user3 = User(name='user3', fullname='STEd Jones', nickname='STed')
user4 = User(name='user4', fullname='WTEd Jones', nickname='WTed')

session.add_all(user3, user4)'''

session.add(user1)
session.commit()

'''for instance in session.query(User).order_by(User_id) :
    print(instance.name, instance.fullname)'''