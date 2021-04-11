#tuple-1
'''
t1 =(1, 2, 3)
t2= (4,)
t3 = t1 + t2
print(t3)
'''

#set-1
'''
a= [1,1,1,2,2,3,3,3,4,4,5]
b=set(a)
print(b)
'''

#set-2
'''
a=set()
print(type(a))
'''

#
'''
def check_pal(s) :
      low = 0
      high = len(s) - 1

      while True :
            if low > high :
                  return True

            a = s[low]
            b = s[high]

            if a != b :
                  return False 

            low += 1
            high -= 1

s = input("문자열을 입력하시오:")
s = s.replace("  ", " ")

if(check_pal(s) == True) :
      print("회문입니다.")

else :
      print("회문이 아닙니다.")
'''
#class.1

class Calculator :
      def __init__ (self) :
            self.value = 0

      def add(self, val) :
            self.value += val
'''
class UpgradeCalculator(Calculator) :
      def minus(self, val) :
            self.value -= val

cal=UpgradeCalculator()
cal.add(10)
cal.minus(7)

print(cal.value)
'''
#class.2

class MaxLimitCalculator(Calculator) :
      def add(self, val) :
            self.value += val
            if self.value > 100 :
                  self.value = 100
            else :
                  return self.value
            
cal = MaxLimitCalculator()
cal.add(50)
cal.add(60)
print(cal.value)
