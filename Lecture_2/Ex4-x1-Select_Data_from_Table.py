import psycopg2

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
            print(f"name = {row[0]}")
            print(f"comment = {row[1]}")
    
    except (Exception, psycopg2.Error) as error :
        print("Error while fetching data from PostgreSQL", error)

    finally :
        if(connection) :
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

getStudentDetails('a')
    