import pandas as pd
from sklearn.model_selection import train_test_split

# 데이터 전처리
def hour(hour):
    if hour >= 0 and hour < 6:
        return '새벽'
    elif hour >= 6 and hour < 12:
        return '오전'
    elif hour >= 12 and hour < 18:
        return '오후'
    elif hour >= 18:
        return '저녁'
def weat(month):
    if month >= 3 and month < 6:
        return '봄'
    elif month >= 6 and month < 9:
        return '여름'
    elif month >= 9 and month < 12:
        return '가을'
    else:
        return '겨울'

def display_scores(scores):
    print('점수 : ', scores)
    print('평균 : ', scores.mean())
    print('표준 편차 : ', scores.std())

def measureRMSE(model): # 평균 제곱근 오차 (rmse) 측정
    scores = cross_val_score(model, pfwdX, pfwdY, scoring='neg_mean_squared_error', cv=5)
    rmse = np.sqrt(-scores)
    display_scores(rmse)
seed = 777

weather = pd.read_csv('C:/DataSet/Data/jeju/2017~2018.csv') # 기온 데이터
electronic = pd.read_csv('C:/DataSet/Data/jeju/final17-20.csv') # 전력량 데이터
df = pd.DataFrame({'년월일시': pd.to_datetime(weather['일시'])}) # 일시를 이용해서 시간대와 계절을 나눔 / 데이터 프레임 형태 생성
df['month'] = df['년월일시'].dt.strftime('%m') # 년월일시 중 월만 추출
df['month'] = pd.to_numeric(df['month']) # 추출한 월 데이터 숫자 형태로 변경
df['hour'] = df['년월일시'].dt.strftime('%H')
df['hour'] = pd.to_numeric(df['hour'])
df = df[['month', 'hour']]
weather = pd.concat([weather, df], axis=1) # 기온데이터에 월, 시간 컬럼 추가
weather['시간대'] = weather.apply(lambda x: hour(x['hour']), axis=1) # 시간 컬럼을 이용해 hour함수 적용
weather['계절'] = weather.apply(lambda x: weat(x['month']), axis=1) # 월 컬럼을 이용해 weat함수 적용
weather = weather[['기온', '풍속', '습도', '지면온도', '시간대', '계절']]
# print(weather.계절.value_counts())
pfwd = pd.get_dummies(weather) # 원핫인코딩이 수행된(계절, 시간대에 관한 특성이 추가된) 기온 데이터(plus feature weather data)
# print(list(weather.columns))
electronic = electronic[['전력량']]
pfwdtrain = pd.concat([pfwd, electronic], axis=1)

# EDA
import seaborn as sns
import matplotlib.pyplot as plt
matrix = pfwdtrain.corr() # 특성간의 상관관계를 수치로 표현
matrix['전력량'].sort_values(ascending=False)
plt.figure(figsize=(12,12))
sns.heatmap(data=matrix, annot=True, fmt='.2f', linewidths=5, cmap='Blues')
plt.show()

# 데이터 분리
pfwdtrain = pfwdtrain.dropna() # 데이터에서 빈 값 제거
pfwdtest = pfwdtrain[30633:] # 특성 추가 테스트 테이터셋
pfwdtrain = pfwdtrain[:30633] # 툭성 추가 훈련 데이터셋

pfwdY = pfwdtrain['전력량']
pfwdX = pfwdtrain.drop('전력량', axis=1)
pfwdX_train, pfwdX_valid, pfwdY_train, pfwdY_valid= train_test_split(pfwdX, pfwdY, test_size=0.3, random_state=seed)
testY = pfwdtest['전력량']
testX = pfwdtest.drop('전력량', axis=1)


# 선형 회귀
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import cross_val_score
import numpy as np

FA_LR = LinearRegression()
measureRMSE(FA_LR)

