import psycopg2

try :
    connection = psycopg2.connect(user="postgres",
                                  password="Mac126254",
                                  host='127.0.0.1',
                                  port='5432',
                                  database='mydb')
                                
    cursor = connection.cursor()

    postgres_insert_query = """ INSERT INTO subjects (subject_id, subject_name, creadit, teacher_id) VALUES (%s,%s,%s,%s)"""
    record_to_insert = ('060233201','LabNetwork',
                        3,"WKN")
    cursor.execute(postgres_insert_query, record_to_insert)

    record_to_insert = ('060233112','DataEng',
                        3,"STS")
    cursor.execute(postgres_insert_query, record_to_insert)

    record_to_insert = ('040203123','DisMath',
                        3,"ACK")
    cursor.execute(postgres_insert_query, record_to_insert)

    connection.commit()
    count = cursor.rowcount
    print(count, 'record inserted succrssfully into students table')

except (Exception, psycopg2.Error) as error :
    if(connection) :
        print('Failed to insert record into students table',error)

finally :
    if(connection) :
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")