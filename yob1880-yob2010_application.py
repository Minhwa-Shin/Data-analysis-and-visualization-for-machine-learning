import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 1. “yob1880.txt” 파일을 읽어 데이터 프레임으로 구성한다.
# 이 때 columns = ['name', 'sex', 'births']로 이루어져야 한다.
df=pd.read_csv('yob1880.txt',names=['name','sex','births'])

# 2. 1번에서 만든 데이터프레임의 앞에 10개, 뒤에 10개의 데이터를 출력한다.
print(df[:10],'\n')
print(df[-10:],'\n')

# 3. 위의 데이터프레임을 'sex'로 그룹화하고, 이렇게 그룹화한 데이터로부터 'births' 데이터의 합을 출력한다.
grouped=df.groupby('sex')
print(grouped['births'].sum(),'\n')

# 4. “yob1880.txt” ~ “yob2010.txt” 파일을 데이터프레임으로 읽어 들인다.
# 이때 연도 파일의 연도를 참조하여 각 데이터프레임에 항목 ‘year’를 추가하여 저장한다.
names=[]
for year in range(1880,2011):
    filename='yob'+str(year)+'.txt'
    df=pd.read_csv(filename,names=['name','sex','births'])
    df['year']=year
    names.append(df)

# 5. 4번에서 연도별 파일로부터 만든 각각의 데이터프레임들을 하나의 데이터프레임으로 합친다.
# 이때 합쳐진 데이터프레임은 'names' 변수로 저장한다.
names=pd.concat(names,ignore_index=True)
# print(names,'\n')

# 6. names 데이터프레임을 index='year', columns='sex'로 그룹화하고,
# 이렇게 그룹화한 데이터프레임에서 'births' 데이터의 합을 구한다.
# 이 때 데이터 그룹화는 groupby 대신 pivot_table 함수를 사용한다.
pivotTable=names.pivot_table(index='year',columns='sex',aggfunc=sum)
print(pivotTable.births,'\n')

# 7. 6번 문제에서 만들어진 그룹 데이터를 선 그래프로 도식화한다.
pivotTable['births'].plot()
plt.show()

# 8. 'names' 데이터프레임에 'prop'열을 추가해서 각 이름이 전체 출생 수에서 차지하는 비율을 계산하여 삽입 후 출력한다.
# (.ex:1880, 1881, 1882… 2010년도 별로 각 년도의 출생 수 합에 대한 이름 비율을 계산하여 삽입한다.)
names['prop']=names.births.div(names.year.map(pivotTable['births'].sum(axis=1)))
print(names,'\n')
