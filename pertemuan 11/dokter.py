from db import DBConnection as mydb

class Dokter:

    def __init__(self):
        self.__id=None
        self.__nip=None
        self.__nama=None
        self.__jk=None
        self.__spesialis=None
        self.__tempat_bertugas=None
        self.conn = None
        self.affected = None
        self.result = None
           
    @property
    def id(self):
        return self.__id

    @property
    def nip(self):
        return self.__nip

    @nip.setter
    def nip(self, value):
        self.__nip = value

    @property
    def nama(self):
        return self.__nama

    @nama.setter
    def nama(self, value):
        self.__nama = value

    @property
    def jk(self):
        return self.__jk

    @jk.setter
    def jk(self, value):
        self.__jk = value

    @property
    def spesialis(self):
        return self.__spesialis

    @spesialis.setter
    def spesialis(self, value):
        self.__spesialis = value

    @property
    def tempat_bertugas(self):
        return self.__tempat_bertugas

    @tempat_bertugas.setter
    def tempat_bertugas(self, value):
        self.__tempat_bertugas = value

    def simpan(self):
        self.conn = mydb()
        val = (self.__nip, self.__nama, self.__jk, self.__spesialis, self.__tempat_bertugas)
        sql="INSERT INTO dokter (nip, nama, jk, spesialis, tempat_bertugas) VALUES " + str(val)
        self.affected = self.conn.insert(sql)
        self.conn.disconnect
        return self.affected

    def update(self, id):
        self.conn = mydb()
        val = (self.__nip, self.__nama, self.__jk, self.__spesialis, self.__tempat_bertugas, id)
        sql="UPDATE dokter SET nip = %s, nama = %s, jk=%s, spesialis=%s, tempat_berteduh=%s WHERE id=%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected

    def updateByNIP(self, nip):
        self.conn = mydb()
        val = (self.__nama, self.__jk, self.__spesialis, self.__tempat_bertugas, nip)
        sql="UPDATE dokter SET nama = %s, jk=%s, spesialis=%s, tempat_bertugas=%s WHERE nip=%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected        

    def delete(self, id):
        self.conn = mydb()
        sql="DELETE FROM dokter WHERE id='" + str(id) + "'"
        self.affected = self.conn.delete(sql)
        self.conn.disconnect
        return self.affected

    def deleteByNIP(self, nip):
        self.conn = mydb()
        sql="DELETE FROM dokter WHERE nip='" + str(nip) + "'"
        self.affected = self.conn.delete(sql)
        self.conn.disconnect
        return self.affected

    def getByID(self, id):
        self.conn = mydb()
        sql="SELECT * FROM dokter WHERE id='" + str(id) + "'"
        self.result = self.conn.findOne(sql)
        self.__nip = self.result[1]
        self.__nama = self.result[2]
        self.__jk = self.result[3]
        self.__spesialis = self.result[4]
        self.__tempat_bertugas = self.result[5]
        self.conn.disconnect
        return self.result

    def getByNIP(self, nip):
        a=str(nip)
        b=a.strip()
        self.conn = mydb()
        sql="SELECT * FROM dokter WHERE nip='" + b + "'"
        self.result = self.conn.findOne(sql)
        if(self.result!=None):
            self.__nip = self.result[1]
            self.__nama = self.result[2]
            self.__jk = self.result[3]
            self.__spesialis = self.result[4]
            self.__tempat_bertugas = self.result[5]
            self.affected = self.conn.cursor.rowcount
        else:
            self.__nip = ''
            self.__nama = ''
            self.__jk = ''
            self.__spesialis = ''
            self.__tempat_bertugas = ''
            self.affected = 0
        self.conn.disconnect
        return self.result

    def getAllData(self):
        self.conn = mydb()
        sql="SELECT * FROM dokter"
        self.result = self.conn.findAll(sql)
        return self.result
    
# Tampilkan semua Data
A = Dokter()
B = A.getAllData()
print(B)

# # Entry Data
# A = Dokter()
# A.nip = "1089"
# A.nama = "dr.ijat"
# A.jk = "L"
# A.spesialis = "Kandungan"
# A.tempat_bertugas = "Rs.Permata"
# A.simpan()
# B = A.getAllData()
# print(B) 

# # Update data
# A = Dokter()
# nip = "1022"
# A.nama = "Yaya"
# A.jk = "P"
# A.spesialis = "Ginjal"
# A.tempat_bertugas = "Rs.Mitra"
# A.updateByNIP(nip)
# B = A.getAllData()
# print(B)

# # Delete Data
# A = Dokter()
# nip = "1089"
# A.deleteByNIP(nip)
# B = A.getAllData()
# print(B)