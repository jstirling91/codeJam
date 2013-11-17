import csv
import time
import sqlite3
conn = sqlite3.connect('data.db')
c = conn.cursor()
#c.execute('DROP TABLE radiation')
#c.execute('DROP TABLE humidity')
#c.execute('DROP TABLE temp')
#c.execute('DROP TABLE wind')
#c.execute('CREATE TABLE time (id TEXT PRIMARY KEY)')
#c.execute('CREATE TABLE month (id TEXT PRIMARY KEY)')
#c.execute('CREATE TABLE day (id TEXT PRIMARY KEY)')
#c.execute('CREATE TABLE radiation (id INTEGER PRIMARY KEY)')
#c.execute('CREATE TABLE humidity (id FLOAT PRIMARY KEY)')
#c.execute('CREATE TABLE temp (id FLOAT PRIMARY KEY)')
#c.execute('CREATE TABLE wind (id INTEGER PRIMARY KEY)')
#c.execute('DROP TABLE data')
#c.execute('CREATE TABLE data (id FLOAT, hits INTERGER DEFAULT 0, time TEXT, month TEXT, day TEXT, radiation INTEGER, humidity FLOAT, temp FLOAT, wind INTEGER, FOREIGN KEY(time) REFERENCES time(id), FOREIGN KEY(month) REFERENCES month(id), FOREIGN KEY(day) REFERENCES day(id), FOREIGN KEY(radiation) REFERENCES ratiation(id), FOREIGN KEY(humidity) REFERENCES humidity(id), FOREIGN KEY(temp) REFERENCES temp(id), FOREIGN KEY(wind) REFERENCES wind(id))')
#conn.commit()
with open('data_set.csv', 'r') as f:
    reader = csv.reader(f)
    i = 0
    ii = 0
    rad = 0
    hum = 0
    tempe = 0
    wind = 0
    start = 0
#    temp = reader
#    temp.next()
#    y = temp.next()[1]
#    y = int(y)
#    for iii in range (0, 3):
#        temp.next()
#    x = temp.next()[1]
#    x = int(x)
#    z = (x - y)/4
#    for iii in range (0, 3):
#        print y
#        y = y + z
#    print x
    print type(reader)
    diffRad = 0
    diffHum = 0
    diffTemp = 0
    diffWind = 0
    listRad = []
    listHum = []
    listTemp = []
    listWind = []
    for row in reader:
        if i == 0:
            i += 1
        else:
            if ii == 0:
#                print row
                listRad.append(int(row[1]))
                listHum.append(float(row[2]))
                listTemp.append(float(row[3]))
                listWind.append(int(row[4]))
                #                rad = float(row[1])
                #                #min: -333	max: 858
                #                hum = float(row[2])
                #                #min: 0.15	max: 1.0
                #                tempe = float(row[3])
                #                #min: -29.3	max: 35.0
                #                wind = int(row[4])
                #                #min: 0	max: 50
#        else:
#            print row
            ii = (ii + 1)%4
    f.seek(0)
    reader = csv.reader(f)
    print listRad[0]
    i = 0
    index = 0
    for row in reader:
        
        if i == 0:
            i += 1
        else:
#            print row
            temp = row[0].split('T')
            date = temp[0].split('-')
            time = temp[1].split('-')
            if ii == 0:
                if index < len(listRad) - 1:
                    diffRad = (listRad[index + 1] - listRad[index]) / 4
                    diffHum = (listHum[index + 1] - listHum[index]) / 4.0
                    diffTemp = (listTemp[index + 1] - listTemp[index]) / 4.0
                    diffWind = (listWind[index + 1] - listWind[index]) / 4
                    index += 1
                rad = float(row[1])
                #min: -333	max: 858
                hum = float(row[2])
                #min: 0.15	max: 1.0
                tempe = float(row[3])
                #min: -29.3	max: 35.0
                wind = int(row[4])
                #min: 0	max: 50
#            else:
#                print row


#            temp = 'INSERT INTO time VALUES(\'' + time[0] + '\')'
#            try:
#                c.execute(temp)
#            except:
#                pass
#            temp = 'INSERT INTO month VALUES(\'' + date[1] + '\')'
#            try:
#                c.execute(temp)
#            except:
#                pass
#            temp = 'INSERT INTO day VALUES(\'' + date[2] + '\')'
#            try:
#                c.execute(temp)
#            except:
#                pass
#            temp = 'INSERT INTO radiation VALUES(%d)' % (rad)
#            try:
#                c.execute(temp)
#            except:
#                pass
#            temp = 'INSERT INTO humidity VALUES(%d)' % (hum)
#            try:
#                c.execute(temp)
#            except:
#                pass
#            temp = 'INSERT INTO temp VALUES(%d)' % (tempe)
#            try:
#                c.execute(temp)
#            except:
#                pass
#            temp = 'INSERT INTO wind VALUES(%d)' % (wind)
#            try:
#                c.execute(temp)
#            except:
#                pass
#

#            temp = 'INSERT INTO time VALUES(\'' + date[1] + time[0] + '\', \'' + date[1] + '\', \'' + time[0] + '\')'
#            try:
#                c.execute(temp)
#            except:
#                pass

#c.execute('CREATE TABLE data (id FLOAT, hits INTERGER DEFAULT 0, time TEXT, month TEXT, day TEXT, radiation INTEGER, humidity FLOAT, temp FLOAT, wind INTEGER, FOREIGN KEY(time) REFERENCES time(id), FOREIGN KEY(month) REFERENCES month(id), FOREIGN KEY(day) REFERENCES day(id), FOREIGN KEY(radiation) REFERENCES ratiation(id), FOREIGN KEY(humidity) REFERENCES humidity(id), FOREIGN KEY(temp) REFERENCES temp(id), FOREIGN KEY(wind) REFERENCES wind(id))')
#
            if row[5] != '':
                temp = 'INSERT INTO data VALUES(%d, 0, \'%s\', \'%s\', \'%s\', %d, %d, %d, %d)' % (float(row[5]), time[0], date[1], date[2], rad + ii * diffRad, hum + float(ii) * diffHum, tempe + float(ii) * diffTemp, wind + ii * diffWind)
                c.execute(temp)
            ii = (ii + 1)%4

#temp = 'SELECT id FROM date'
#c.execute(temp)
#for time in c.fetchall():
#    min = 100000
#    max = 0
#    temp = 'SELECT id FROM data WHERE date = \'' + time[0] + '\''
#    c.execute(temp)
##    print time[0]
#    i = 0
#    for data in c.fetchall():
#        if i == 0:
#            min = data[0]
#            max = min
#            i += 1
#        elif data[0] < min:
#            min = data[0]
#        elif data[0] > max:
#            max = data[0]
##            print max
#    print max - min

conn.commit()
conn.close()