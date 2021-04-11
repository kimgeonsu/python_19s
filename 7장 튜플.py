#dictionary.1.
'''def process(w) :
    output=""
    for ch in w :
        if( ch.isalpha() ) :
            output += ch
        return output.lower()
words= set()

fname=input("입력 파일 이름:")
file=open(fname, "r")

for line in file :
    lifewords=line.split()
    for word in linewords:
        words.add(process(word))

print("사용된 단어의 개수=", len(words))
print(words)'''

#
'''fname=input("파일 이름:")
file=open(fname,"r")

table=dict()
for line in file :
    words=line.split()
    for word in words :
        if word not in table :
            table[word]=1
        else :
            table[word] += 1
print(table)'''

#dictionary.2
'''num=input("문자열을 입력하시오:")
ref={"ABC":2, "DEF":3, "GHI":4, "JKL":5, "MNO":6, "PQRS":7, "TUV":8, "XWYZ":9}
for x in num :
    for key in ref :
        print(key)'''


#dictionary.3
'''
customer = {"1234" : "4567", "8910" : "1112"}
ID = input("무슨 비밀번호가 궁금하느냐:")

if ID in customer :
    print(customer[ID])

else :
    print("존재하지 않는 아이디입니다.")
'''

#dictionary.4
'''
phone = {}
while True :
    person = input("(입력모드) 이름을 입력하세요:")
    num = input("(입력모드) 전화번호를 입력하세요:")
    phone[person] = num

    if person == "" :
        break

while True :
    who = input("(검색모드) 이름을 입력하세요:")

    if who in phone or who2 in phone :
        print( "전화번호는", phnoe[who], "입니다.")
        break
    else :
        who2 = input("찾는 이름이 없습니다. 이름을 입력하세요:")
'''        
#1. birth
'''birth=int(input("생년월일을 입력하세요(예:20000412):"))
year=birth[0:4]
month=birth[5:6]
date=birth[7:8]
if year>2019 or month<1 or month>13 or date<0 or date>31 :
    print("올바른 생년월일이 아닙니다.")
else :
    print("올바른 생년월일입니다.")'''

#2.print reverse_via_reversed()
'''
s=input("문자열을 입력하시오:")
rs="".join(reversed(s))
print(rs)
'''
#2.print reverse_via_none_reverse()
'''s=input("문자열을 입력하시오:")
rs=""

for i in range(0, len(s)) :
    rs += s[len(s)-i-1]
print(rs)'''

#3.palindrome_via_reversed()
'''s=input("문자열을 입력하시오:")
rs="".join(reversed(s))
if s==rs :
    print("회문입니다.")
else :
    print("회문이 아닙니다.")'''

#3.palindrome_via_none_reversed()
'''s=input("문자열을 입력하시오:")
rs=""

for i in range(0,len(s)) :
    rs += s[len(s)-i-1]

if s==rs :
    print("회문입니다.")
else :
    print("회문이 아닙니다.")'''

#4.count_via_count()
'''s=input("문자열을 입력하시오:")
ocount=s.count("o")
print(ocount)'''

#4.count_via_none_count()
'''s = input("문자열을 입력하시오:")
ocount = 0
for i in s :
    if "o" == i :
        ocount += 1
print(ocount)'''

#5.how old are you?
'''
old=float(input("당신의 나이를 입력하세요:"))
while True :
    if old < 0 or old != int(old) :
        print("잘못된 나이입니다.")
        old=float(input("당신의 나이를 입력하세요:"))
    else :
        print("당신의 나이는 %d 이군요" %old)
        break
'''    
