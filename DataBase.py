
import sqlite3

db = sqlite3.connect('Database.db')
db.execute('drop table if exists hello')
db.execute('create table hello(firstname txt,lastname txt,age int)')
db.commit()
db.execute('insert into hello(firstname,lastname,age) values ("Aditya" ,"verma",25)')
db.execute('insert into hello(firstname,lastname,age) values ("Addytheriot" ,"verma",25)')
db.execute('insert into hello(firstname,lastname,age) values ("Adylad" ,"verma",25)')
db.execute('insert into hello(firstname,lastname,age) values ("mustafa" ,"verma",25)')
db.commit()
db.execute('update hello set firstname =" Addytheriot" where lastname = "verma"')
db.commit()


import sqlite3

db = sqlite3.connect('Database.db')
db.row_factory=sqlite3.Row

table = db.execute('select  firstname , age from hello')

for each in table:
	print(dict(each))
	
