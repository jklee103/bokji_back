import sqlite3
import json
import io


id = []
name = []
benefit = []

database_filename = 'service.db'
conn = sqlite3.connect(database_filename)
conn.text_factory = str
cs = conn.cursor()

age = 1
jang = 0
bo = 0

#영유아-1 아동-2 청소년-3 청년-4 중장년-5 노인-6
def makedb():
    query = "DROP TABLE IF EXISTS benefit;"
    cs.execute(query)
    query = "CREATE TABLE benefit (id VARCHAR(20), name VARCHAR(255), benefit integer, ageint integer, " \
            "jang integer, bo integer, primary key(ageint, jang, bo)); "
    cs.execute(query)


def insertdb():
    for i in range(len(id)):
        query = "INSERT into benefit (id, name, benefit, ageint, jang, bo) values (" \
                "?, ?, ?, ?, ?, ?); "
        cs.execute(query, (id[i], name[i], benefit[i], age, jang, bo))
    conn.commit()


def selectdb():
    query = "SELECT * FROM benefit;"
    cs.execute(query)
    all_rows = cs.fetchall()
    for i in all_rows:
        print(i)
    print('select done')


def jsontest():
    with io.open('/root/no_bo.json', encoding='utf-8-sig') as json_file:
        json_data = json.load(json_file)
        for elem in json_data:
            id.append(elem['servid'])
            name.append(elem['servnm'])
            benefit.append(elem['benefit'])


def finishdb():
    cs.close()
    conn.close()


if __name__ == '__main__':
    jsontest()
    makedb()
    insertdb()
    finishdb()
