import csv, sqlite3
from flask import Flask, flash, redirect, render_template, request, session, url_for
application = Flask(__name__)


conn = sqlite3.connect('data.db', check_same_thread=False)
cu = conn.cursor()

class_s = ['10-1','10-2','10-3','10-4','10-5','',
    '11-1','11-2','11-3','11-4','11-5','',
    '12-1','12-2','12-3','12-4','12-5']

@application.route('/', methods=['GET', 'POST'])
def index():  

    if request.method == "POST":
        searched_class=request.form.get('searched_class')
        cu.execute("SELECT * FROM users WHERE class LIKE (?)",[searched_class]) 
        users = cu.fetchall()
        return render_template("index.html", users=users,class_s=class_s, searched_class=searched_class)
    else:
        cu.execute('SELECT * FROM users')
        users = cu.fetchall()
        return render_template("index.html", users=users,class_s=class_s)


@application.route("/search")
def search():

    cu.execute("SELECT * FROM users WHERE name LIKE (?)",[ "%" + request.args.get("searched_word") + "%"]) 
    users = cu.fetchall()
    if users:
        return render_template("index.html", users=users,class_s=class_s)
    else:
        cu.execute('SELECT * FROM users')
        users = cu.fetchall()
        not_found = 1
        return render_template("index.html", users=users,class_s=class_s, not_found=not_found)



@application.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == "POST":
        username=request.form.get('username')
        class_n=request.form.get('class_n')
        student_n=request.form.get('student_n')
        mother_n=request.form.get('mother_n')
        father_n=request.form.get('father_n')
        note=request.form.get('note')
        
        if not username or not class_n:
            return ("فضلاً التأكد من ملء جميع التفاصيل")
        if not student_n and not mother_n and not father_n:
            return ("فضلاً التأكد من ملء جميع التفاصيل")
            
        if len(username)<4:
            return ("فضلاً التأكد من ملء جميع التفاصيل")
        
        else:
            #cu.execute("INSERT INTO users(name, student_n) VALUES (?,?)", (username, student_n))
            cu.execute("INSERT INTO users(name, class, student_n, mother_n, father_n, note) VALUES (?,?,?,?,?,?)", (username, class_n, student_n, mother_n, father_n, note))
            conn.commit()
            
            cu.execute("SELECT * FROM users WHERE name LIKE (?)",(username,)) 
            users = cu.fetchall()
            return render_template("index.html", users=users)
            #return (index())
    else:

        return render_template("add.html", class_s=class_s)
    
    
    

@application.route("/test")
def test():
    cu.execute('SELECT * FROM users')
    users = cu.fetchall()
    return render_template("test.html", users=users)

@application.route("/sql")
def sql():
    cu.execute("UPDATE users SET note ='ملاحظة عن الطالب عمر' WHERE name ='omar'") 
    conn.commit()
    cu.execute('SELECT * FROM users')
    users = cu.fetchall()
    return render_template("index.html", users=users)

@application.route("/sqlomar")
def sqlomar():
    cu.execute("UPDATE users SET name ='عمر محمد ابومخ' WHERE name ='omar'") 
    conn.commit()
    cu.execute('SELECT * FROM users')
    users = cu.fetchall()
    return render_template("index.html", users=users)

@application.route("/rrr")
def rrr():
    cu.execute("DELETE FROM users WHERE mother_n='' ") 
    conn.commit()
    return (index())

 
 
 
 
 
 


if __name__ == "__main__":
    application.run(debug=True)


""" 
git add .
git commit -m 'any text'
git push origin main

 """
 
 
 
 










