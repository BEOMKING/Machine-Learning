# globals(), locals()
# Call by value : 변수를 복사한 값을 전달하는 방식
# 예를 들어 변수 a가 있고 함수 def1가 있을 때,
# def1(a)에서 전달받은 a는 a 자체(주소 값)가 아니라 a의 복사 값, 레플리카
# 따라서 함수 내에서 해당 인자를 조작하여 바꾸었다고 해도 원본 변수 a는 변하지 않는다.
# 원본을 건드리지 않아 안전하지만, 함수의 사용으로 해당 전역 변수를 바꾸고 싶을
# 때는 리턴 값을 다시 전역 변수로 집어넣어야 하는 번거로움과 시간 사용의 단점
# Call by reference : 인자로 받은 변수의 주소 값을 전달하는 것
# 함수의 인자를 받을 때, 변수가 가리키는 주소 값을 전달한다.
# 예를 들어 변수 a가 있고 함수 def2가 있을 때,
# def2(a)에서 전달받은 a는 원본 전역 변수 a의 주소 값이다.
# 따라서 함수 내에서 해당 인자를 조작하면 원본 변수의 주소 값으로 타고 들어가 해당 값 자체를 바꿔버린다.
# 이를 통해 전역 변수의 즉각적 변경이 가능하지만, 부주의하면 변수를 잘못 조작해 프로그램에 문제를 야기할 수 있다.
# Call by objective
# python은 모든 것을 "객체"로 판단한다
# python에서 변수는 위에서처럼 특정 메모리 공간을 할당받은 컨테이너 개념이
# 아니라, 어떤 객체에 붙여진 이름표일 뿐이다.
'''물건에는 위치가 존재할 수 있다. 예를 들어 알파카 인형을 합정역 31번 사물함에 숨겨뒀다면
"알파카 인형"은 객체, "합정역 31번 사물함"은 알파카 인형의 위치, 즉 주소 값이 된다.
그러나 알파카 인형에 붙여진 이름표, 즉 변수에 대해서도 위치(주소값)를 지정해 두지는 않는다.
"알파카 인형"에는 여러 가지 이름표(변수)가 붙어있을 수도 있다.

예를 들어 해당 인형에 "귀여운 동물", "복학생 아싸"등의 여러 이름표가 붙어있다고 하자.

이때 변수"귀여운 동물"의 주소 값(위치)과 변수"복학생 아싸"의 주소 값(위치)은 객체"알파카 인형"의 주소 값(위치)으로 같다.
python에서는 global인지 local인지 영역에 따라 변수들의 정보를 저장하는 namespace가 따로 있다.

즉, 전역 변수를 함수에서 인자로 받아오더라도 함수 내에서는 지역변수(이름표)에 불과하다.

함수 내에서 이름표를 떼서 다른 객체에 붙인다고 하더라도,

그 이름표는 함수 내에서만 사용하는 이름표일 뿐이다.
결국 함수 호출이 끝나면 전역 변수(이름표)가 여전히 그 객체에 붙어있다.
예를 들어 list 1 = [1,2,3,4] 일 때,
함수 내에서 list 1을 [5,6,7,8]이라는 새로운 객체랑 binding 한다고 해도
함수 호출이 끝나면 list 1은 그대로 [1,2,3,4]이다.
의할 점은
이름표(변수)만 떼고 붙이는 것이 아니라, 이름표가 붙여진 물건(객체)의 구성품을 직접 조작하는 경우이다.
예를 들어 위의 예시와 같이 list 1 = [1,2,3,4] 일 때,
함수 내에서 list 1이라는 이름표가 붙여진 객체 [1,2,3,4]에 대하여
list 1 [0] = 5
이와 같이 객체 내의 요소(element)를 조작할 수 있다.
이 경우에 함수의 호출이 끝나서 지역 이름표가 전역 이름표로 바뀐다고 하더라도
객체가 변한 상태이므로 list 1은 [5,2,3,4]가 된다.
"복학생 아싸" 이름표가 붙은 알파카 인형의 털을 초록색으로 염색했다면
"귀여운 동물" 이름표가 붙은 알파카 인형의 털도 초록색인 게 당연하지 않겠는가?
(하나의 알파카 인형에 두 개의 다른 이름표가 붙어있으므로)
이때, 객체 자체를 바꾸려면 당연히 객체가 mutable, 즉 가변적인 포맷이어야 한다.
mmutable 한 포맷의 객체(tuple 등)는 변경할 수 없지만,
imutable한 포맷의 객체(list, dictionary, 직접 만든 클래스 등)는 변경할 수 있다는 특성을 갖는다.'''
# a = [10]
#
# def my_fun(a):
#     a[0] = a[0] + 10
# names = ['kang', 'hong', 'kim']
# student_names = names
# student_names[0] = 'lee'
# print(student_names)
# print(names)
# print(names is student_names)
# print(id(names), id(student_names))

