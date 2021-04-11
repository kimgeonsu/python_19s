import csv

f = open("Luggage.tsv", "r", encoding = "utf-8")
rdr = csv.reader(f, delimiter = "\t")
r= list(rdr)

high=[]
low=[]

for i in range(1, len(r)) :
      try :
            if  int(r[i][7]) >= 4 :
                  high.append(i)

            else 1<= int(r[i][7]) <=3 :
                  low.append(i)
      except IndexError :
            continue
      
highdic = {}
lowdic = {}

for num in high :
      word = r[num][13].split()
      for j in word :
            if j in highdic :
                  highdic[j] += 1

            else :
                  highdic[j] = 1


for num in low :
      word = r[num][13].split()
      for j in word :
            if j in lowdic :
                  lowdic[j] += 1

            else :
                   lowdic[j] = 1


shighdic = sorted(highdic.items(), key = lambda kv:  kv[1], reverse = True )
slowdic = sorted(lowdic.items(), key = lambda kv:  kv[1], reverse = True)


shighdic = shighdic[49:100]
slowdic = slowdic[49:100]

count = 50
for a in shighdic :
      print(count, a)
      count  += 1

count = 50
for b in slowdic :
      print(count, b)
      count += 1

f.close()
