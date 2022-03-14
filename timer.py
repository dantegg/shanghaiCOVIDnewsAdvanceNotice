import datetime

fileName = str(datetime.date.today()) + 'result.txt'
f = open(fileName, 'w')
f.write('hello' + '\n' + 'world')
f.close()