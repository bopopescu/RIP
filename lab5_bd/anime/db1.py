import pymysql
pymysql.install_as_MySQLdb()

db=pymysql.connect(
    host='localhost',
    user='dbuser',
    passwd='123',
    db='anime'
)

c=db.cursor()

c.execute('INSERT INTO anime (name, description, author) VALUES (%s, %s, %s);', ("Унесенные призраками", "Первое, что вспомнила", "Хайао Миядзаки"))

db.commit()

c.execute('SELECT * FROM anime;')

entries=c.fetchall()

for e in entries:
    print(e)

c.close()
db.close()