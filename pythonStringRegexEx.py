val='a,b, kim'
print(val.split(','))
pieces=[x.strip() for x in val.split(',')]
print(pieces,'\n')

# first,second,third=pieces
print('::'.join(pieces),'\n')
print(val.index(','),'\n')
print(val.count(','),'\n')
print(val.replace(',','::'),'\n')

import re

# text='foo bar\t baz \ttqux'
text='foo   bar\t baz   \tqux'
print(re.split('\s+',text),'\n')

regex=re.compile('\s+')
print(regex.split(text),'\n')
print(regex.findall(text),'\n')

text='''Dave dave@google.com
Steve steve@gmail.com
Rob rob@gmail.com
Ryan ryan@yahoo.com'''

pattern=r'[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4}'
regex=re.compile(pattern,flags=re.IGNORECASE)
print('findall:',regex.findall(text),'\n')

m=regex.search(text)
print('text:',text[m.start():m.end()],'\n')

pattern=r'([A-Z0-9._%+-]+)@([A-Z0-9.-]+)\.([A-Z]{2,4})'
regex=re.compile(pattern,flags=re.IGNORECASE)
m=regex.match('wesm@lge.com')
print(m.groups(),'\n')
