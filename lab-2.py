# Lab no. - 2 
# date - 02/02/2026


class students:
    def data(self):
        self.name=input("Enter your name: ")
        self.age=int(input("Enter your age: "))
    def display(self):
        print(self.name)
        print(self.age)

s1=students()
s1.data()
s1.display()

class faculty:
    def data(other):
        other.lecture=input("which lecture?")
    def display(others):
        print(others.lecture)

s2=faculty()
s2.data()
s2.display()

class student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        print(self.name)
        print(self.age)
s1=student("joy",999)
s2=student("ro",578)
s3=student("rock",8348)
s4=student("fjhj",3862)
s5=student("jhfjd",348)

class faculties:
    def __init__(nss,name,subject,salary,gm):
        nss.name=name
        nss.subject=subject
        nss.salary=salary
        nss.gm=print("good morning ")
        print(nss.name)
        print(nss.subject)
        print(nss.salary)
s1=faculties("jkfgj", "hdjhf",67546358)
s2=faculties("jkfgj", "hdjhf",67546358)
s3=faculties("jkfgj", "hdjhf",67546358)


class faculties:
    def __init__(nss,name,subject,salary):
        nss.name=name
        nss.subject=subject
        nss.salary=salary
    def display(nss):
        print(nss.name)
        print(nss.subject)
        print(nss.salary)
    def greet(nss):
        print("welcome",nss.name)
s1 = faculties("fhjfh","jhdgjh",47875)
print(s1.name)

class Add:
    def __init__(addd,m,n):
        addd.m=m
        addd.n=n
        print(addd.m+addd.n)

s1=Add(4,6)
