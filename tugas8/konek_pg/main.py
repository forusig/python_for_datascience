import conn as cf

koneksi = cf.connection_pgadmin()
cursor = koneksi.cursor()

cursor.execute("select * from show where release_year = 2016 and country = 'US' and genre = 'Comedy'")
dataset = cursor.fetchall()

for data in dataset:
    print(data)

cursor.close()