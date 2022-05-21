#singal inheritance
'''class Company:
    def accept(self,name):
        self.name=name
    def display(self):
        print(self.name)

class Manager(Company):
    def accept1(self,eid,ename):
        self.eid=eid
        self.ename=ename
    def display1(self):
        print("id is ",self.eid,"Name is",self.ename)

obj=Company()
obj.accept("kangaroo")
obj.display()

obj1=Manager()
obj1.accept("kangaroo")
obj1.accept1(1001,"ABC")
obj1.display()
obj1.display1()



class Company:
    def accept(self):
        self.cid=1001
        self.companyname="xyz INC"
    def display(self):
        print("Company id is"+str(self.cid))
        print("company name is"+str(self.companyname))

class Manager(Company):
    def accept1(self,sal):
        self.sal=sal
    def display1(self):
        print("Salary is"+str(self.sal))
obj=Manager()
obj.accept()
obj.accept1(15000)
obj.display()
obj.display1()
# multilavel inheritance
class Company:
    def accept(self,name):
        self.name=name
    def display(self):
        print(self.name)
class Manager(Company):
    def accept1(self,eid,ename):
        self.eid=eid
        self.ename=ename
    def display1(self):
        print("id is",self.eid,"name is ",self.ename)

class Developer(Manager):
    def accept2(self,salary):
        self.salary=salary
    def display2(self):
        print("salary is",self.salary)
obj1=Manager()
obj1.accept("kangaroo")
obj1.accept1(1001,"ABC")
obj1.display()
obj1.display1()

obj2=Developer()
obj2.accept("kangaroo")
obj2.accept1(1001,"MNB")
obj2.accept2(45000)
obj2.display()
obj2.display1()
obj2.display2() 

class Company:
    def accept(self):
        self.cid=1001
        self.companyname="xyz inc"

    def display(self):
        print("company id is"+str(self.cid))
        print("Company name is"+str(self.companyname))
class Manager(Company):
    def accept1(self,sal):
        self.sal=sal
    def display1(self):
        print("salary is"+str(self.sal))

class Employee(Manager):
    def accept2(self,bonus):
        self.bonus=bonus
    def display2(self):
        print("Bonus is"+str(self.bonus))
obj= Employee()
obj.accept()
obj.accept1(15000)
obj.accept2(1200);
obj.display()
obj.display1()
obj.display2() ''' 
class Company:
    def accept(self,name):
        self.name=name
    def display(self):
        print(self.name)
class Manager(Company):
    def accept1(self,eid,ename):
        self.eid=eid
        self.ename=ename
    def display1(self):
        print("id is",self.eid,"name is",self.ename)
class Developer(Company):
    def accept2(self,salary):
        self.salary=salary
    def display2(self):
        print("salary is",self.salary)

obj1=Manager()
obj1.accept("kangaroo")
obj1.accept1(1001,"ABC")
obj1.display()
obj1.display1()
obj2=Developer()
obj2.accept("kangaroo")
#obj2.accept(1002,"mno1")
obj2.accept2(45000)
obj2.display()
#obj2.display1()
obj2.display2()
















