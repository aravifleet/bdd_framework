import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password="",
    database="qa_automation"
)

if connection.is_connected():
    print("MySQL connection successful!")

connection.close()