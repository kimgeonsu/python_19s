answer="1234" #답 변수

for k in range (0,10) :# 게임을 10번 반복
    num=str(input("4자리 숫자를 입력하세요:"))

    s=0#스트라이크 변수
    b=0#볼 변수

    for i in range (0,4) :#answer와 num의 인덱스를 비교하면서 i가 같고 숫자까지 같으면 strike
        if num[i] == answer[i] :
            s += 1

        else :
            for j in range (0,4) :#answer와 num의 인덱스를 비교하면서 숫자는 같지만 i가 다르면 ball
                if num[i]==answer[j] :
                    b += 1
    if s==4 :
        print("정답입니다.")
        break
    if s==0 and b==0 :
        print("아웃입니다.")
    else :
        print(s,"스트라이크", b, "볼 입니다.")
if k==9 or s==4 :
    print("게임을 종료합니다.")
    
