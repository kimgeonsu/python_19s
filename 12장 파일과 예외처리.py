#1
'''
outfile = open("phones.txt", "w")

outfile.write("홍길동 010-1234-5678\n")
outfile.write("김철수 010-1234-5679\n")
outfile.write("김영희 010-1234-5680\n")

outfile.close()
'''

#2-1
'''
infile = open("phones.txt", "r")

for line in infile.readlines() :
      print(line)

infile.close()
'''

#2-2
'''
infile = open("phones.txt" , "r")

for line in infile.readlines() :
      print(line.strip())

infile.close()
'''

#3
'''
import os.path

outfile = open("todo.txt", "w")

if os.path.isfile("todo.txt") :
      print("동일한 이름의 파일이 이미 존재합니다.")

else :
      outfile.write("파이썬 프로그래밍")
      outfile.write("자료구조")
      outfile.write("네트워크 프로그래밍")

outfile.close()
'''

#4
'''
infile = open("marry.txt", "r")
freqs = {}

for line in infile :
      for word in line.split() :
            if  word in freqs :
                  freqs[word] += 1

            else :
                  freqs[word] = 1

print(freqs)
infile.close()
'''
#5
'''
import pickle


pickle.dump(freqs, open("save.p", "wb"))

myfreqs = pickle.load(open("save.p","rb"))
print(myfreqs)
'''
#6
'''
so= sorted(myfreqs.items(), key = lambda kv:  kv[1], reverse = True)
print(so)
'''
#7
'''
while True :
      try :
            fname = input("입력 파일 이름 :")
            infile = open(fname,"r")
            break
      except IOError :
            print("파일" + fname + "이 없습니다. 다시 입력하시오.")

print("파일이 성공적으로 열렸습니다.")
'''
#8
'''
import pickle

sum = 0
n=0

infile = open("data.txt", "r")

for line in infile :
      sum += float(line)
      n += 1

average = sum/n
sa={"sum:":sum, "average:":average}

pickle.dump(sa,open("output.txt","wb"))
myout = pickle.load(open("output.txt","rb"))
print(myout)  
'''
