from datetime import datetime

stamp=datetime(2017,1,3)
print(str(stamp),'\n')
print(stamp.strftime('%Y-%m-%d'),'\n')

value='2017-1-05'
date1=datetime.strptime(value,'%Y-%m-%d')
print(date1,'\n')

datestrs=['7/6/2018','8/6/2018']
print([datetime.strptime(x,'%m/%d/%Y') for x in datestrs],'\n')

from dateutil.parser import parse
print(parse('2017-01-03'),'\n')
print(parse('Jan 31, 2001 10:45 PM'),'\n')
