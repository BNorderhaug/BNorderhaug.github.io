import sqlite3

conn = sqlite3.connect("companyapp.db")

curs = conn.cursor()
curs.execute('''drop table student''')
curs.execute('''create table student (student_id int,
				grad_year int,
				first_name text,
				last_name text,
				major text,
				luther_user text,
				comp_id int,
				foreign key(comp_id) references company(comp_id) ;''' )

curs.execute('''insert into student values (123,1986,'brad','miller','CS','millbr01')''')
curs.execute('''insert into student values (234,2016,'john','smith','CS','smitjo01')''')	
curs.execute('''insert into student values (345,2000,'bjorn','norderhaug','English','nordbj01')''')
curs.execute('''insert into student values (567,2020,'jake','ford','Math','fordja01')''')		
conn.commit()

curs.execute('''drop table company''')
curs.execute('''create table company (comp_name text,
				year_created int,
				stock_ind int,
				comp_type text,
				CEO_name text,
				comp_id int) ;''' )
				
curs.execute('''insert into company values ('McDonalds',1986,187.65,'fast food','Ronald McDonald', '1')''')
curs.execute('''insert into company values ('Nike',1970,53.23,'clothing','Usain Bolt', '2')''')	
curs.execute('''insert into company values ('Oracle',1985,123.34,'technology','Larry Ellison','3')''')
curs.execute('''insert into company values ('Taco Bell',1995,23.53,'fast food','Taco Man','4')''')		
conn.commit()

curs.execute('''drop table internship''')
curs.execute(''' create table internship (comp_id int,
					student_id int,
					date text,
					language text,
					paid text,
					description text );''' )

curs.execute('''insert into internship values ( ''')

rows = curs.execute('''select comp_name, year_created, stock_ind, comp_type from company''')

select first_name, from student, internship, company
where student.sid = internship.sid and
		internship.comp_id = company.comp_id and
		company.name = 'ibm'

OR

select first_name
from student natural join internship natural join company
where company.name = 'ibm'

for row in rows:
	print(row)