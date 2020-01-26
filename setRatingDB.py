import sqlite3
# uid, 서비스명, 평점(uid와 서비스명이 기본키)

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


def finishdb():
    cs.close()
    conn.close()


if __name__ == '__main__':
    makedb()
    finishdb()
