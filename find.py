from flask import Flask, request, jsonify, Response
import sqlite3
import json
import pandas as pd
import scipy as sp
import numpy as np
import surprise
from surprise.model_selection import cross_validate
import warnings
warnings.filterwarnings('ignore')

app = Flask(__name__)
app.config['JSON_AS_ASCII']=False
database_filename = 'service.db'
conn = sqlite3.connect(database_filename, check_same_thread=False)

name_list = []  # 서비스명
cos_set = set()  # 서비스 id
cos_list = list(cos_set)
option = {'name': 'pearson', 'shrinkage': 90}
algo = surprise.KNNBasic(sim_options=option)
data = pd.read_csv('life.csv', engine='python')

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
    pwd = request.args.get('pwd')
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

    if uid and pwd and name and age and gender and loc and freg and baby and kid and chung and jung and no and handi and hanbumo and damunhwa and lowsodek and bohun:
        cs = conn.cursor()
        query = "INSERT into user (uid, pwd, name, age, gender, loc, freg, baby, kid, chung, jung, no, handi, hanbumo, " \
            "damunhwa, lowsodek, bohun) values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?); "
        cs.execute(query, (uid, pwd, name, age, gender, loc, freg, baby, kid, chung, jung, no, handi, hanbumo, damunhwa, lowsodek, bohun))
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
    return Response(json.dumps({'result': [str(row) for row in rows]},
               ensure_ascii=False), mimetype='application/json; charset=utf-8')


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


@app.route("/findbenefit")
def findbenefit():
    ageint = request.args.get('ageint')
    jang = request.args.get('jang')
    bo = request.args.get('bo')
    cs = conn.cursor()
    query = "SELECT * FROM service INNER JOIN benefit ON service.name = benefit.name WHERE ageint = ? AND jang = ? AND bo = ?;"
    cs.execute(query, (ageint, jang, bo))
    rows = cs.fetchall()
    return Response(json.dumps({'result': [str(row) for row in rows]},
               ensure_ascii=False), mimetype='application/json; charset=utf-8')


#추천돌리기전에 json받는거
@app.route("/putjson", methods=['GET','POST'])
def putjson():
    if request.method == 'POST':
        uid = []
        name = []
        rate = []
        request.on_json_loading_failed = on_json_loading_failed_return_dict
    #json받아서 DB에 넣기
        data = request.get_json()
        for elem in data:
            uid.append(elem['name'])
            name.append(elem['servnm'])
            rate.append(elem['rate'])

    cs = conn.cursor()

    #추가할지변경할지
    for i in range(len(uid)):
        query = "INSERT INTO rating (uid, name, rate) VALUES (?,?,?) ON DUPLICATE KEY UPDATE rate = ?;"
        cs.execute(query, (uid[i], name[i], rate[i], rate[i]))

    conn.commit()

    getcsv()
    learning()


#빈값방지
def on_json_loading_failed_return_dict(e):
    return {}


#디비에서 csv만들기
def getcsv():
    cs = conn.cursor()
    query = "SELECT * FROM rating;"
    data = cs.execute(query)
    with open('output.csv', 'wb') as f:
        writer = csv.writer(f)
        writer.writerow(['name', 'age', 'servnm', 'rate'])
        writer.writerows(data)


# 딕셔너리 생성
def recur_dictify(frame):
    if len(frame.columns) == 1:
        if frame.values.size == 1:
            return frame.values[0][0]
        return frame.values.squeeze()
    grouped = frame.groupby(frame.columns[0])
    d = {k: recur_dictify(g.ix[:, 1:]) for k, g in grouped}
    return d


def learning():
    global data, algo, name_list, cos_set, cos_list, option
    data = pd.read_csv('output.csv', engine='python')
    df = data[['name', 'servnm', 'rate']]
    df_to_dict = recur_dictify(df)

    for user_key in df_to_dict:
        name_list.append(user_key)

        for cos_key in df_to_dict[user_key]:
            cos_set.add(cos_key)

    cos_list = list(cos_set)
    rating_dic = {
        'name': [],
        'servnm': [],
        'rate': []
    }

    for name_key in df_to_dict:
        for cos_key in df_to_dict[name_key]:
            a1 = name_list.index(name_key)
            a2 = cos_list.index(cos_key)
            a3 = df_to_dict[name_key][cos_key]

            rating_dic['name'].append(a1)
            rating_dic['servnm'].append(a2)
            rating_dic['rate'].append(a3)

    df = pd.DataFrame(rating_dic)

    reader = surprise.Reader(rating_scale=(1, 5))  # 평점 범위 : 1~5
    col_list = ['name', 'servnm', 'rate']
    data = surprise.Dataset.load_from_df(df[col_list], reader)

    trainset = data.build_full_trainset()
    # option = {'name': 'pearson', 'shrinkage': 90}
    # algo = surprise.KNNBasic(sim_options=option)

    # cross_validate(algo, data)["test_mae"].mean()

    algo.fit(trainset)


@app.route("/getrecommend")
def getrecommend():
    global data, algo, name_list, cos_set, cos_list, option

    # 서비스 추천받기
    who = request.args.get('uid')
    result_list = []
    count = 0

    index = name_list.index(who)

    result = algo.get_neighbors(index, k=3)

    #servid는 서비스명 담고있음
    for r1 in result:
        max_rating = data.df[data.df["name"] == r1]["rate"].max()
        serv_id = data.df[((data.df["rate"] == max_rating) | (data.df["rate"] == max_rating - 1)) & (data.df["name"] == r1)][
            "servnm"].values

        for serv_item in serv_id:
            if (len(result_list)) > 0:
                for i in range(len(result_list)):
                    if cos_list[serv_item] == result_list[i]:
                        count = count + 1
                if count == 0:
                    result_list.append(cos_list[serv_item])
                count = 0

            elif (len(result_list)) == 0:
                result_list.append(cos_list[serv_item])

    #print(result_list)
    return Response(json.dumps({'result': [str(row) for row in result_list]},
                        ensure_ascii=False), mimetype='application/json; charset=utf-8')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    app.debug = False
