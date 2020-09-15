from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Date
import psycopg2
try :
    connection = psycopg2.connect(user="postgres",
                                  password="Mac126254",
                                  host='127.0.0.1',
                                  port='5432',
                                  database='postgres')
    cursor = connection.cursor()
    connection.autocommit = True
    connection.commit()
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres:Mac126218@127.0.0.1:5432/test'
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
        signature = Comments(name=name, comment=comment)
        db.session.add(signature)
        db.session.commit()
        return redirect(url_for('index'))

except (Exception, psycopg2.Error) as error :
    print('Error while connecting to PostgreSQL',error)
finally :
    if (connection) :
        cursor.close()
        connection.close()
        print('PostgreSQL connection is closed')