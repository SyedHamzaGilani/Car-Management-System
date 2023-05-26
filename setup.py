import cx_Oracle
connection = cx_Oracle.connect('system/69-Gilani-53@localhost:1521/orcl')
cursor = connection.cursor()
query = "SELECT * FROM LOGIN"
cursor.execute(query)
row = cursor.fetchone()
print(row[0])
print(row[1])
connection.commit()
cursor.close()