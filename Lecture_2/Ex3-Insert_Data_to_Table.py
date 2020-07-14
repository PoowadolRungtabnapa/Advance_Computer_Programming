import psycopg2

try :
    connection = psycopg2.connect(user="postgres",
                                  password="Mac126218",
                                  host='127.0.0.1',
                                  port='5432',
                                  database='mydb')
                                
    cursor = connection.cursor()

    postgres_insert_query = """ INSERT INTO students (student_id, f_name, l_name, e_mail) VALUES (%s,%s,%s,%s)"""
    record_to_insert = ('3100796777241','Poowadol',
                        'Rungtabanapa',"s6206022610033@email.kmutnb.ac.th")
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