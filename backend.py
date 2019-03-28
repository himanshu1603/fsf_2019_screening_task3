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



 
# for row in rows:
# 	print(row[1])