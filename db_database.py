import sqlite3
class Karmand:
    def __init__(self,db):
        self.con = sqlite3.connect(db)
        self.cur = self.con.cursor()
        self.cur.execute('''CREATE TABLE IF NOT EXISTS database (id integer primary key , fname text ,
                         lname text , city text , phone text)
                         ''')
        self.con.commit()
#===========inset============================
    def insert (self , fname , lname , city , phone):
        self.cur.execute('INSERT INTO database (id , fname , lname , city , phone) VALUES (null , ? , ? , ? , ? )',
                         (fname , lname , city , phone))
        self.con.commit()
        print('insert recorded')
#===========show=============================
    def Show(self):
        self.cur.execute('SELECT * FROM database ')
        records = self.cur.fetchall()
        return records
#===========delete===========================
    def delete(self , id):
        self.cur.execute('DELETE FROM database where id = ?',(id,))
        self.con.commit()
#==========update============================
    def Update(self, id, fname, lname , city , phone):
        self.cur.execute("""
                            UPDATE database SET fname = ?, lname = ?, city = ? , phone = ? WHERE id = ? """ ,
                            (fname, lname , city , phone , id))
        self.con.commit()
#==========search============================
    def Search (self,input_):
        self.cur.execute("""SELECT * FROM database WHERE id = ? or fname = ? or lname = ?
                         or city = ? or phone = ? """,(input_,input_,input_,input_,input_))
        return self.cur.fetchall()

    