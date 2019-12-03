import sqlite3
import json
import io


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
conn.text_factory = str
cs = conn.cursor()


def makedb():
    query = "DROP TABLE IF EXISTS service;"
    cs.execute(query)
    query = "CREATE TABLE service (id integer primary key autoincrement, cate_top VARCHAR(20), cate_mid VARCHAR(20), " \
            "cate_low VARCHAR(20), name VARCHAR(255), brief VARCHAR(1000), target VARCHAR(255), content VARCHAR(1000), " \
            "url VARCHAR(255), patriot VARCHAR(20)); "
    cs.execute(query)


def insertdb():
    for i in range(len(toparr)):
        query = "INSERT into service (cate_top, cate_mid, cate_low, name, brief, target, content, url, patriot) values (" \
                "?, ?, ?, ?, ?, ?, ?, ?, ?); "
        cs.execute(query, (toparr[i], midarr[i], lowarr[i], name[i], brief[i], target[i], contents[i], urls[i], patriot[i]))
    conn.commit()


def selectdb():
    query = "SELECT * FROM service;"
    cs.execute(query)
    all_rows = cs.fetchall()
    for i in all_rows:
        print(i)
    print('select done')


def jsontest():
    with io.open('/root/servicelist.json', encoding='utf-8-sig') as json_file:
        json_data = json.load(json_file)
        for elem in json_data:
            toparr.append(elem['cate_top'])
            midarr.append(elem['cate_mid'])
            lowarr.append(elem['cate_low'])
            name.append(elem['serv_name'])
            brief.append(elem['serv_brief'])
            target.append(elem['target'])
            contents.append(elem['contents'])
            urls.append(elem['url'])
            patriot.append(elem['is_patriot'])



def finishdb():
    cs.close()
    conn.close()


if __name__ == '__main__':
    jsontest()
    makedb()
    insertdb()
    selectdb()
    finishdb()

