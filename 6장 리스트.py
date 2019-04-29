#1
'''mylist=[1,2,3,4,5,6]
print(mylist[0])#a
print(mylist[1:5])#b
print(max(mylist))#c
print(min(mylist))#d
print(sum(mylist))#e
print(mylist[-2])#f'''

#2
shopping_list=["apple","blueberry","peach"]

'''shopping_list.append("melon")'''
'''shopping_list.pop(3)'''
'''shopping_list.insert(0,"melon")'''
'''shopping_list.pop(0)'''
'''shopping_list.pop(1)
print(shopping_list)'''

#3
'''customer=[]
for i in range(5) :
    customer.append(input("고객명:"))
customer1=sorted(customer)
print(customer1)'''

#4-1
'''customer=[]
for i in range(5) :
    customer.append(input("고객명:"))
customer.sort()
customer.reverse()
print(customer)'''

#4-2
'''def reverselist(list1) :
    list1=[]
    list1.sort()
    for i in range(5) :
        list1.append(list1[-i])
    return 0
    
customer=[]
for i in range(5) :
    customer.append(input("고객명:"))
print(reverselist(customer))

#5
'''scorelist=[]
suum=0
student=0
for i in range(5) :
    score=int(input("성적:"))
    scorelist.append(score)
    suum += score

avg=suum/5
for i in range(5) :
    if scorelist[i] > avg :
        student += 1
print(student)'''


