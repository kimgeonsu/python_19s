answer=1234#답 변수

answer2=[answer//1000, (answer%1000)//100, (answer%100)//10, answer%10]
#답 변수를 인덱스로 스트링화
for k in range(0,10):#게임을 10번 반복

    num=int(input("4자리 숫자를 입력하세요:"))
    a=num//1000
    b=(num%1000)//100
    c=(num%100)//10
    d=num%10

    index=[a, b, c, d]#입력 숫자 변수를 인덱스로 각 숫자 쪼개기

    s=0#스트라이크 변수
    b=0#볼 변수

    for i in range(0,4) :#index와 answer2의 인덱스를 비교하면서 i가 같고 숫자까지 같으면 strike
        
        if index[i] == answer2[i] :
            s += 1
        else :
            for j in range(0,4) :
                if index[i] == answer2[j] :#index와 answer2의 인덱스를 비교하면서 숫자는 같지만 i가 같지 않으면 ball
                    b += 1

    if s == 4:
        print("정답입니다.")
        break
    if s == 0 and b == 0 :
        print("아웃입니다.")
    else :
        print(s, '스트라이크', b, '볼 입니다.')

if k == 9 or s ==4 :
    print("게임을 종료합니다.")
    
