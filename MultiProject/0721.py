from abc import *
import random

#상속 이미 만들어짅 클래스의 변수와 함수를 그대로 이어받고 새로운 내용
#만 추가해서 클래스 선언 , 부모 클래스는 상위 클래스 혹은 슈퍼클래스
#자식 클래스는 하위클래스 혹은 서브 클래스
class Person:
    def __init__(self, name):
        self.name = name
        print('부모 클래스 init 호출')
    def hello(self):
        print('hi')
class Student(Person):
    def __init__(self, name):
        super().__init__(name) # 표현 1
        #Person.__init__(self, name) # or 2
        print('Student 모듈')

    def hello(self): # 메서드 오버라이딩
        super().hello()
        print('항녕')
    def study(self):
        print('concentration')

#bjp = Student('bjp')

'''#다중 상속
class A:
    def hello(self):
        print('ㅎㅇ')

class B:
    def hello(self):
        print('ㅎㅇ2')

class C(A):
    def helloo(self):
        print('ㅎㅇ3')
class D(C, B):
    pass
child = D()
child.hello()
print(D.mro()) # 상속 순서 출력 함수'''

class StudentBase(metaclass=ABCMeta):
    def hello(self):
        print('안녕')
    @abstractmethod
    def study(self):
        pass
# bjp = StudentBase() 추상 클래스는 객체 생성 불가
# 오직 부모 역할을 하기 위해서만 있는 존재
class Student(StudentBase):
    def study(self):# 상속 받은 추상 메서드는 반드시 구현
        print('공부')

class Account:
    account_count = 0
    def __init__(self, name, balance):
        self.deposit_count = 0
        self.name = name
        self.balance = balance
        self.bank = '신한은행'

        num1 = random.randint(0, 999)
        num2 = random.randint(0, 99)
        num3 = random.randint(0, 999999)

        num1 = str(num1).zfill(3)  # 1 -> '1' -> '001'
        num2 = str(num2).zfill(2)  # 1 -> '1' -> '01'
        num3 = str(num3).zfill(6)
        self.account_number = num1 + '-' + num2 + '-' + num3
        Account.account_count += 1

    @classmethod
    def get_account_num(cls):
        print(cls.account_count)

    def deposit(self, money):
        self.balance += money
        self.deposit_count += 1
        if self.deposit_count % 5 == 0:
            self.balance *= 1.01

    def withdraw(self, money):
        self.balance -= money

data = []
k = Account("KIM", 10000000)
l = Account("LEE", 10000)
p = Account("PARK", 10000)
data.append(k)
data.append(l)
data.append(p)
    # 예외 처리
# i = int(input())
# try:
#     print(10 / i)
# except:
#     print('되겠니?')
# try:
#     list = [10, 20, 30]
#     index, x = map(int, input('인덱스와 나눌 숫자 : ').split())
#     print(list[index] / x)
#  except IndexError:  파이참 부분 선택 주석 ctrl /
#      print('인덱스 오류임')
#  except ZeroDivisionError:
#      print('선 넘네')
# except Exception: #모든 예외의 에러 메시지를 출력하고 싶다면 Exception
#     print('ㅇ?')

# try:
#     value = int(input('3의 배수 ㄱㄱ'))
#     if value % 3 != 0:
#         raise Exception
#     print(value)
# except Exception as e:
#     print('예외 발생', e)
#
# class bjp(Exception):
#     def __init__(self):
#         super().__init__('3의 배수 아님')

class Car:
    def __init__(self, wheel, price):
        self.wheel = wheel
        self.price = price
    def info(self):
        print('바퀴수 : ', self.wheel)
        print('가격 : ', self.price)

class Bycycle(Car):
    def __init__(self, wheel, price, 구동계):
        super().__init__(wheel, price)
        self.구동계 = 구동계
    def info(self):
        super().info()
        print('구동계 : ', self.구동계)
class Car2(Car):
    def __init__(self, wheel, price):
        super().__init__(wheel, price)

# f = open("C:/Users/Student/Desktop/매수종목1.txt")
# lines = f.readlines()
# dic = {}
# for i in lines:
#     dic.append(i.split(''))
# f.close
# print(dic)
print('아오 적당히 해야지'.split(maxsplit=1))
print()