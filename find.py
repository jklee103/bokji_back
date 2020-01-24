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


@app.route("/findbyname")
def findbyname():
    name = request.args.get('name')
    cs = conn.cursor()
    query = "SELECT * FROM service WHERE name = ? ORDER BY ROWID ASC LIMIT 1;"
    cs.execute(query, (name,))
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
    bohun = request.args.get('bohun')

    if uid and name and age and gender and loc and freg and baby and kid and chung and jung and no and handi and hanbumo and damunhwa and lowsodek and bohun:
        cs = conn.cursor()
        query = "INSERT into user (uid, name, age, gender, loc, freg, baby, kid, chung, jung, no, handi, hanbumo, " \
            "damunhwa, lowsodek, bohun) values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?); "
        cs.execute(query, (uid, name, age, gender, loc, freg, baby, kid, chung, jung, no, handi, hanbumo, damunhwa, lowsodek, bohun))
        conn.commit()
        return jsonify({'msg' : '회원가입 완료'}), 200
    else:
        return jsonify({'err' : '입력값 부족'}),404


@app.route("/modusr")
def modusr():
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
    bohun = request.args.get('bohun')

    if uid and name and age and gender and loc and freg and baby and kid and chung and jung and no and handi and hanbumo and damunhwa and lowsodek and bohun:
        cs = conn.cursor()
        query = "UPDATE user SET name = ?, age = ?, gender = ?, loc = ?, freg = ?, baby = ?, kid = ?, chung = ?, jung = ?, no = ?, handi = ?, hanbumo = ?, " \
            "damunhwa = ?, lowsodek = ?, bohun = ? WHERE uid = ?; "
        cs.execute(query, (name, age, gender, loc, freg, baby, kid, chung, jung, no, handi, hanbumo, damunhwa, lowsodek, bohun, uid))
        conn.commit()
        return jsonify({'msg' : '수정 완료'}), 200
    else:
        return jsonify({'err' : '입력값 부족'}),404


@app.route("/getnoxml")
def getnoxml():
    filedir="/root/xmls/no.xml"
    xml = open(filedir, 'r')
    data = xml.read()
    return Response(data, mimetype='text/xml')


@app.route("/getbabyxml")
def getbabyxml():
    filedir="/root/xmls/baby.xml"
    xml = open(filedir, 'r')
    data = xml.read()
    return Response(data, mimetype='text/xml')


@app.route("/getchungxml")
def getchungxml():
    filedir="/root/xmls/chung.xml"
    xml = open(filedir, 'r')
    data = xml.read()
    return Response(data, mimetype='text/xml')


@app.route("/getjungxml")
def getjungxml():
    filedir="/root/xmls/jung.xml"
    xml = open(filedir, 'r')
    data = xml.read()
    return Response(data, mimetype='text/xml')


@app.route("/getkidxml")
def getkidxml():
    filedir="/root/xmls/kid.xml"
    xml = open(filedir, 'r')
    data = xml.read()
    return Response(data, mimetype='text/xml')


@app.route("/getpregxml")
def getpregxml():
    filedir="/root/xmls/preg.xml"
    xml = open(filedir, 'r')
    data = xml.read()
    return Response(data, mimetype='text/xml')


@app.route("/findinq")
def findinq():
    cate_mid = request.args.get('catemid')
    cs = conn.cursor()
    query = "SELECT * FROM inq WHERE cate_mid = ? ORDER BY inqnum DESC;"
    cs.execute(query, (cate_mid,))
    rows = cs.fetchall()
    return jsonify({'result': [jsonify(row) for row in rows]}), 200


@app.route("/addrating")
def addrating():
    cate_mid = request.args.get('')
    cs = conn.cursor()
    query = "UPDATE rating SET "  
    #add on duplicate to query
    cs.execute(query, (uid, name, rate))
    rows = cs.fetchall()
    return Response(json.dumps({'result': [str(row) for row in rows]},
               ensure_ascii=False), mimetype='application/json; charset=utf-8')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    app.debug = False
