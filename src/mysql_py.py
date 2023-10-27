import pymysql

connection = pymysql.connect(host='localhost',
                             user='root',
                             password='jsk2819',
                             database='simulator')

cursor = connection.cursor()

# data = [
#     (99, 'qwe',1000),
#     (98, 'asd', 2000)
# ]
data = []
for i in range(1, 101):
    row = (i, 'name'+str(i), i*2000)
    data.append(row)

query = "INSERT INTO test2 (id, nam, num) VALUES (%s, %s, %s)"

# cursor.executemany(query, data)
# connection.commit()
# cursor.close()
# connection.close()
try:
    cursor.executemany(query, data)
    connection.commit()
except pymysql.MySQLError as e:
    print("Error: ", str(e))
    connection.rollback()
finally:
    cursor.close()
    connection.close()
