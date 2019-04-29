#1. print even_ver_if
'''for i in range(1,101) :
    if i%2 == 0 :
        print(i, end=" ")'''

#1. print even_ver_none_if
'''for i in range(2, 101, 2) :
    print(i, end=" ")'''

#2. 복리이자율
'''mymoney=10000000
year=0
while mymoney<= 20000000 :
    mymoney += mymoney*0.07
    year += 1
print(year)'''

#3. 구구단
'''for i in range(1, 10) :
    for j in range(1, 10) :
        print (i*j ,end=" ")'''

#4. factorial_ver_for
'''n=int(input("몇 팩토리얼이 궁금하느냐:"))
for i in range(1, n) :
    n *= i
print(n)'''

#4. factorial_ver_while
'''n=int(input("몇 팩토리얼이 궁금하느냐:"))
fac=1
i=1
while i <= n :
    fac *= i
    i += 1
print(fac)'''

#5. dec to bin
n=int(input("이진수로 변환시킬 십진수를 입력하시오:"))
bi=""

while n > 1 :
    rest = n%2
    n = n//2
    bi= str(rest) +bi
bi=str(n) + bi
print(bi)

#6. 최대공약수
'''x=int(input("x:"))
y=int(input("y:"))
a=[]
for i in range(1, max(x,y)) :
    if x%i == 0 and y%i ==0 :
        a.append(i)
print("최대공약수는", max(a),"입니다.")'''
    

#7. quiz
'''a=int(input("87+36의 값은?"))
while True :
    if a==123 :
        print("맞았습니다.")
        break
    else :
        print("틀렸습니다.")
        a=int(input("87+36의 값은?"))'''
