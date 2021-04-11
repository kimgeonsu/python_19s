#1. cunter class
'''class Counter :

    def reset(self) :
        self.count = 0

    def increment(self) :
        self.count += 1

    def get(self) :
        return self.count

#1. 객체 생성
a= Counter()

a.reset()
a.increment()

print("카운터 a의 값은", a.get())'''

#2. bank acoount
'''class bankAccount:

    def __init__(self):
        self.__balance = 0

    def withdraw(self, amount) :
        self.__balance -= amount
        print("통장에 ",amount, "가 입금되었음")
        return self.balance

    def deposit(self, amount) :
        self.__balance += amount
        print("통장에서 ", amount, "가 출금되었음")
        return self.__balance

a=bankAccount()
a.deposit(100)
a.withdraw(10)'''

#3. class Dog
'''class Dog :

      def ear(self) :
            print("귀를 쫑긋한다.")

      def mouth(self) :
            print("멍멍 짖는다.")

      def paw(self) :
            print("뒹군다.")

d= Dog()
d.ear()'''

#4. class ScoreManager

class classScoreManager :
      def __init__(self) :
            self.score = []
            self.stu = 0

      def add(self, s) :
            self.score.append(s)
            self.stu += 1
            return self.stu
      
      def average(self) :
            return sum(self.score)/self.stu


a = classScoreManager()

while True :
      n = int(input("메뉴를 입력하세요:"))
      if n == 1 :
            while True :
                  sc = int(input("성적을 입력하세요. (종료는 -1) :"))

                  if sc == -1 :
                        break
                  a.add(sc)
                        


      if n == 2 :
            print("평균점수는",a.average(), "점 입니다.")

      if n == 3 :
            print("학생수는:", a.stu, "명 입니다.")

