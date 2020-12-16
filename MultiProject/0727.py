import pandas as pd # numpy를 기반으로 만들어짐
# numpy는 같은 데이터 타입 배열만 처리, pandas는 데이터 타입이 다양하게 섞여있어도 가능
df_train = pd.read_csv('C:/Users/student/Desktop/train.csv')
Survived1 = df_train[df_train['Survived'] == 1]['Age'].mean()
df_train[df_train['Survived'] == 1]['Age'].fillna(Survived1)
df_train.drop(['Age2'], axis=1)
data_frame = pd.read_csv('C:/Users/student/Desktop/student.csv',  encoding = 'ISO-8859-1')
df_train['Pclass'] = df_train['Pclass'].astype(str)
df_train.info()
df_train['Age']

s1 = pd.Series([10,20,30])
s2 = pd.Series([10,20,30], index=[1,2,3])
s1
s1.index
s1.values
s2
import math
import os
import numpy as np

def age_categorize(age):
    if math.isnan(age):
        return -1
    return math.floor(age / 10) * 10
df_train['Age'].apply(age_categorize)

# group by

pclass_group = df_train.groupby('Pclass')
pclass_group.groups
df_train.groupby(['Pclass', 'Sex']).mean().index
df_train.set_index(['Pclass', 'Sex']).reset_index()
df_train.set_index('Age').groupby(age_categorize).mean()['Survived']
df_train.set_index('Age').groupby(level=0).mean()


df_train.groupby(['Pclass', 'Age']).aggregate([np.sum, np.mean, np.max])
df_train.groupby('Pclass').mean()
df_train['Age2'] = df_train.groupby('Pclass').transform(np.mean)['Age']
df_train.head(3)

dent_list = [{'name' : 'park', 'sex' : 'male', 'major' : 'Computer Science'},
             {'name' : 'kim', 'sex' : 'female', 'major' : 'java'},
             {'name' : 'lee', 'sex' : 'female', 'major' : 'c'},
             {'name' : 'sim', 'sex' : 'male', 'major' : 'c++'},
             {'name' : 'song', 'sex' : 'female', 'major' : 'python'},
             {'name' : 'park', 'sex' : 'male', 'major' : 'Computer Science'},
             {'name' : 'park', 'sex' : 'male', 'major' : 'Computer Science'},
             {'name' : 'park', 'sex' : 'male', 'major' : 'Computer Science'}
             ]
df = pd.DataFrame('name', 'sex', 'major')
major_group = df.groupby('major')
df.duplicated(['name'])
df.drop_duplicates(['name'], keep='first')

data_list = [
    {'yyyy-mm-dd' : '1995-09-06'},
    {'yyyy-mm-dd' : '1999-09-20'},
    {'yyyy-mm-dd' : '1966-01-14'},
    {'yyyy-mm-dd' : '1966-02-02'}
]
df = pd.DataFrame(data_list, columns=['yyyy-mm-dd'])
df
def get_year(column):
    return column.split('-')[0]
def get_residentnum(column):
    return column.split('-')[:3]
get_year('1995-09-06')
df['year'] = df['yyyy-mm-dd'].apply(get_year)
df
df[' Resident registration'] = df['yyyy-mm-dd'].apply(get_residentnum)
df

list1 = [
    {'name' : 'bjp', 'lang' : 'python'},
    {'name' : 'lbm', 'lang' : 'java'},
    {'name' : 'syk', 'lang' : 'c++'}
]
list2 = [
    {'name' : 'sms', 'lang' : 'go'},
    {'name' : 'khy', 'lang' : 'R'},
    {'name' : 'ljy', 'lang' : 'c++'}
]
df1 = pd.DataFrame(list1, columns=['name', 'lang'])
df2 = pd.DataFrame(list2, columns=['name', 'lang'])
df1
df2
result_df = pd.concat([df1,df2])
result_df
df1.append(df2)
df1
df1.append(df2, ignore_index=True)
list3 = [
    {'age':26, 'address':'경기도 부천시'},
    {'age':26, 'address':'경기도 구리시'},
    {'age':27, 'address':'서울시 노원구'}
]
df3 = pd.DataFrame(list3, columns=['age', 'address'])
result_col = pd.concat([df1, df3], axis=1)
result_col

emp_df = pd.read_csv('C:/Users/student/Desktop/employees.csv')
dept_df = pd.read_csv('C:/Users/student/Desktop/department.csv')
dept_df
pd.merge(emp_df, dept_df, on='DEPARTMENT_ID', how='left')



cus = pd.read_csv('C:/Users/student/Desktop/customer.csv')
ord = pd.read_csv('C:/Users/student/Desktop/orders.csv')
cus
ord
pd.merge(cus, ord, on='customer_id').groupby('item').sum().sort_values(by='quantity', ascending=False)
cus.join(ord).groupby(['name', 'item']).sum().loc['영희', '길동', '영수','수민','동건']
cus.join(ord)

# 시각화 matplotlib
import matplotlib.pyplot as plt

data = [12, 50, 36, 80]
plt.plot(data)
x = np.arange(-4.5, 5, 0.5)
y1 = 2*x**2
plt.plot(x, y1)

y2 = 5*x + 30
y3 = 4*x**2 + 10
plt.plot(x, y1)
plt.plot(x, y2)
plt.plot(x, y3)
plt.plot(x, y1, x, y2, x, y3)

plt.figure()

y4 = 10*np.exp(-x) + 1
plt.subplot(2,2,1)
plt.plot(x, y4)
plt.subplot(2,2,2)
plt.plot(x, y1)
plt.subplot(2,2,3)
plt.plot(x, y2)
plt.subplot(2,2,4)
plt.plot(x, y3)
plt.show()




