from peewee import MySQLDatabase

mysql = MySQLDatabase(
    'capstone', 
    user='admin',
    password='Capstone23!',
    host='capstone23.c8rvzpjcouw1.ap-northeast-2.rds.amazonaws.com',
    port='3306',
    charset='utf8mb4'
)