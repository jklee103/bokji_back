from flask import Flask, request, jsonify, Response
import sqlite3
import json

app = Flask(__name__)
app.config['JSON_AS_ASCII']=False
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
    return Response(json.dumps({'result': [str(row) for row in rows]},
               ensure_ascii=False), mimetype='application/json; charset=utf-8')


# 되는대로 만든거임
@app.route("/findall")
def findall():
    cs = conn.cursor()
    query = "SELECT * FROM service;"
    cs.execute(query)
    rows = cs.fetchall()
    return Response(json.dumps({'result': [str(row) for row in rows]},
               ensure_ascii=False), mimetype='application/json; charset=utf-8')


@app.route("/signin")
def signin():
    uid = request.args.get('uid')
    cs = conn.cursor()
    query = "SELECT * FROM user WHERE uid = ?;"
    cs.execute(query, (uid,))
    rows = cs.fetchall()
    return jsonify(rows)


@app.route("/signup")
def signup():
    uid = request.args.get('uid')
    name = request.args.get('name')
    age = request.args.get('age')
    gender = request.args.get('gender')
    loc = request.args.get('loc')
    freg = request.args.get('freg')
    baby = request.args.get('baby')
    kid = request.args.get('kid')
    chung = request.args.get('chung')
    jung = request.args.get('jung')
    no = request.args.get('no')
    handi = request.args.get('handi')
    hanbumo = request.args.get('hanbumo')
    damunhwa = request.args.get('damunhwa')
    lowsodek = request.args.get('lowsodek')

    if uid and name and age and gender and loc and freg and baby and kid and chung and jung and no and handi and hanbumo and damunhwa and lowsodek:
        cs = conn.cursor()
        query = "INSERT into user (uid, name, age, gender, loc, freg, baby, kid, chung, jung, no, handi, hanbumo, " \
            "damunhwa, lowsodek) values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?); "
        cs.execute(query, (uid, name, age, gender, loc, freg, baby, kid, chung, jung, no, handi, hanbumo, damunhwa, lowsodek))
        conn.commit()
        return jsonify({'msg' : '회원가입 완료'}), 200
    else:
        return jsonify({'err' : '입력값 부족'}),404


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    app.debug = False
