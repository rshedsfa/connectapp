import csv, sqlite3
from flask import Flask, flash, redirect, render_template, request, session, url_for
application = Flask(__name__)


conn = sqlite3.connect('data.db', check_same_thread=False)
cu = conn.cursor()




class_s = ['10-1','10-2','10-3','10-4','10-5',
    '11-1','11-2','11-3','11-4','11-5',
    '12-1','12-2','12-3','12-4','12-5']


@application.route('/', methods=['GET', 'POST'])
def index():  
    if request.method == "POST":
        searched_class=request.form.get('searched_class')
        cu.execute("SELECT * FROM users WHERE class_n LIKE (?)",[searched_class]) 
        users = cu.fetchall()
        return render_template("index.html", users=users,class_s=class_s, searched_class=searched_class)
    else:
        cu.execute('SELECT * FROM users')
        users = cu.fetchall()
        return render_template("index.html", users=users,class_s=class_s)


@application.route("/search")
def search():
    cu.execute("SELECT * FROM users WHERE username LIKE (?)",[ "%" + request.args.get("searched_word") + "%"]) 
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
        if not username or not class_n:
            return ("فضلاً التأكد من ملء جميع التفاصيل")
        if not student_n and not mother_n and not father_n:
            return ("فضلاً التأكد من ملء جميع التفاصيل")
            
        if len(username)<4:
            return ("فضلاً التأكد من ملء جميع التفاصيل")
        
        else:
            #cu.execute("INSERT INTO users(name, student_n) VALUES (?,?)", (username, student_n))
            cu.execute("INSERT INTO users(username, class_n, student_n, mother_n, father_n) VALUES (?,?,?,?,?)", (username, class_n, student_n, mother_n, father_n))
            conn.commit()
            
            cu.execute("SELECT * FROM users WHERE username LIKE (?)",(username,)) 
            users = cu.fetchall()
            return render_template("index.html", users=users)
            #return (index())
    else:
        return render_template("add.html", class_s=class_s)
    
    

@application.route('/+', methods=['GET', 'POST'])
def addSomeStudents():
    cu.execute("INSERT INTO users(username, class_n, student_n, mother_n, father_n) VALUES (?,?,?,?,?)", ("اركان محمد مواسي", "10-2", "0504834414", "0507733453", "0504834414"))
    cu.execute("INSERT INTO users(username, class_n, student_n, mother_n, father_n) VALUES (?,?,?,?,?)", ("عمر محمد غنايم", "10-2", "0504834414", "0507733453", "0504834414"))
    cu.execute("INSERT INTO users(username, class_n, student_n, mother_n, father_n) VALUES (?,?,?,?,?)", ("كرم احمد ابومخ", "10-2", "0504834414", "0507733453", "0504834414"))
    cu.execute("INSERT INTO users(username, class_n, student_n, mother_n, father_n) VALUES (?,?,?,?,?)", ("انس اسامة قعدان", "10-2", "0504834414", "0507733453", "0504834414"))
    cu.execute("INSERT INTO users(username, class_n, student_n, mother_n, father_n) VALUES (?,?,?,?,?)", ("عبد الله عبد الرحمن ابو بدر", "10-2", "0504834414", "0507733453", "0504834414"))
    cu.execute("INSERT INTO users(username, class_n, student_n, mother_n, father_n) VALUES (?,?,?,?,?)", ("يوسف محمد ابومخ", "10-3", "0504834414", "0507733453", "0504834414"))
    cu.execute("INSERT INTO users(username, class_n, student_n, mother_n, father_n) VALUES (?,?,?,?,?)", ("اسامة رامي بيادسة", "10-3", "0504834414", "0507733453", "0504834414"))
    cu.execute("INSERT INTO users(username, class_n, student_n, mother_n, father_n) VALUES (?,?,?,?,?)", ("انس محمد عويسات", "11-2", "0504834414", "0507733453", "0504834414"))
    cu.execute("INSERT INTO users(username, class_n, student_n, mother_n, father_n) VALUES (?,?,?,?,?)", ("جهاد عمر عنبوسي", "11-2", "0504834414", "0507733453", "0504834414"))
    conn.commit()
    return (index())   
    
    
    
@application.route('/delete/<id>')
def delete(id):
    cu.execute("DELETE FROM users WHERE user_id LIKE (?)", (id,))       # (,) extra comm is needed. 
    conn.commit()
    return (index())   
    

@application.route('/t')
def tttt():
    #x=request.form.get('qwe45')
    #x=request.args.get('qwe45')
    x= 5
    x = str(x)                  #withouw str will not work
    return x



@application.route('/UPDATE/<id>', methods=['GET', 'POST'])
def UPDATE(id):
    if request.method == "POST":
        username=request.form.get(f'username{id}')
        class_n=request.form.get(f'class_n{id}')
        student_n=request.form.get(f'student_n{id}')
        mother_n=request.form.get(f'mother_n{id}')
        father_n=request.form.get(f'father_n{id}')
        print(username)
        print(class_n)
        print(student_n)
        print(mother_n)
        print(father_n)
        if not username or not class_n:
            return ("فضلاً التأكد من ملء جميع التفاصيل")
        if not student_n and not mother_n and not father_n:
            return ("فضلاً التأكد من ملء جميع التفاصيل")
            
        if len(username)<4:
            return ("فضلاً التأكد من ملء جميع التفاصيل")
        
        else:
            cu.execute("UPDATE users SET username =(?), class_n =(?), student_n =(?), mother_n =(?), father_n =(?) WHERE user_id LIKE (?)", (username, class_n, student_n, mother_n, father_n, id,)) 
            conn.commit()
            cu.execute('SELECT * FROM users')
            users = cu.fetchall()
            return render_template("index.html", users=users,class_s=class_s)
            
            # return index()
            
            # cu.execute('SELECT * FROM users')
            # users = cu.fetchall()
            # return render_template("index.html", users=users)
            # return (index())
    else:
        return render_template("add.html", class_s=class_s)
    











@application.route('/test/<id>')
def test(id):
    
    class_n=request.form.get('class_n')
    student_n=request.form.get('student_n')
    mother_n=request.form.get('mother_n')
    father_n=request.form.get('father_n')
    
    #cu.execute("UPDATE users SET username ='*****' WHERE user_id LIKE (?)", (id,)) 
    cu.execute("UPDATE users SET username =(?) WHERE user_id LIKE (?)", (id,)) 
    conn.commit()
    cu.execute('SELECT * FROM users')
    return (index()) 



 
 
 
 
 


if __name__ == "__main__":
    application.run(debug=True)


""" 
git add .
git commit -m 'any text'
git push origin main

 """
 