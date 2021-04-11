#6-1
'''scores=[]
for i in range(10) :
    scores.append(int(input("성적을 입력하시오:")))
print(scores)'''

#6-2
'''scores=[]
high=0
s=int(input("학생수:"))
stusum=0
for i in range(s) :
    score=int(input("성적을 입력하시오:"))
    scores.append(score)
    stusum += score
stuavg=stusum/s
print(stuavg)
for j in range(len(scores)) :
    if scores[j] >=  80 :
        high += 1
print(high)'''

#6-3
name=[]
while True :
    dog=input("이름:")
    
    if dog=="":
        break
    name.append(dog)
print(name)        
