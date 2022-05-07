# """ SELECT """ #
import pymysql
con = pymysql.connect(host='localhost',port=3306,user='root',password='Admin@123',db='test')
cursor = con.cursor()
sql = 'select * from student;'
cursor.execute(sql)
print cursor.fetchall()
cursor.close()
con.close()


# """ INSERT """ #
import pymysql
con = pymysql.connect(host='localhost',port=3306,user='root',password='Admin@123',db='test')
cursor = con.cursor()
sql = 'insert into student(Name) values ("ArunThejaKumar");'
cursor.execute(sql)
con.commit()
print cursor.fetchall()
cursor.close()
con.close()


# """ DELETE """ #
import pymysql
con = pymysql.connect(host='localhost',port=3306,user='root',password='Admin@123',db='test')
cursor = con.cursor()
sql = 'delete from student where id = 9;'
cursor.execute(sql)
con.commit()
print cursor.fetchall()
cursor.close()
con.close()


# """ UPDATE """ #
import pymysql
con = pymysql.connect(host='localhost',port=3306,user='root',password='Admin@123',db='test')
cursor = con.cursor()
sql = 'update student set name = "Arun" where id = 13;'    # "missionimpossible" name replacing with "Arun" name 
cursor.execute(sql)
con.commit()
print cursor.fetchall()
cursor.close()
con.close()
