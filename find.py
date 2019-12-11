from flask import Flask, request
import sqlite3
import json

app = Flask(__name__)
database_filename = 'service.db'
conn = sqlite3.connect(database_filename, check_same_thread=False)


@app.route('/')
def index():
    return 'hello'


# 되는대로 만든거임
@app.route("/find")
def find():
    cate_mid = request.args.get('catemid')
    cate_low = request.args.get('catelow')
    cs = conn.cursor()
    query = "SELECT * FROM service WHERE cate_mid = ? AND cate_low = ?;"
    cs.execute(query, (cate_mid, cate_low))
    rows = cs.fetchall()
    for i in rows:
        print(i)
    return str(rows)


# 되는대로 만든거임
@app.route("/findall")
def findall():
    cs = conn.cursor()
    query = "SELECT * FROM service;"
    cs.execute(query)
    rows = cs.fetchall()
    for i in rows:
        print(i)
    return str(rows)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    app.debug = True
