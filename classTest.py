class Person:
    cnt = 0
    def __init__(self, name, age):
        self._name = name
        self._age = age
        Person.cnt+=1
        self.No = 'PE'+str(Person.cnt)

    def setName(self, name):
        self._name = name

    def getName(self):
        return self._name

    def setAge(self, age):
        if age >= 65:
            return
        self._age = age

    def getAge(self):
        return self._age

    def show(self):
        print("No : {} name : {} age : {}".format(self.No, self._name, self._age))

    # def __str__(self):
    #     return "name : {} age : {} phone : {}".format(self.__name, self.__age)


class Employee(Person):
    def __init__(self, name, age, company, cID, phone):
        super().__init__(name, age)
        self.__company = company
        self.__cID =cID
        self.__phone=phone
        self.No = 'EM'+str(Person.cnt)

    def setCompany(self, com):
        self.__company = com

    def getCompany(self):
        return self.__company

    def show(self):
        print("No : {} name : {} age : {}  company : {} phone : {}".format(self.No, self._name, self._age, self.__company, self.__phone))

class Teacher(Person):
    def __init__(self):
        self.__school = ''
        self.__sID =''
        self.__phone=''


# PE1
# EM2
# TE9

print(Person.cnt)
p1 = Person('park',  35)
e1 = Employee('song',  35, 'samsung', 's111','010-1114-1111')
print(Person.cnt)
e2 = Employee('lee',  25, 'samsung', 's1123','010-4444-5511')
p2 = Person('choi',  45)

p1.show()
e1.show()
e2.show()
p2.show()
print(Person.cnt)

# member = []
#
# member.append(Employee('song',  35, 'samsung', 's111','010-1114-1111'))
# member.append(Teacher('song',  35, 'samsung', 's111','010-1114-1111'))
# member.append(Employee())
# member.append(Teacher())
# member.append(Employee())
# member.append(Teacher())

# member[0].show()


# p1 = Employee()
# p2 = Teacher()


# print(Person.cnt)
# p2 = Person('song',  35, '010-1114-1111')
# print(Person.cnt)
#
# print(p2.cnt)
#
# p3 = Person('lee',  38, '010-1666-1111')
# p4 = Person('choi',  25, '010-1166-1111')
#
# print(p2.cnt)
# print(Person.cnt)
#
# print(p2)
# print(p3)
# print(p4)
