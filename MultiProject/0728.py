import matplotlib.pyplot as plt

histo = [46,15,4,34,48,1,13,1,4,8,46,4,48,8,7,79,8,64,3,4,87]
plt.hist(histo)
plt.show()
plt.hist(histo, bins=8)
plt.xlabel('일자')
plt.ylabel('연속 게임 시간')
plt.title('바람의 나라 : 연')
plt.grid()
# 피부과, 약 받기, 가족 결합, 정처기 제출, 집 방역 신청, 물 시키기, 닭 시키기, 이력서 제출, 코테 공부, 정처기 공부, 프로젝트 계획

fruit = ['사과', '바나나', '딸기', '오렌지', '포도']
result = [7, 6, 3, 2, 2]
explode_value = (0.1, 0, 0, 0, 0)
plt.pie(result)
plt.figure(figsize=(5, 5)) # 그래프 크기
plt.pie(result, labels=fruit, autopct='%.1f%%', startangle=90, counterclock=False, explode=explode_value, shadow=True)
plt.savefig('C:/Users/student/Desktop/figimg1.png', dpi=200) # 인치당 200
plt.show()

import pandas as pd
import matplotlib
s1 = pd.Series([1,2,3,4,5,6,7,8,9])
s1
s1.plot()
plt.show()
s2 = pd.Series([1,2,3,4,5,6,7,8,9,10], index=pd.date_range('2019-01-01', periods=10))
s2

df_emp = pd.read_csv('C:/Users/student/Desktop/employees.csv', index_col='HIRE_DATE')
df_emp
matplotlib.rcParams['font.family'] = 'Malgun Gothic'
matplotlib.rcParams['axes.unicode_minus'] = False
df_emp.plot()
plt.show()

year = [2006, 2008, 2010, 2012 , 2014, 2016]
area = [26.2, 27.8, 28.5, 31.7, 33.5, 33.2]
table = {'연도': year, '주거면적': area}
df_area = pd.DataFrame(table, columns=['연도', '주거면적'])
df_area.plot(x='연도', y='주거면적', grid=True, title='연도별 1인당 주거면적')
plt.show()

temperature = [25.2, 27.4, 22.9, 26.2, 29.5, 33.1, 30.4, 36.1, 34.4, 29.1]
Icecream_sales = [236500, 357500, 203500, 365200, 446600, 574200, 453200, 675400, 598400, 463100]
dict_data = {'기온':temperature, '판매량':Icecream_sales}
df_icecream = pd.DataFrame(dict_data, columns=['기온', '판매량'])
df_icecream

import requests
from bs4 import BeautifulSoup


r = requests.get('https://sports.news.naver.com/news.nhn?oid=430&aid=0000000854')
r.text[0:100]
html='''<html><body><div><span>\
<a href=http://naver.com>naver</a>\
<a href=http://google.com>naver</a>\
<a href=http://daum.com>naver</a>\
</span></div></body></html>'''
soup = BeautifulSoup(html, 'html.parser')
soup
print(soup.prettify())
soup.find_all('a')


html = '''
<html>
    <head>
        <title> 바람의 나라 : 연 </title>
    <head>
    <body>
        <div id='upper' class='bjp' custom='good'>
            <h3 title='주술사'>
                뷰티풀 수프
            </h3>
        </div>
        <div id='lower' class='bjp'>
            <p> 헬파이어 </p>
            <p> 뢰격주 </p>
            <p> 뽀로로 </p>
        </div>
    </body>
</html>
'''
bs = BeautifulSoup(html,'html.parser')
bs
h3_tag = bs.find('h3')
h3_tag.get_text()

bs.find('p')
bs.find_all('p')
bs.find('div')


url = 'https://sports.news.naver.com/news.nhn?oid=430&aid=0000000854'
html_web = requests.get(url).text
soup_web = BeautifulSoup(html_web, 'html.parser')
website_rank = soup_web.select('div.default_h h3')
header = [website_rank_add.get_text() for website_rank_add in website_rank]
header



url = 'https://www.weather.go.kr/weather/observation/currentweather.jsp'
resp = requests.get(url)
resp
bs = BeautifulSoup(resp.text, 'html.parser')
table = bs.find('table', class_='table_develop3')
data = []

for tr in table.find_all('tr'):
    tds = list(tr.find_all('td'))
    for td in tds:
        if td.find('a'):
            point = td.find('a').text
            temperature = tds[5].text
            humidity = tds[9].text
            data.append({'point':point, 'temperature':temperature, 'humidity':humidity})
weather = pd.DataFrame(data)
weather
weather.to_csv('C:/Users/student/Desktop/weather.csv', encoding='cp949')
weather.to_csv('C:/Users/student/Desktop/weather2.csv')
df = pd.read_csv('C:/Users/student/Desktop/weather2.csv')

df = pd.DataFrame(df)
df[0]
df7 = df.groupby({'point':['인천', '부천']})
df7 = df.loc['point']['인천', '부천']
data
temper = []

temper