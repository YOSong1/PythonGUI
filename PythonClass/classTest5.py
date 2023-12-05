
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
        print("No : {0:5s} name : {1:10s} age : {2:3d}".format(self.No, self._name, self._age))

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
        print("No : {0:5s} name : {1:10s} age : {2:3d}  company : {3:10s} phone : {4:12s}".format(self.No, self._name, self._age, self.__company, self.__phone))

class Teacher(Person):
    def __init__(self, name, age, school, sID, phone):
        super().__init__(name, age)
        self.__school = school
        self.__sID =sID
        self.__phone=phone
        self.No = 'TE' + str(Person.cnt)

    def setSchool(self, school):
        self.__school = school

    def getSchool(self):
        return self.__school

    def show(self):
        print("No : {} name : {} age : {}  school : {} phone : {}".format(self.No, self._name, self._age, self.__school, self.__phone))



class PersonManager:
    memberdict = {}

    def mainMenu(self):
        print('1. 멤버 추가')
        print('2. 멤버 출력')
        print('3. 검색(No)')
        print('4. 삭제(No)')
        print('5. 정렬')
        print('0. 종료')

    def memberInput(self):
        print("1. 일반인")
        print("2. 회사원")
        print("3. 선생님")
        print("종류 : ", end='')
        m1 = int(input())

        if m1 == 1:
            print("멤버 입력")
            name = input('이름 : ')
            age = int(input('나이 :'))
            tmp = Person(name, age)
            self.memberdict[tmp.No] = tmp
        elif m1 == 2:
            print("멤버 입력")
            name = input('이름 : ')
            age = int(input('나이 :'))
            com = input("회사명 :")
            cid = input("사번 :")
            phone = input("전화 : ")
            tmp = Employee(name, age, com, cid, phone)
            self.memberdict[tmp.No] = tmp

    def memberSelectAll(self):
        for k, p in self.memberdict.items():
            p.show()

    def memberSearch(self):
        print("검색 No 입력")
        id = input('No : ')
        for k, p in self.memberdict.items():
            if k == id:
                p.show()

    def memberDelete(self):
        print("삭제 No 입력")
        id = input('No : ')
        delk = ''
        for k, p in self.memberdict.items():
            if k == id:
                print("삭제 멤버 정보")
                p.show()
                delk = k
                break
        if delk != '':
            self.memberdict.pop(k)
        else:
            print("해당 멤버 정보가 없습니다.")

    def memberSort(self):
        print("정렬 기준")
        print("1. 이름")
        print("2. 나이")
        print("기준 : ", end='')
        m1 = int(input())

        if m1 == 1:
            tmp = list(self.memberdict.values())
            tmp.sort(key=lambda p: p.getName())

            for t in tmp:
                t.show()

        elif m1 == 2:
            tmp = list(self.memberdict.values())
            tmp.sort(key=lambda p: p.getAge())

            for t in tmp:
                t.show()





def main():
    pm = PersonManager()
    while (True):
        pm.mainMenu()
        print('메뉴 선택 : ', end='')
        menu = int(input())

        if menu == 0:
            break

        if menu == 1:
            pm.memberInput()
        elif menu == 2:
            pm.memberSelectAll()
        elif menu == 3:
            pm.memberSearch()
        elif menu == 4:
            pm.memberDelete()
        elif menu == 5:
            pm.memberSort()


main()


