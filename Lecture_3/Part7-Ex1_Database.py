import psycopg2

try :
    connection = psycopg2.connect(user="",
                                  password="",
                                  host='',
                                  port='',
                                  database='postgres')
    
    connection.autocommit = True

    cursor = connection.cursor() 
    
    sql = """CREATE database TestDB"""
    
    cursor.execute(sql)
    print("Database created successfully........")

except (Exception, psycopg2.DatabaseError) as error :
    print('Error while creating PostgreSQL table', error)

finally :
    if(connection) :
        cursor.close()
        connection.close()
        print('PostgreSQL connection is closed')