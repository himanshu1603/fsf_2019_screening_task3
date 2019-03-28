import sqlite3

conn = sqlite3.connect('steel_sections.sqlite')
def show_beams():
	cur = conn.cursor()
	cur.execute("SELECT * FROM Beams") 
	rows = cur.fetchall()
	# conn.close()
	return rows

def show_details(text):
	cur = conn.cursor()
	cur.execute("SELECT * FROM Beams WHERE designation=?",(text,)) 
	row = cur.fetchall()
	# conn.close()
	return row

def setDataToDB(data):
	cur = conn.cursor()
	# cur.execute("SELECT * FROM Beams WHERE designation=?",(text,))
	cur.execute("INSERT INTO Beams VALUES (NULL,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",(data[0],data[1],data[2],data[3],data[4],data[5],data[6],data[7],data[8],data[9],data[10],data[11],data[12],data[13],data[14],data[15],data[16],data[17],data[18]))
	




 
