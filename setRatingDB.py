import sqlite3
# uid, 이름, 나이, 성별,지역, -불린 임신,출산,아동청소년, 청년, 중장년, 노년, 장애인, 한부모, 다문화, 저소득층, 보훈여부

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
