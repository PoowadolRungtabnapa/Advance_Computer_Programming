from Lecture_7.crud import Session
from models import Book

s = Session()

bps = s.query(Book.title, Book.author).all()
for bp in bps :
    print('Title : ', bp.title)
    print('Author : ', bp.author)
    print('_____'*20)
    
s.close()