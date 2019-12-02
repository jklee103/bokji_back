import sqlite3
import json

toparr = []
midarr = []
lowarr = []
name = []
brief = []
target = []
contents = []
urls = []
patriot = []

database_filename = 'service.db'
conn = sqlite3.connect(database_filename)
cs = conn.cursor()


# 처음에 테이블만들기
def makedb():
    query = "DROP TABLE IF EXISTS service;"
    cs.execute(query)
    query = "CREATE TABLE service (id integer primary key autoincrement, cate_top VARCHAR(20), cate_mid VARCHAR(20), " \
            "cate_low VARCHAR(20), name VARCHAR(255), brief VARCHAR(1000), target VARCHAR(255), content VARCHAR(1000), " \
            "url VARCHAR(255), patriot VARCHAR(20)); "
    cs.execute(query)


# 배열에 있는 데이터 디비에 집어넣기
def insertdb():
    for i in range(len(toparr)):
        query = "INSERT into service (cate_top, cate_mid, cate_low, name, brief, target, content, url, patriot) values (" \
                "?, ?, ?, ?, ?, ?, ?, ?, ?); "
        cs.execute(query, (toparr[i], midarr[i], lowarr[i], name[i], brief[i], target[i], contents[i], urls[i], patriot[i]))
    conn.commit()


# 잘들갔는지 테스트
def selectdb():
    query = "SELECT * FROM service;"
    cs.execute(query)
    all_rows = cs.fetchall()
    for i in all_rows:
        print(i)
    print('select done')


# 크롤링한 데이터 배열에 넣기
def jsontest():
    with open('\\servicelist.json', encoding='utf-8-sig') as json_file:
        json_data = json.load(json_file)
        for i in json_data:
            toparr.append(str(i['cate_top']))
            midarr.append(str(i['cate_mid']))
            lowarr.append(str(i['cate_low']))
            name.append(str(i['serv_name']))
            brief.append(str(i['serv_brief']))
            target.append(str(i['target']))
            contents.append(str(i['contents']))
            urls.append(str(i['url']))
            patriot.append(str(i['is_patriot']))
            # 일단 불린도 스트링으로 받음(sqlite에 불린이 없대)


def finishdb():
    cs.close()
    conn.close()


if __name__ == '__main__':
    jsontest()
    makedb()
    insertdb()
    selectdb()
    finishdb()

