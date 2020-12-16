# from module_0722 import fun
import random
import datetime
# import sys
#
# print(sys.path)
import pickle

# a = 'python'
# a = a.replace('y', 'e')
# print(a)

# enumerate
# 리스트가 있는 경우 순서와 리스트의 값을 전달하는 기능
# 열거, 순서가 있는 자료형을 입렵으로 받아 인덱스를 포함하는
# enumerate 객체를 반환
b = enumerate([1,2,3])
for i in b:
    print(i)

for i, value in enumerate('python', 100):
    print(i, value)
#
# #zip
# number = [1,2,3,4,5]
# name = ['이비세비치', '요비치', '돈치치', '레비치']
#
# person = list(zip(number, name))
# print(person)

#pickle
# name = 'bjp'
# age = 26
# address = '부천'
# score = {'kor' : 100, 'programming' : 50}
#
# with open('매수종목1.txt', 'wb') as file:
#     pickle.dump(name, file)
#     pickle.dump(age, file)
# with open('매수종목1.txt', 'rb') as file:
#     name = pickle.load(file)
#     age = pickle.load(file)
#
#     print(name, age)

random.random()
print(datetime.datetime.now())
print(type(datetime.datetime.now()))