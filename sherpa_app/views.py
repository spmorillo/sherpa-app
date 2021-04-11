import sqlite3
from flask import Flask, render_template, request, jsonify
from datetime import datetime
from pgeocode import Nominatim
from os.path import dirname, join, realpath
from . import app

PROJECT_ROOT = dirname(realpath(__file__))
DATABASE = join(PROJECT_ROOT, 'db', 'sherpa.db')

@app.route("/")
def home():
    return render_template("home.html")

@app.route('/user')
def user():
   return render_template('user.html')

@app.route('/adduser', methods=['POST', 'GET'])
def adduser():
    if request.method == 'POST':
        try:
            con = sqlite3.connect(DATABASE)
            cur = con.cursor()

            user = request.form['user']
            cp = request.form['cp']
            nomi = Nominatim('es')
            city = nomi.query_postal_code(cp)["place_name"] 
                
            cur.execute("INSERT INTO master (usuario) \
                VALUES (?)",(user,))
            cur.execute("INSERT INTO detalle (ciudad,cp,usuario) \
                VALUES (?,?,?)",(city, cp, user))
                
            con.commit()
            result = "Éxito"
            msg = "Usuario " + user + " introducido en la base de datos."
            code = 201

        except Exception as e:
            con.rollback()
            result = "Error"
            msg = str(e)
            code = 400
      
        finally:
            con.close()
            return jsonify(result=result, message=msg, code=code), code

@app.route("/list")
def list():
    con = sqlite3.connect(DATABASE)
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("SELECT * FROM detalle")
    rows = cur.fetchall()
    con.close()
    
    return render_template("list.html", rows=rows)

