import pandas as pd
import csv

df1 = pd.read_excel('NCFAS_all_scores.xls')
df2 = pd.read_excel('Raw TouchPoint Report_IFS_032415.xls') 
df3 = pd.DataFrame()
df2 = df2.iloc[:,[0,2,3,4]]
df2.columns = ['a','c','b','d']
df2['c'] = df2['c'].astype('category')
df2['c'] = df2['c'].cat.rename_categories([0,1,2,3,4,5,6,7,8])
df2['d'] = df2['d'].astype('category')
df2['d'] = df2['d'].cat.rename_categories([0,1,2,3,4,5,6,7])

x = [2, 3, 6, 7]
for i in range(0, len(df2.index)):
    if df2.ix[i, 'd'] in x:
        df2.ix[i, 'e']= 1
    else:
        df2.ix[i,'e'] = 0
df1 = df1.iloc[0:,[0,1,14,15]]
df1.columns = ['a','b','d','e']
df1['c'] = 9
adults = df1['a'].unique()
for i in range(0, len(df1.index)):
    df1.ix[i,'f'] = df1.ix[i,'d']+df1.ix[i,'e']
for i in range(0, len(df1.index)-1):
        if (df1.ix[i, 'a'] == df1.ix[i+1, 'a']):
            if (df1.ix[i, 'f'] < df1.ix[i+1, 'f']):
                df1.ix[i+1, 'g'] = 1
            else:
                df1.ix[i+1, 'g'] = 0
# df1['c'] = df1['c'].astype('category')
# df1['c'] = df1['c'].cat.rename_categories([4,5,1,2,3,0])
for i in range(0, len(df2.index)):
    if df2.ix[i,'a'] in adults:
        df3 = df3.append(df2.ix[i, ['a','b','c','e']])
for i in range(0, len(df1.index)):
    df3 = df3.append(df1.ix[i, ['a','b','c','g']])
result = df3.sort(['a','b'])
writer = open("submit.csv", "wb" )
f = csv.writer(writer)
f.writerow(["person"]+["date"]+["intervention"]+["attendance"]+["increase"])
for row in range(0,len(result.index)):
     i,j,k,l,m = result.iloc[row] 
     f.writerow([str(i)] +[str(j)]+[str(k)]+[str(l)]+[str(m)]) 
writer.close()

