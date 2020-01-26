import sqlite3
# uid, 서비스명, 평점(uid와 서비스명이 기본키)

uid = []
name = []
rate = []

database_filename = 'service.db'
#푸티랑 같은 디비인거 확인
conn = sqlite3.connect(database_filename)
conn.text_factory = str
cs = conn.cursor()


def makedb():
    query = "DROP TABLE IF EXISTS rating;"
    cs.execute(query)
    query = "CREATE TABLE rating (uid VARCHAR(40), name VARCHAR(255), rate integer, primary key(uid, name)); "
    cs.execute(query)

    
def insertdb():
    for i in range(len(uid)):
        query = "INSERT into rating (uid, name, rate) values (" \
                "?, ?, ?); "
        cs.execute(query, (uid[i], name[i], rate[i]))
    conn.commit()
    

def finishdb():
    cs.close()
    conn.close()

def jsontest():
    with io.open('/root/life.json', encoding='utf-8-sig') as json_file:
        json_data = json.load(json_file)
        for elem in json_data:
            uid.append(elem['name'])
            name.append(elem['servnm'])
            rate.append(elem['rate'])
            
            
if __name__ == '__main__':
    jsontest()
    makedb()
    insertdb()
    finishdb()
