import pymysql as sq

db = sq.connect("localhost","nomad","nomad","CSE")
cursor = db.cursor()
try:
    sql = "select * from R1"
    cursor.execute(sql)
    res = cursor.fetchall()
    for row in res:
        id = row[0]
        time = row[1]
        mon = row[2]
        print(str(id)+time+mon,sep=" ")
except Exception as e:
    print("err"+e)