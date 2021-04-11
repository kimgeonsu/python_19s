#1.
'''print(dir(list()))'''

#10
'''import os
for file in os.listdir(".") :
      print(file)'''

#2
'''
stat = input("수식을   입력하세요 : " )
print(eval(stat))
'''

#3
'''
n= exec((input("코드를 입력하세요"))
'''

#4.
'''
import sys

print(sys.path)
print("-------------------------")
print(sys.prefix)
'''

#5
'''
import random

n=[]

for i in range(10) :
      num=random.randrange(0, 100)
      n.append(num*(-1))

print(sorted(n, key=abs))
'''

#6
'''
class Person(object) :
      def __init__(self, name, age) :
            self.name = name
            self.age = age

      def __repr__(self) :
            return"<이름 : %s, 나이 : %s>" %(self.name, self.age)

def keyAge(person) :
            return person.age

people = [Person("홍길동", 20), Person("김철수", 35), Person("최자영", 38)]
print(sorted(people, key = keyAge))
'''

#7
'''
class Circle :
      def __init__(self, radius) :
            self.__radius = radius


      def __add__(self, other) :
            return Circle(self.__radius + other.__radius)

      def __lt__(self, other) :
            return self.__radius < other.__radius

      def __gt__(self, other) :
            return self.__radius > other.__radius

      def __str__(self) :
            return "원의 반지름은"+str(self.__radius)+ "입니다."

c1 = Circle(4)
c2 = Circle(5)
c3 = c1 + c2

print(c3)

if c1 < c2 :
      print("c1이 c2보다 작습니다.")

else :
      print("c1이 c2보다 큽니다")

if c2 > c3 :
      print("c2 이 c3보다 큽니다.")

else :
      print("c2 이 c3보다 작습니다.")
'''
#8
'''
class Fiblterator :
      def __init__(self, a=1, b=0, maxValue = 50) :
            self.a = a
            self.b = b
            self.maxValue = maxValue

      def __iter__(self) :
            return self

      def __next__(self) :
            n = self.a + self.b
            if n > self.maxValue :
                  raise StopIteration()
            self.a = self.b
            self.b = n
            return n

for i in Fiblterator() :
      print(i, end = " ")
'''
