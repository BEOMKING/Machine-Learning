import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

dayold = pd.read_excel('C:/Users/박범진/Desktop/dayold2.xls', index_col='시군구', encoding='cp949')
daychild = pd.read_excel('C:/Users/박범진/Desktop/daychild2.xls', index_col='시군구', encoding='cp949')

matplotlib.rcParams['axes.unicode_minus'] = False
matplotlib.rcParams['font.family'] = 'Malgun Gothic'
# 요일별 노인 사고
dayold2015= dayold.loc['일요일':'토요일', ['서초구', '영등포구', '강남구','강서구','송파구']]
plt.xlabel('요일')
plt.ylabel('발생빈도')
plt.title('2015 요일별 사고건수')
plt.plot(dayold2015)
plt.subplot(2,3,1)

dayold2016= dayold.loc['일요일.1':'토요일.1', ['서초구', '영등포구', '강남구','강서구','송파구']]
plt.figure()
plt.xlabel('요일')
plt.ylabel('발생빈도')
plt.title('2016 요일별 사고건수')
# plt.show()
plt.subplot(2,3,2)
plt.plot(dayold2015)
dayold2015.plot()

dayold2017= dayold.loc['일요일.2':'토요일.2', ['서초구', '영등포구', '강남구','강서구','송파구']]
plt.figure()
dayold2017.plot()
plt.xlabel('요일')
plt.ylabel('발생빈도')
plt.title('2017 요일별 사고건수')
plt.show()
plt.subplot(2,3,3)
plt.plot(dayold2015)

dayold2018= dayold.loc['일요일.3':'토요일.3', ['서초구', '영등포구', '강남구','강서구','송파구']]
plt.figure()
dayold2018.plot()
plt.xlabel('요일')
plt.ylabel('발생빈도')
plt.title('2018 요일별 사고건수')

# plt.show()
plt.subplot(2,3,4)
plt.plot(dayold2015)


dayold2019= dayold.loc['일요일.4':'토요일.4', ['서초구', '영등포구', '강남구','강서구','송파구']]
dayold2019
plt.figure(9)
plt.xlabel('요일')
plt.ylabel('발생빈도')
plt.title('2019 요일별 사고건수')
plt.show()
plt.subplot(2,3,5)
plt.plot(dayold2015)

# daychild

daychild2015= daychild.loc['일요일':'토요일', ['서초구', '영등포구', '강남구','강서구','송파구']]
plt.figure()
daychild2015.plot()
plt.xlabel('요일')
plt.ylabel('발생빈도')
plt.title('2015 요일별 어린이 사고건수')
plt.show()
plt.subplot(2,3,1)
plt.plot(dayold2015)

daychild2016= daychild.loc['일요일.1':'토요일.1', ['서초구', '영등포구', '강남구','강서구','송파구']]
plt.figure()
daychild2016.plot()
plt.xlabel('요일')
plt.ylabel('발생빈도')
plt.title('2016 요일별 어린이 사고건수')
plt.show()
plt.subplot(2,3,2)
plt.plot(dayold2015)

daychild2017= daychild.loc['일요일.2':'토요일.2', ['서초구', '영등포구', '강남구','강서구','송파구']]
plt.figure()
daychild2017.plot()
plt.xlabel('요일')
plt.ylabel('발생빈도')
plt.title('2017 요일별 어린이 사고건수')
plt.show()
plt.subplot(2,3,3)
plt.plot(dayold2015)

daychild2018= daychild.loc['일요일.3':'토요일.3', ['서초구', '영등포구', '강남구','강서구','송파구']]
plt.figure()
daychild2018.plot()
plt.xlabel('요일')
plt.ylabel('발생빈도')
plt.title('2018 요일별 어린이 사고건수')

# plt.show()
plt.subplot(2,3,4)
plt.plot(dayold2015)


daychild2019= daychild.loc['일요일.4':'토요일.4', ['서초구', '영등포구', '강남구','강서구','송파구']]
plt.figure()
daychild2019.plot()
plt.xlabel('요일')
plt.ylabel('발생빈도')
plt.title('2019 요일별 어린이 사고건수')
plt.show()
plt.subplot(2,3,5)
plt.plot(dayold2015)