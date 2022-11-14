import csv, sqlite3
from flask import Flask, flash, redirect, render_template, request, session, url_for
app = Flask(__name__)


conn = sqlite3.connect('users.sqlite', check_same_thread=False)
cu = conn.cursor()
cu.execute("CREATE TABLE IF NOT EXISTS users (id, name, gender, class, student number, mother number, father number, img, year, note)")

#cu.execute("SELECT * FROM users")
#print(cu.fetchall())
"""     
    cu.execute("SELECT * FROM users")
    print(cu.fetchall())
     """



@app.route("/")
def index():  
    users = conn.execute('SELECT * FROM users')
    return render_template("index.html", users=users)


@app.route("/popup")
def popup():  
    return render_template("popup.html")






if __name__ == "__main__":
    app.run(debug=True)