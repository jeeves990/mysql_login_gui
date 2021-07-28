

import pymysql
# db = pymysql.connect(host="localhost",user="root",password="j33ves99",database="event_calendar", port = 3305)
db = pymysql.connect(\
    user = "sherril",\
    password = "j33ves99",\
    host = "localhost",\
    database = "event_calendar")
if db:
    print('success')
else:
    print('not success')


# db = pymysql.connect(\
#     user = "sherril",\
#     password = "j33ves99",\
#     host = "mean-machine",\
#     database = "wordscape")

