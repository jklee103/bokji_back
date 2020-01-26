import sqlite3
import json
import io

#대분류, 중분류, 서비스명, 요약, 조회수 컬럼이 있는 DB생성코드
toparr = []
midarr = []
name = []
brief = []
inqnum = []

database_filename = 'service.db'
conn = sqlite3.connect(database_filename)
conn.text_factory = str
cs = conn.cursor()


def makedb():
    query = "DROP TABLE IF EXISTS inq;"
    cs.execute(query)
    query = "CREATE TABLE inq (id integer primary key autoincrement, cate_top VARCHAR(20), cate_mid VARCHAR(20), " \
            "name VARCHAR(255), brief VARCHAR(1000), inqnum integer); "
    cs.execute(query)


def insertdb():
    for i in range(len(toparr)):
        query = "INSERT into inq (cate_top, cate_mid, name, brief, inqnum) values (" \
                "?, ?, ?, ?, ?); "
        cs.execute(query, (toparr[i], midarr[i], name[i], brief[i], inqnum[i]))
    conn.commit()


def selectdb():
    query = "SELECT * FROM inq;"
    cs.execute(query)
    all_rows = cs.fetchall()
    for i in all_rows:
        print(i)
    print('select done')


def jsontest():
    with io.open('/root/servlist_cb.json', encoding='utf-8-sig') as json_file:
        json_data = json.load(json_file)
        for elem in json_data:
            toparr.append(elem['cate_top'])
            midarr.append(elem['cate_mid'])
            name.append(elem['serv_name'])
            brief.append(elem['serv_brief'])
            inqnum.append(elem['inqNum'])


def finishdb():
    cs.close()
    conn.close()


if __name__ == '__main__':
    jsontest()
    makedb()
    insertdb()
    finishdb()
