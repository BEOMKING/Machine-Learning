'''def print_5xn(line, num): #227
    count = 0
    for i in line:
        count += 1
        print(i, end='')
        if count % num == 0:
            print('\n')
# print_5xn("아이엠어보이유알어걸", 3)

def make_url(str):
    return 'www.' + str + '.com'
# print(make_url('naver'))

def make_list(str):
    return [i for i in str]
# print(make_list("abcd"))

class Person:
    def __init__(self, **kwargs):
        self.name = kwargs['name']
        self.age = kwargs['age']
bjp = Person(name='박범진', age=26)
print(bjp.name, bjp.age)

esther = Person(**{'name' : 'ruciper', 'age' : 18})
print(esther.name, esther.age)

class Book:
    pass
python = Book()
python.name = '파이썬 입문'
print(python.name)

class Person:
    def __init__(self, **kwargs):
        self.__name = kwargs['name'] #앞의 __는 비공개 속성을 나타냄
        self.age = kwargs['age']

    def get_name(self):
        return self.__name
bjp = Person(name='범킹', age='26')
print(bjp.get_name(), bjp.age)

class Person:
    def __hello(self):
        print('하위')
    def hi(self):
        self.__hello()
bjp = Person()
bjp.hi()

class Person:
    name =''
    def get_name(self):
        return self.name
bjp = Person()
bjp.name = 'park'
esther = Person()
esther.name = 'rucci'
print(esther.get_name())
print(bjp.get_name())
print(Person.name)

class Person:
    bag = []

    def put_bag(self, item):
        self.bag.append(item)
bjp = Person()
bjp.put_bag('candy')
esther = Person()
esther.put_bag('book')

print(bjp.bag)
print(esther.bag)

class Cal: #정적 메소드 굳이 인스턴스를 만들 필요없을때
    @staticmethod
    def add(a, b):
        print(a+b)
Cal.add(1,3)

class Person:
    count = 0
    def __init__(self):
        Person.count += 1
    @classmethod
    def print_count(cls):
        print('{}명 생성됨 ㅎ'.format(cls.count))
bjp = Person()
esther = Person() 88 33.5%
Person.print_count()'''

class Human: # 클래스
    def __init__(self, name, age, gender): # 생성자
        self.name = name
        self.age = age
        self.gender = gender
    def who(self): # 메소드
        print('이름 : {} 나이 : {} 성별 : {}'
              .format(self.name, self.age, self.gender))
    def setinfo(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def __del__(self): # 소멸자
        print("나의 죽음을 알리지마라")
# bjp = Human('범킹', 26, '남자') # 인스턴스

class Stock:
    def __init__(self, menu, code, PER, PBR, 배당):
        self.menu = menu
        self.code = code
        self.PER = float(PER)
        self.PBR = float(PBR)
        self.배당 = float(배당)
    def set_per(self, PER):
        self.PER = PER
    def set_pbr(self, PBR):
        self.PBR = PBR
    def set_dividend(self, 배당):
        self.배당 = 배당

한국금융지주 = Stock('한국금융지주', '071050', 6.58, 0.63, 0.0573)
print(한국금융지주.menu)
print(한국금융지주.code)
print(한국금융지주.PER)
print(한국금융지주.PBR)
한국금융지주.set_pbr(3.78)
print(한국금융지주.PBR)