import psycopg2

#配置したDBよって変更
host = "localhost"
port = "5432"
dbname = "aicreation2"
user = "postgres"
password = "taiki0831"

conn = psycopg2.connect(\
    "host=" + host + \
    " port=" + port + \
    " dbname=" + dbname + \
    " user=" + user + \
    " password=" + password\
        )

cur = conn.cursor()
cur.execute('SELECT theater_spot FROM theater_table')
spots = cur.fetchall()
spots_list = []
for i in spots:
    spots_list.append(i[0])

#検索したい時空間要件を入力
print("---------------------------------------------")
when = input("[予約したい月を入力(半角数字で入力)]：")
while True:
    print("\n~~検索可能地点~~")
    for i in spots:
        print("・" + i[0])
    print("~~~~~~~~~~~~~~~~")
    where = input("[最寄りの駅を選択]：")
    if where in spots_list:
        break
print("---------------------------------------------")
print("[" + when + "月", where, "で検索]")

cur.execute("SELECT movie_title, name_theater, month_playing, theater_spot \
    FROM movie_table,theater_table WHERE \
    movie_table.theater_id = theater_table.theater_id AND \
    movie_table.month_playing =" + when + \
    "AND theater_table.theater_spot = '" + where +"'")
book_able = cur.fetchall()
if not book_able:
    print("\n予約可能な映画は有りません\n")
else:
    dict_info = {}
    count = 1
    for i in book_able:
        print("\n"+str(count) + ". [タイトル]:" + i[0], \
            "[映画館]:" + i[1], "[上映月]:" + str(i[2]) + "月", \
            "[上映場所]:" + i[3])
        dict_info[str(count)] = i
        count += 1
    
    which_movie = input("\n[予約したい映画を選択(半角数字で入力)]：")
    reserved_movie = dict_info[which_movie]
    print("---------------------------------------------")

    cur.execute("INSERT INTO reserved_table\
        (movie_title,name_theater,month_playing,theater_spot)\
        VALUES ('" + reserved_movie[0] + "','" + reserved_movie[1] + "','" + \
            str(reserved_movie[2]) + "','" + reserved_movie[3] + "')")
    cur.execute("SELECT * FROM reserved_table")
    reserved_list = cur.fetchall()
    print("[予約済み映画]")
    count = 1
    for i in reserved_list:
        print(str(count) + ". [タイトル]:" + i[0], \
            "[映画館]:" + i[1], "[上映月]:" + str(i[2]) + "月", \
            "[上映場所]:" + i[3])
        count += 1
    print("---------------------------------------------")

cur.close()
conn.commit()
conn.close()