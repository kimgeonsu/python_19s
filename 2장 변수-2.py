#2. 나중 날짜를 알랴주
day=int(input("오늘 요일을 입력하세요(월:0,화:1,수:2,목:3,금:4,토:5,일:6):"))
after=int(input("며칠 이후의 요일을 알고 싶나요?"))
nextday=(day+after)%7
print(after,"일 이후의 요일은", nextday,"입니다.")
