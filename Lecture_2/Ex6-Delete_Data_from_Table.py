import psycopg2

def deletestudents(name) :
    try :
        connection = psycopg2.connect(user="postgres",
                                    password="Mac126218",
                                    host='127.0.0.1',
                                    port='5432',
                                    database='mydb')

        cursor = connection.cursor()
        postgresSQL_select_Query = "select * from students"
        cursor.execute(postgresSQL_select_Query, (name,))
        print("Before Delete")
        student_records = cursor.fetchall()
        for row in student_records :
            print(row,'\n')
        
        postgresSQL_select_Query = "delete from students where f_name = %s"
        cursor.execute(postgresSQL_select_Query, (name,))
        connection.commit()

        postgresSQL_select_Query = "select * from students "
        cursor.execute(postgresSQL_select_Query, (name,))
        print("After Delete")
        student_records = cursor.fellchall()
        for row in student_records :
            print(row, '\n')

    except (Exception, psycopg2.Error) as error :
        print("Error while fetching data from PostgreSQL", error)

    finally :
        if(connection) :
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

deletestudents('Poowadol')