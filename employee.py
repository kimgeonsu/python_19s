class Employee :
      emp_cnt = 0

      def __init__(self, name='Null', salary=0) :
            self.__name = name
            self.__salary = salary
            Employee.emp_cnt += 1

      def set_name(self, name) :
            self.__name = name

      def set_salary(self,salary) :
            self.__salary = salary

      def get_name(self) :
            return self.__name

      def get_salary(self) :
            return self.__salary

      def get_tot_cnt(self, emp_cnt) :
            return Employee.emp_cnt

Employees=[]


file=open("emp.txt.txt", "r")
emp=Employee.get_name
Employees.append(emp)
print(Employees)