arrays = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

import numpy as np

#shift  alt e 한줄 실행
# numby 파이썬으로 과학 연산을 쉽고 빠르게 해주는 패키지
# 배열 : 순서가 있는 같은 종류의 데이터가 저장된 집합
#시퀀스 데이터를 이용한 ndarray 생성

data2 = [[1, 2, 3], [4, 5, 6]]
arr2 = np.array(data2)
arr2

data3 = [1, 2, 2, 3, 3, 3]
arr3 = np.array(data3)
arr3

a = np.ones((3, 4))
b = np.empty((3, 4))
c = np.full((3, 4), 3)
d = np.zeros((2, 3, 2))
e = np.eye(5)
f = np.linspace(1, 10, 3)
arr3_num = arr3.astype(int)
print(arr3_num.dtype)

np.random.rand(4, 5, 3) # 0 ~ 1 (개수, 행, 열)
np.random.randint(1, 100, size=(3, 5)) # 정수 (범위, 범위, 크기(행, 열)
# seed 랜덤한 값을 동일하게 다시 생성할 때
np.random.seed(24)
print(np.random.randn(3, 4))
# choice 주어진 1차원 ndarray로부터 랜덤으로 샘플링
sample_data = np.array([10, 20, 30, 40, 50])
np.random.choice(sample_data, size=(2, 3))
np.random.choice(46, size=(6,), replace=False)
np.random.uniform(1, 0, 3, 0, size=(4, 5))
np.random.normal(size=(3, 4))
np.random.randn(3, 4)
np.random.randn(3, 4)

arr1 = np.array([10, 20, 30, 40])
arr2 = np.array([1, 2, 3, 4])
arr1 + arr2
arr3 = np.arange(15).reshape(3, 5)
arr3
arr4 = np.random.rand(15).reshape(3, 5)
arr4
arr3 + arr4
np.multiply(arr3, arr4)

np.sum(arr1)
np.cumsum(arr1)
arr5 = np.random.randn(5)
np.any(arr5 > 0)
np.all(arr5 > 0)
# where 조건에 따라서 선별적으로 값을 선택
np.where(arr5 > 0, arr5, 0)

arr2 = np.arange(10).reshape(2, 5)

arr9 = np.arange(36).reshape(6, 6)
arr9
arr9[1:4, 1:3]
arr9[2, 3:-4]

#indexing, slicing
a1 = np.array([1, 3, 4, 5, 6, 6])
a1[[1, 2, 4]]
arr9[1:4, 1:3]
arr9[1][0:2]
# ndarry의 shape 변경 방법
# ravel 파라미터 order 'C' 행우선 'F' 열 우선
np.ravel(arr9, order='F')

# axis
np.sum(arr9, axis=0) #세로합 =1 가로합

zero = np.zeros(20) # 1
zero
four = np.arange(16).reshape(4,4) # 2
four
ten = np.arange(1, 11) # 4
ten
idenmatrix = np.eye(4) # 6
idenmatrix
three = np.random.randn(3, 3, 3) # 7
three
np.max(three) # 8
np.min(three)
ran20 = np.random.rand(20)
np.mean(ran20) # 9
four10 = np.ones((4,4)) # 10
four10[1:3, 1:3] = 0
four10