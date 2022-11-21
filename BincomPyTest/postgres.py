import psycopg2

hostname = 'localhost'
database = 'color'
username = 'postgres'
pwd = 'po$@|p@$$#0^d'
port_id = '5432'
connect = None
curs = None

try:
 connect = psycopg2.connect(
  host = hostname,
  dbname = database,
  user = username,
  password = pwd,
  port = port_id
 )

 curs = connect.cursor()

 curs.execute('DROP TABLE IF EXISTS color')

 create_script = """CREATE TABLE IF NOT EXISTS color (
  id int PRIMARY KEY,
  color varchar(40) NOT NULL,
  frequency int
 )
 """

 curs.execute(create_script)

 insert_script = 'INSERT INTO color (id, color, frequency) VALUES (%s, %s, %s)'


 insert_values = [(1, 'Yellow', 5), (2, 'Green', 10), (3, 'Brown', 6), (4, 'Blue', 31), (5, 'Orange', 9), (6, 'Red', 9), (7, 'White', 16), (8, 'Cream', 2), (9, 'Arsh', 1), (10, 'Black', 1), (11, 'Pink', 4)]

 for record in insert_values:
  curs.execute(insert_script, record)

 connect.commit()

except Exception as error:
 print(error)
finally:
 if curs is not None:
  curs.close()
 if connect is not None:
  connect.close()
 