#삼각형_넓이_구하기
'''def s(x,y) :
    s=x*y*1/2
    return s

w=float(input("밑변의 길이:"))
h=float(input("높이의 길이:"))

ss=s(w,h)
print("삼각형의 넓이:" ,ss)'''


#n부터_m까지_더하기_for문
'''n=int(input("시작:"))
m=int(input("끝:"))
suum=0
for i in range(n, m+1, 1) :
    suum += i
print("%d부터 %d까지의 합은 %d 입니다." %(n,m,suum)'''


#n부터_m까지_더하기_while문
'''n=int(input("시작:"))
m=int(input("끝:"))
x=n
suum=0
while x<= m:
    suum += x
    x += 1
print(suum)'''


#펙토리얼_계산
'''n=int(input("정수를 입력하세요:"))

fact=1
for i in range(1, n+1) :
    fact *= i
print(fact)'''


#펙토리얼_계산_함수버전+무한루프
'''def fac(a) :
    fact=1
    for i in range(1, n+1) :
        fact *= i
    return fact

while 1 :
    n=int(input("정수를 입력하세요:"))
    if n <= 0 :
        break
    print(fac(n))'''


#369게임
'''import time
n=1
print("369게임 시작")
while n <= 20 :
    if "3" in str(n) or "6" in str(n) or "9" in str(n) :
        print("박수")
    else :
        print(n)
    n += 1
    time.sleep(0.7)
print("369게임 끝")'''


#홀수만_더하기
'''n=int(input("몇까지 더할까여:"))
suum=0
for i in range (0, n+1) :
    if i%2 == 0 :
        suum += 0
    else :
        suum += i

print(suum)'''




