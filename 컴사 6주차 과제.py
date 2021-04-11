#p202.07
'''def score(x) :
    if x>=90 :
        print("A")
    elif 80<= x < 90 :
        print("B")
    elif 70<= x < 80 :
        print("C")
    elif 60<= x < 70 :
        print("D")
    else :
        print("F")

yourScore=int(input("점수를 입력하세요:"))
score(yourScore)'''

#p202.08
'''def evenodd(x) :
    if x%2 ==0 :
        print("짝수입니다.")
    else :
        print("홀수입니다.")

num=int(input("숫자를 입력하세요:"))
evenodd(num)'''

#227.09_for.ver
'''num=int(input("몇 단이 궁금한가요:"))
if 2<= num <=9 :
    for i in range(1, 10) :
        print("%d x %d = %d" %(num, i, num*i))
else :
    print("잘못된 값이 입력되었습니다.")
print("프로그램을 종료합니다.")'''

#227.09_while.ver
'''i=1
num=int(input("몇 단이 궁금한가요:"))
if 2<= num <=9 :
    while i<=9 :
        print("%d x %d = %d" %(num, i, num*i))
        i += 1
else :
    print("잘못된 값이 입력되었습니다.")
print("프로그램을 종료합니다.")'''

#228.14
suum=0
i=50
while i <=100 :
    if i%3 == 0 or i%5 ==0 :
        suum += i
        i += 1
    else :
        i += 1
print(suum)

