import os
from Include.DBConnection import DbConnection
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/home')
def get_from_db():
    dbconn = DbConnection()
    dbconn.enable_connection()
    return render_template("homepage.html", records=dbconn.records)


app.run(debug=True, port="8000", host="0.0.0.0")
