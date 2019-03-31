import sqlite3

import dictnry



def show_designations(table):
	conn = sqlite3.connect('steel_sections.sqlite')
	cur = conn.cursor()
	query = "SELECT * FROM {}".format(table)
	cur.execute(query) 
	rows = cur.fetchall()
	conn.close()
	return rows

def show_details(text):
	conn = sqlite3.connect('steel_sections.sqlite')
	cur = conn.cursor()

	table = dictnry.Type[text]
	query = "SELECT * FROM {} WHERE designation=?".format(table)

	cur.execute(query,(text,)) 
	row = cur.fetchall()
	conn.close()
	return row

def setDataToDB(data, table):
	conn = sqlite3.connect('steel_sections.sqlite')
	cur = conn.cursor()

	k = 0

	if data[0] in dictnry.Type.keys():
		pass
	else:
		k = 1

	if k == 1:

		dictnry.dWrite(data[0], table)


		if table == "Angles":
			query = "INSERT INTO {} VALUES (NULL,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)".format(table)	
			cur.execute(query,(data[0],data[1],data[2],data[3],data[4],data[5],data[6],data[7],data[8],data[9],data[10],data[11],data[12],data[13],data[14],data[15],data[16],data[17],data[18],data[19],data[20],data[21],data[22]))

		elif table == "Beams":
			query = "INSERT INTO {} VALUES (NULL,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)".format(table)	
			cur.execute(query,(data[0],data[1],data[2],data[3],data[4],data[5],data[6],data[7],data[8],data[9],data[10],data[11],data[12],data[13],data[14],data[15],data[16],data[17],data[18]))

		elif table == "Channels":
			query = "INSERT INTO {} VALUES (NULL,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)".format(table)	
			cur.execute(query,(data[0],data[1],data[2],data[3],data[4],data[5],data[6],data[7],data[8],data[9],data[10],data[11],data[12],data[13],data[14],data[15],data[16],data[17],data[18],data[19]))

		conn.commit()
		conn.close()








 
