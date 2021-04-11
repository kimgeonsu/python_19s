# 5x5 빙고 게임
import random
board=[[' ' for x in range(1,6)] for y in range(5)]
n=1
for r in range(5) :
      for c in range(5) :
            board[r][c]=n
            n += 1
numlist=[]
comlist=[]
bingo=0

#빙고판 만들기
while True :

      for r in range(5) :
            for c in range(5) :
                  print("{:>3}" .format(board[r][c]),end=" ")
            print()


#사용자로부터 숫자 입력 받기
      num=int(input("번호를 선택하세요:"))
      numlist.append(num)


#잘못된 위치 확인하기
      if num < 1 or num > 25 :
            print("잘못된 위치입니다.")

      elif num in comlist  :
            print("이미 선택된 숫자입니다.")
            continue
      


#위치 맞을 시 숫자 X로 변환 
      else :
            for r in range(5) :
                  for c in range(5):
                        if board[r][c] == num :
                              board[r][c]='X'


#컴퓨터가 숫자 고르기
      com=random.randint(1,25)
      comlist.append(com)
      if com  not in numlist :
            for r in range(5) :
                  for c in range(5) :
                        if board[r][c] == com :
                              board[r][c] ='O'

            

#빙고  체크                              
      for i in range(5) :
            if board[i][0] == board[i][1] == board[i][2] == board[i][3] == board[i][4] :
                  print("빙고!")
                  bingo += 1
      for i in range(5) :
            if board[0][i] == board[1][i] == board[2][i] == board[3][i] == board[4][i] :
                  print("빙고!")
                  bingo += 1
            
      if board[0][0] == board[1][1] == board[2][2] == board[3][3] == board[4][4] :
            print("빙고!")
            bingo += 1
                  
      elif board[0][4] == board[1][3] == board[2][2] == board[3][1] == board[4][0] :
            print("빙고!")
            bingo += 1
#빙고하면 게임 종료!
      if bingo == 1 :
            break
            
print("게임을 종료합니다.")
