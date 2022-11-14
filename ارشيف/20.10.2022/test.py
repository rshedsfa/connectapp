import sqlite3

#Connect to database
conn = sqlite3.connect('test.db')

#Create a cursor
cu = conn.cursor()


#CreateaTable
cu.execute("CREATE TABLE IF NOT EXISTS customers(first_name text,last_name text,email text)")


# insert one row 
cu.execute("INSERT INTO customers VALUES('John','Elder','john@codemy.com')")

# insert mult row
customers =[
            ('Wes','Brown','wes@brown.com'),
            ('Steph','Kuewa','steph@kuewa.com'),
            ('Dan',"Pas",'dan@pas.com'),
            ]
cu.executemany("INSERT INTO customers VALUES(?,?,?)",customers)


# show data
cu.execute("SELECT * FROM customers")
print(cu.fetchall())        # print all data as list in one line

items = cu.fetchall()
""" for item in items:          
    #print(item)            		#print cpecific column
    #print(item[0])     		    #print cpecific column
    print(item[0]+ "\t|\t" + item[1]+ "\t|\t" + item[2]) """



# save database
conn.commit()

#close connection
conn.close()