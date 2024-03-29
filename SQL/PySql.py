"""
Basic SQL Function Using Python with Sqlite
"""
import sqlite3
import datetime
import time
import random
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from dateutil import parser
from matplotlib import style
style.use('fivethirtyeight')

conn = sqlite3.connect('tutorial.db')
c = conn.cursor()

def create_table():
    c.execute("CREATE TABLE IF NOT EXISTS stuffToPlot(unix REAL, datestamp TEXT, keyword TEXT, value REAL)")

"""
def data_entry():
    c.execute("INSERT INTO stuffToPlot VALUES(1452549219,'2016-01-11 13:53:39','Akhil',6)")
    conn.commit()
    c.close()
    conn.close()
"""

create_table()
##
##def dynamic_data_entry():
##    unix = int(time.time())
##    date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))
##    keyword = 'Python'
##    value = random.randrange(0,10)
##
##    c.execute("INSERT INTO stuffToPlot (unix, datestamp, keyword, value) VALUES (?, ?, ?, ?)",(unix, date, keyword, value))
##    conn.commit()
##
##    
##for i in range(10):
##    dynamic_data_entry()
##    time.sleep(1)

##def read_from_db():
##    c.execute(" SELECT * FROM stuffToPlot WHERE Keyword='Akhil' ")
##    data = c.fetchall()
##    print(data)
##    for row in data:
##        print(row)
##        
##read_from_db()

def graph_data():
    c.execute('SELECT datestamp, value FROM stuffToPlot')
    data = c.fetchall()

    dates = []
    values = []
    
    for row in data:
        #print(row[0])
        dates.append(parser.parse(row[0]))
        #print(dates)
        #print(row[1])
        values.append(row[1])
        #print(values)

    plt.plot_date(dates,values,'-')
    plt.show()

graph_data()
#data_entry()

