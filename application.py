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


@application.route("/add")
def add():
    return render_template("add.html")



if __name__ == "__main__":
    application.run(debug=True)



""" 
git add .
git commit -m 'any text'
git push origin main

 """