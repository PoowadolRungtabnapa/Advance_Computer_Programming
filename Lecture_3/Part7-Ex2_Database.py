import psycopg2

try :
    connection = psycopg2.connect(user="webadmin",
                                  password="XVBqxc19866",
                                  host='node1449-testdb.app.ruk-com.cloud',
                                  port='11025',
                                  database='testdb')

    cursor = connection.cursor() 
    
    create_table_query = """CREATE TABLE Comments
            (id             SERIAL PRIMARY KEY,
            name            VARCHAR(50) NOT NULL,
            comment         VARCHAR(1000) NOT NULL);"""
    
    cursor.execute(create_table_query)
    connection.commit()
    print("Table created successfully in PostgreSQL")

except (Exception, psycopg2.DatabaseError) as error :
    print('Error while creating PostgreSQL table', error)

finally :
    if(connection) :
        cursor.close()
        connection.close()
        print('PostgreSQL connection is closed')