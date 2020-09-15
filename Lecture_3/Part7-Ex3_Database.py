from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Date
import psycopg2
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Mac126218@127.0.0.1:5432/test'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Comments(db.Model):
    __tablename__ = 'comments'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    comment = Column(String)

@app.route('/')
def index() :
    result = Comments.query.all()
    return render_template('index.html', result=result)

@app.route('/sign')
def sign() :
    return render_template('sign.html')

@app.route('/process', methods=['POST'])
def process() :
    name = request.form['name']
    comment = request.form['comment']
    getStudentDetails(name)
    
    '''signature = Comments(name=name, comment=comment)
    db.session.add(signature)
    db.session.commit()'''
    return redirect(url_for('index'))

def getStudentDetails(name) :
    try :
        connection = psycopg2.connect(user="postgres",
                                    password="Mac126218",
                                    host='127.0.0.1',
                                    port='5432',
                                    database='test')

        cursor = connection.cursor()
        postgreSQL_select_Query = "select * from comments where name = %s"

        cursor.execute(postgreSQL_select_Query, (name,))
        print("Selecting rows from comments table using cursor.fechall")
        student_records = cursor.fetchall()

        print("Print each row and it's colums values")
        for row in student_records :
            print(f"id = {row[0]}")
            print(f"name = {row[1]}")
            print(f"comment = {row[2]}")

    except (Exception, psycopg2.Error) as error :
        print("Error while fetching data from PostgreSQL", error)

    finally :
        if(connection) :
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

if __name__ == '__main__' :
    app.run(debug=True)

#node1449-testdb.app.ruk-com.cloud:11025