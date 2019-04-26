#2.두 점 사이의 거리 구하기
'''import math as m
x1=int(input("x1="))
y1=int(input("y1="))
x2=int(input("x2="))
y2=int(input("y2="))

dist= m.sqrt((x2-x1)**2+(y2-y1)**2)
print(dist)'''

#3.4자리 정수의 각 자리수 합 구하기
num=int(input("4자리 정수를 입력하시오:"))
a=int(num/1000)
b=int(num%1000/100)
c=int(num%100/10)
d=int(num%10)
sum=a+b+c+d
print(sum)
