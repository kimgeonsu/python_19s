#1. center letter
'''s=input("어떤 문자열의 중앙글자가 궁금하느냐:")
if len(s)%2 == 0 :
    cs1=s[len(s)//2]
    cs2=s[(len(s)//2)-1]
    print(cs1)
    print(cs2)
else :
    cs1=s[len(s)//2]
    print(cs1)'''

#2. abs
'''num=int(input("숫자를 입력하세요:"))
if num <0 :
    print(-1*num)
else :
    print(num)'''

#3. 2와 3의 공배수인가?
'''num=int(input("숫자를 입력하세요:"))
if num %2 ==0 and num%3==0 :
    print("2와 3의 공배수입니다.")
else :
    print("2와 3의 공배수가 아닙니다.")'''

#4. 상품권을 주자
'''price=int(input("구매금액을 입력하세요(만원):"))
if price <10 :
    print("상품권 5천원이 지급됩니다.")
elif 10 <= price < 30 :
    print("상품권 1만원이 지급됩니다.")
else :
    print("상품권 5만원이 지급됩니다.")'''

#5. 배송료
country=input("배송할 나라:")
city=input("배송할 도시:")
if country != "한국" :
    print("배송료는 20000원입니다.")
elif country=="한국" and city == "제주시" :
    print("배송료는 10000원입니다.")
else :
    print("배송료는 5000원입니다.")
