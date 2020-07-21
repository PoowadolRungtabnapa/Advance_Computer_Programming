import psycopg2

def getStudentDetails(name) :
    try :
        connection = psycopg2.connect(user="postgres",
                                    password="Mac126254",
                                    host='127.0.0.1',
                                    port='5432',
                                    database='mydb')

        cursor = connection.cursor()
        postgreSQL_select_Query = "select * from students where f_name = %s"

        cursor.execute(postgreSQL_select_Query, (name,))
        print("Selecting rows from students table using cursor.fechall")
        student_records = cursor.fetchall()

        print("Print each row and it's colums values")
        for row in student_records :
            print(f"student_id = {row[0]}")
            print(f"f_name = {row[1]}")
            print(f"l_name = {row[2]}")
            print(f"e_mail = {row[3]} \n")
    
    except (Exception, psycopg2.Error) as error :
        print("Error while fetching data from PostgreSQL", error)

    finally :
        if(connection) :
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

getStudentDetails('Poowadol')
getStudentDetails('Thanabode')
getStudentDetails('Kanokwan')
getStudentDetails('Wichittranut')
    