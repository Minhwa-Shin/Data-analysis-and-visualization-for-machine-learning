import requests
from lxml.html import parse
from io import StringIO
import pandas as pd

text = requests.get('http://finance.yahoo.com/q/op?s=AAPL+Options').text
parsed = parse(StringIO(text))
doc = parsed.getroot()
links = doc.findall('.//a')
print(links[15:20])
lnk = links[27]
print(lnk.get('href'),'\n')
urls = [lnk.get('href') for lnk in doc.findall('.//a')]
print(urls[-10:],'\n')

url = 'https://api.github.com/repos/pydata/pandas/milestones/28/labels'
resp=requests.get(url)
print(resp,'\n')

data=resp.json()
print(data,'\n')

df=pd.DataFrame(data)
print(df['url'])
