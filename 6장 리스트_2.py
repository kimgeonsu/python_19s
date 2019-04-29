#7.TIK/TAE/TOE
board=[[''for x in range(3)]for y in range(3)]
while True :
    for r in range(3) :
        print("   "+ board[r][0]+ "|  "+ board[r][1]+ " |"+ board[r][2])
        if (r != 2) :
            print("---|---|---")
            
    x=int(input("다음 수의 x좌표를 입력하시오:"))
    y=int(input("다음 수의 y좌표를 입력하시오:"))

    if board[x][y] !='' :
        print("잘못된 위치입니다.")
        continue
    else : 
        board[x][y]='X'

    done=False
    for i in range(3) :
        for j in range(3) :
            if board[i][j] == ''and not done :
                board[i][j]='O'
                done=True
                break

#6.주사위_던지기
'''import random 
a=0
b=0
c=0
d=0
e=0
f=0
numlist=[]
for i in range(600) :
    numlist.append(random.randint(1,6))
    for j in numlist :
        if j==1 :
            a += 1
        elif j==2 :
            b +=1
        elif j==3 :
            c +=1
        elif j==4 :
            d +=1
        elif j==5 :
            e +=1
        else :
            f +=1
print("주사위가 1인 경우는 %d 번" %a)
print("주사위가 2인 경우는 %d 번" %b)
print("주사위가 3인 경우는 %d 번" %c)
print("주사위가 4인 경우는 %d 번" %d)
print("주사위가 5인 경우는 %d 번" %e)
print("주사위가 6인 경우는 %d 번" %f)
print(numlist)'''
