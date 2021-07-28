import pymysql
import sys

# db = pymysql.connect("your hostname","your username","your password","your database" )
# db = pymysql.connect(\
#     user = "sherril",\
#     # user = "remote_user",\
#     password = "j33ves99",\
#     # host = "localhost",\
#     host = "s-notebook",\
#     database = "wordscape",\
#     port=3305)

connection_string = 'database="wordscape", host="s_notebook", port=3305, user="sherril", password="j33ves99"'
# db = pymysql.connect(connection_string)
db = pymysql.connect(\
    user="sherril", \
    # user = "remote_user",\
    password="j33ves99", \
    host = "s-notebook",\
    database = "wordscape", \
    port=3305)


# db = pymysql.connect(\
#     user = "sherril",\
#     password = "j33ves99",\
#     host = "mean-machine",\
#     database = "wordscape")

# db = pymysql.connect( \
#     user="ardit700_student", \
#     password="ardit700_student", \
#     host="108.167.140.122", \
#     database="ardit700_pm1database")

print(db)
# sys.exit(0)

print('hello hello goodbye goodbye')
crsr = db.cursor()
try:
    while True:

        userIn = input("enter a word: ")
        if userIn == '_quit_':
            sys.exit(0)

        sql = f"select * from words WHERE word like '%%{userIn}%%' "
        # sql = format("select * from words WHERE word like '%s%%' " % userIn)
        # sql = format("select * from Dictionary WHERE Expression like '%s%%' " % userIn)
        # sql = format("SELECT * FROM Dictionary WHERE Expression like 'rain%'")
        # print(sql)

        qry = crsr.execute(sql)
        result = crsr.fetchall()
        iter = 0
        for word in result:
            print(word)
            iter += 1
        # _qry = crsr.execute("SHOW TABLES")
        # print(_qry)
        print(f'there were {iter} words returned.')

finally:
    db.close()

exit()
    
while True:
    time.sleep(1)
    if msvcrt.kbhit():
        # Only if there's a keypress waiting do we get it with getch()
        char = msvcrt.getch()
        print( "Key hit! ({})".format(char))
        if hex(char) == hex(27):
            break
    else:
        # Do something else here
        print("Nothing...")
     
     