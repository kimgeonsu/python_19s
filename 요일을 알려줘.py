days=['월:','화','수','목','금','토','일']
now=int(input('오늘은 무슨 요일?:'))
wanna=int(input('며칠 뒤의 요일을 알고싶나요?'))
nextday=(now+wanna)%7
print(days[nextday])
