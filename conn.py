import mysql.connector
from mysql.connector import Error
import database_config

class Connect:
    """ Connect to MySQL database """
    def __init__(self):
        self.connection = None
    try:
        connection = mysql.connector.connect(host=database_config.host,
                                             database=database_config.database,
                                             user=database_config.user,
                                             password=database_config.password)
        cursor = connection.cursor()
    except Error as e:
        print(e)

def executor(query):
    """ Execute SQL statement """
    try:
        Connect.cursor.execute(query)
        r = Connect.cursor.fetchall()
    except Error as e:
        r = 1
        print(e)
    return r

def insert_main(query, vals):
    """ Insert data into MySQL database """
    try:
        Connect.cursor.execute(query, vals)
        Connect.connection.commit()
    except Error as e:
        print(e)
    return 0

def update_main(query, vals):
    """ Update data in MySQL database """
    try:
        Connect.cursor.execute(query, vals)
        Connect.connection.commit()
    except Error as e:
        print(e)
    return 0

def delete_main(query, vals):
    """ Delete data in MySQL database """
    try:
        Connect.cursor.execute(query, vals)
        Connect.connection.commit()
    except Error as e:
        print(e)
    return 0

def select_main(query):
    """ Select data from MySQL database """
    try:
        Connect.cursor.execute(query)
        r = Connect.cursor.fetchall()
    except Error as e:
        print(e)
    return r

def select_main_one(query):
    """ Select data from MySQL database """
    try:
        Connect.cursor.execute(query)
        r = Connect.cursor.fetchone()
    except Error as e:
        print(e)
    return r

def select_main_all(query):
    """ Select data from MySQL database """
    try:
        Connect.cursor.execute(query)
        r = Connect.cursor.fetchall()
    except Error as e:
        print(e)
    return r

def select_main_all_dict(query):
    """ Select data from MySQL database """
    try:
        Connect.cursor.execute(query)
        r = Connect.cursor.fetchall()
    except Error as e:
        print(e)
    return r

def select_main_all_dict_one(query):
    """ Select data from MySQL database """
    try:
        Connect.cursor.execute(query)
        r = Connect.cursor.fetchall()
    except Error as e:
        print(e)
    return r


def select_main_all_dict_one_one(query):
    """ Select data from MySQL database """
    try:
        Connect.cursor.execute(query)
        r = Connect.cursor.fetchone()
    except Error as e:
        print(e)
    return r
class DataBase:
    def insert_user(chat_id,firstName,lastName, username):
        if str(chat_id) in str(executor('SELECT CHAT_ID FROM users')):
            print("Saved User")
            pass
        else:
           query = 'INSERT INTO users(CHAT_ID, FIRST_NAME, LAST_NAME, USER_NAME) VALUES (%s,%s,%s,%s)'
           vals = (chat_id, firstName, lastName,username)
           insert_main(query, vals)
           print("New User Saved")
    def func(function):
        try:
            if Connect.connection.is_connected():
                '''db_Info = connection.get_server_info()
                print("Connected to MySQL Server version ", db_Info)
                cursor = connection.cursor()
                cursor.execute("select database();")
                record = cursor.fetchone()
                print("You're connected to database: ", record)
                query = "select * from users;"
                print(executor(query))'''
                function
                #Connect.connection.close()
                #Connect.connection.close()

        except Error as e:
            print("Error while connecting to MySQL", e) 
#print(executor('SELECT CHAT_ID FROM users'))
