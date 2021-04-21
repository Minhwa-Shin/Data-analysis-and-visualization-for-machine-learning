import json
import pandas as pd
import matplotlib.pyplot as plt

db=json.load(open('foods-2011-10-03.json'))

# Number of Foods
print("Number of Foods : ", len(db),'\n')
# keys for each Food
print("Keys for each Food : ",db[0].keys(),'\n')

nutrients = pd.DataFrame(db[0]['nutrients'])
print("Nutrients:",'\n')
print(nutrients[:7],'\n')

# description, group, id, manufacturer extraction
info_keys=['description','group','id','manufacturer']
info=pd.DataFrame(db,columns=info_keys)
print(info[:5],'\n')

print("Distribution of Foods group:")
print(pd.value_counts(info.group)[:10],'\n')

nutrients=[]
for rec in db:
    foodData=pd.DataFrame(rec['nutrients'])
    foodData['id']=rec['id']
    nutrients.append(foodData)

nutrients=pd.concat(nutrients,ignore_index=True)
print(nutrients,'\n')

nutrients=nutrients.drop_duplicates()
nutrients=nutrients.rename(columns={'description':'nutrient','group':'nutgroup'},copy=False)
print(nutrients,'\n')

info=info.rename(columns={'description':'food','group':'fgroup'})
print(info,'\n')

ndata=pd.merge(nutrients,info,on='id',how='outer')
print(ndata.loc[3000],'\n')

result=ndata.groupby(['nutrient','fgroup'])['value'].quantile(0.5)
result['Zinc, Zn'].sort_values().plot(kind='barh')
plt.show()

print(result['Zinc, Zn'].sort_values(),'\n')
