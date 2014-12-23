import sqlite3

conn = sqlite3.connect("internapp.db")

curs = conn.cursor()

curs.execute('''drop table student''')
curs.execute('''create table student (student_id int,
				grad_year int,
				first_name text,
				last_name text,
				major text,
				luther_user text );''' )

curs.execute('''insert into student values (123,1986,'brad','miller','CS','millbr01')''')
curs.execute('''insert into student values (234,2016,'john','smith','CS','smitjo01')''')	
curs.execute('''insert into student values (345,2000,'bjorn','norderhaug','English','nordbj01')''')
curs.execute('''insert into student values (567,2020,'jake','ford','Math','fordja01')''')		
conn.commit()

rows = curs.execute('''select first_name, grad_year from student where major='CS' or major = 'English' order by grad_year desc''')

for row in rows:
	print(row)
