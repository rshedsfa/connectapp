import csv, sqlite3
from flask import Flask, flash, redirect, render_template, request, session, url_for
application = Flask(__name__)


conn = sqlite3.connect('data.db', check_same_thread=False)
cu = conn.cursor()



@application.route("/")
def index():  
    cu.execute('SELECT * FROM users')
    users = cu.fetchall()
    return render_template("index.html", users=users)



@application.route("/search")
def search():
    cu.execute("SELECT * FROM users WHERE name LIKE (?)",[ "%" + request.args.get("searched_word") + "%"]) 
    users = cu.fetchall()
    if users:
        return render_template("index.html", users=users)
    else:
        cu.execute('SELECT * FROM users')
        users = cu.fetchall()
        not_found = 1
        return render_template("index.html", users=users, not_found=not_found)



@application.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == "POST":
        if not request.form.get('username'):
            return ("fill all the fields")
        else:
            username=request.form.get('username')
            student_n=request.form.get('student_n')
            #cu.execute("INSERT INTO users(name, student_n) VALUES (?,?)", (username, student_n))
            cu.execute("INSERT INTO users(name, student_n) VALUES (?,?)", (request.form.get('username'), request.form.get('student_n')))
            conn.commit()
            
            cu.execute("SELECT * FROM users WHERE name LIKE (?)",(username,)) 
            users = cu.fetchall()
            return render_template("index.html", users=users)
            #return (index())
    else:
        return render_template("add.html")
    
    
    

@application.route("/test")
def test():
    cu.execute('SELECT * FROM users')
    users = cu.fetchall()
    return render_template("test.html", users=users)

@application.route("/sql")
def sql():
    cu.execute("UPDATE users SET note ='ملاحظة عن الطالب عمر' WHERE name ='omar'") #############
    cu.execute('SELECT * FROM users')
    users = cu.fetchall()
    return render_template("index.html", users=users)

@application.route("/sqlomar")
def sqlomar():
    cu.execute("UPDATE users SET name ='عمر محمد ابومخ' WHERE name ='omar'") #############
    cu.execute('SELECT * FROM users')
    users = cu.fetchall()
    return render_template("index.html", users=users)




if __name__ == "__main__":
    application.run(debug=True)


""" 
git add .
git commit -m 'any text'
git push origin main

 """
 
 
 
 










