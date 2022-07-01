
import mysql.connector
import pandas as pd

my_db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="12345",     #remark: use the password as string
)

my_cursor = my_db.cursor(buffered=True)




def check_if_database_or_create(name_of_database :str)-> bool:
    """
    checking the database name if present
    else create one
    param:'name_of_database' is the name to be searched in database
    return:bool
    """
    
    my_cursor.execute('SHOW DATABASES')
    
    
    for i in my_cursor:
        if name_of_database == i[0]:
            print("db is present")
            return True

        
    
    print("database is not present ,creating one")
    my_cursor.execute('CREATE DATABASE JOBS')
    return False
    


def print_all_database():

    """ 
    showing all the database present
    return:None
    """
    my_cursor.execute('SHOW DATABASES')
    for i,j in enumerate(my_cursor):
        print(i, j)


def use_database(name_of_database: str):
    """
    fucntion will check if database is present if present then use , else return

    param:'name_of_database' its takes database name
    return:None
    
    """
   
    try:
        command = 'USE ' + name_of_database
        print(command)
        my_cursor.execute(command)
        print("done use command")
    except:
        print("Create the database first , database not present")


def create_table():
    """


    """
    sql = "CREATE TABLE JOB_COMPANY (Id INT AUTO_INCREMENT PRIMARY KEY,company varchar(255), job_name varchar(255));"
    try:
        my_cursor.execute(sql)
        print("TABLE CREATED SUCESSFULL:")
    except:
        print("table already present or check the syntax")
    

def insert_data(list_of_details : list):
    """
    insert data will take the list of data and insert into the table

    param:'list_of_details' is the provided list
    return:None
    """
    for i in list_of_details:
        sql = "INSERT INTO JOB_COMPANY (company,job_name) values (%s , %s)"
        values = (i[0],i[1])
        my_cursor.execute(sql,values)
    my_db.commit()
    print("data inserted sucessfull")
    
def get_queres():
    """This will return the pandas dataframe object"""
    quere = "SELECT * FROM JOB_COMPANY;"
    my_cursor.execute(quere)
    read = pd.read_sql(quere, my_db)
    print(read.head())
    
    







# print_all_database()  
# check_if_database_or_create("JOBS")
use_database("JOBS")
# create_table()
# insert_data([['xyc','python']])
get_queres()


my_db.commit()
# my_db.close()