# 다항 회귀
from sklearn.preprocessing import PolynomialFeatures
poly_feature = PolynomialFeatures(degree=2, include_bias=True)
polyX = poly_feature.fit_transform(pfwdX)
FA_PF = LinearRegression()
FA_PF_scores = cross_val_score(FA_PF, polyX, pfwdY, scoring='neg_mean_squared_error', cv=5)
FA_PF_rmse = np.sqrt(-FA_PF_scores)
display_scores(FA_PF_rmse)

# SVR
from sklearn.svm import SVR
FA_SVR = SVR(kernel="linear")
measureRMSE(FA_SVR)

# 결정트리
from sklearn.tree import DecisionTreeRegressor
FA_DTR = DecisionTreeRegressor()
measureRMSE(FA_DTR)

# 에이다부스트
from sklearn.ensemble import AdaBoostRegressor
FA_ABR = AdaBoostRegressor(random_state=seed, n_estimators=100)
measureRMSE(FA_ABR)

# 경사하강법
from sklearn.linear_model import SGDRegressor
FA_SGD = SGDRegressor(random_state=seed)
measureRMSE(FA_SGD)

# 엘라스틱넷
from sklearn.linear_model import ElasticNet
FA_EN = ElasticNet(alpha=0.1)
measureRMSE(FA_EN)

# 랜덤 포레스트
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
FA_RFR = RandomForestRegressor()
measureRMSE(FA_RFR) # 파라미터 튜닝 전

# 파라미터 튜닝 gridsearchcv
param_grid = [
    {'n_estimators': [100, 200], 'max_features': ["auto", "log2", "sqrt"], 'max_depth': [1, 3, 5]
    , 'min_samples_leaf': [1, 3, 5]}
  ]
HTFA_RFR = RandomForestRegressor(random_state=777)
grid_search = GridSearchCV(HTFA_RFR, param_grid, cv=5,
                           scoring='neg_mean_squared_error',
                           return_train_score=True)
grid_search.fit(pfwdX, pfwdY) # 최적의 파라미터 출력 * 오래걸림
grid_search.best_params_
grid_search.best_estimator_ # 최적 파라미터

final_model = grid_search.best_estimator_
final_predictions = final_model.predict(testX)
final_mse = mean_squared_error(testY, final_predictions)
final_rmse = np.sqrt(final_mse)
final_rmse # 튜닝 후 랜덤 포레스트
final_model = RandomForestRegressor(max_depth=5, min_samples_leaf=5, n_estimators=200,
                      random_state=777)
measureRMSE(final_model)

# 그레디언트부스트
from sklearn.ensemble import GradientBoostingRegressor
FA_GBR = GradientBoostingRegressor(random_state=seed, n_estimators=100, learning_rate=0.05)
measureRMSE(FA_GBR) # 튜닝 전

# 파라미터 튜닝 gridsearchcv
param_grid = [
    {'n_estimators': [100, 200], 'max_features': ["auto", "log2", "sqrt"], 'max_depth': [3, 5, 8]
    , 'min_samples_leaf': [1, 3, 5], 'learning_rate': [0.1, 0.05, 0.01]}
  ]
HTFA_GBR = GradientBoostingRegressor(random_state=seed)
grid_search = GridSearchCV(HTFA_GBR, param_grid, cv=5,
                           scoring='neg_mean_squared_error',
                           return_train_score=True)
grid_search.fit(pfwdX, pfwdY) # 튜닝 *오래걸림
grid_search.best_params_
grid_search.best_estimator_ # 최적의 파리미터


final_model = grid_search.best_estimator_
final_model = GradientBoostingRegressor(learning_rate=0.01, max_depth=8, max_features='log2',
                          min_samples_leaf=5, n_estimators=200,
                          random_state=777)
final_model.fit(pfwdX, pfwdY)
final_predictions = final_model.predict(testX)

final_mse = mean_squared_error(testY, final_predictions)
r2 = r2_score(testY, final_predictions)
final_rmse = np.sqrt(final_mse)
final_rmse # 튜닝 후 그레디언트부스트 오차
r2
measureRMSE(final_model)