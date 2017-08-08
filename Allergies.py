"""Cerner Interview Question.
Design Allergy class """

import datetime
class Pers():

    def __init__(self,name, bdate, houseno, street, city, state, ziip, number):
        try:
            self.__name = name
            if not name.isalpha():
                raise ValueError

            y, m, d = map(int,bdate.split('/'))
            self.__bdate = datetime.date(y, m, d)
            #print self.__bdate
            self.__add = Addrs(houseno, street, city, state, ziip)
            self.__number = int(number)

        except ValueError:
            print('Sorry I dont understand name or number ')

    def get_name(self):
        return self.__name

    def set_name(self, value):
        self.__name = value

    def get_bdate(self):
        return self.__bdate.strftime('%m/%d/%Y')

    def get_number(self):
        return self.__number

    def set_number(self, value):
        self.__number = value

    def get_entire_address(self):
        return (str(self.__add.get_houseno()) +' '+ self.__add.get_street() +" "+ self.__add.get_city() +" "+ self.__add.get_state()+' '+\
                                                                                   str(self.__add.get_ziip_()))


class Addrs():

    def __init__(self, houseno, street , city, state, ziip):
        try:
            self.__houseno = int(houseno)
            self.__street = street
            self.__city = city
            self.__state = state
            self.__ziip = int(ziip)
            if not city.isalpha() or not state.isalpha():
                raise ValueError
        except ValueError:
            print('Sorry I dont understand Address. please check again')

    def get_houseno(self):
        return self.__houseno

    def set_houseno(self, value):
        self.__houseno = value

    def get_street(self):
        return self.__street

    def set_street(self, value):
        self.__street = value

    def get_city(self):
        return self.__city

    def set_city(self, value):
        self.__city = value

    def get_state(self):
        return self.__state

    def set_state(self, value):
        self.__state = value

    def get_ziip_(self):
        return self.__ziip

    def set_zip_(self, value):
        self.__ziip = value

from enum import Enum
class Algy():

    def __init__(self, alname, symptoms, reportedby, severity):
        try:
            self.__alname = alname
            self.__symptoms = symptoms.split()
            s = Sev()
            if severity.lower() not in (s.low,s.medium,s.high):
                raise ValueError
            self.severity = severity

            if reportedby.lower() not in (Reporter.DOCTOR.value, Reporter.PATIENT.value, Reporter.RELATIVE.value):
                raise ValueError
            self.reportedby = reportedby
        except ValueError:
            print('Please enter valid severity or reporter')

    def get_alname(self):
        return self.__alname

    def set_alname(self, value):
        self.__alname = value

    def get_symptoms(self):
        return self.__symptoms

    def add_symptoms(self, value):
        self.__symptoms.append(value)


class Sev():
    high = 'high'
    medium = 'meduim'
    low = 'low'

class Reporter(Enum):
    DOCTOR = 'doctor'
    PATIENT = 'patient'
    RELATIVE = 'relative'


class Patient(Pers):

    def __init__(self,name,bdate, houseno,street, city, state, ziip, number, alname, symptoms, reportedby, severity):
        Pers.__init__(self,name,bdate, houseno,street, city, state, ziip, number)
        self.allergies = []
        self.allergy = self.add_allergy(alname, symptoms, reportedby, severity)


    def add_allergy(self, alname, symptoms, reportedby, severity):
        al = Algy(alname, symptoms, reportedby, severity)
        self.allergies.append(al)

    def get_allergylist(self):
        return self.allergies



if __name__ == '__main__':

    p = Patient('Mary','1995/02/16','4','main st','albany','NY','13333','12345672','eggs','abc def pqr stu','Patient','high')
    p.add_allergy('floar','abc pqr def','Doctor','low')
    p.add_allergy('chicken', 'abc stu jkl', 'Doctor', 'low')
    p.add_allergy('methi', 'pqr stu jkl', 'Doctor', 'low')


    print p.get_name()
    print p.get_entire_address()
    print p.get_bdate()
    for i in p.get_allergylist():
        if  i.get_alname() == 'eggs':
            i.add_symptoms('xyz')


    for i in p.get_allergylist():
        print i.get_alname() + ' : '
        print i.get_symptoms()

list = ['stu','jkl']
# given a list of symptoms write a function to retrive all allergies having symptoms passed as argument
# considering allergy list of object p

'''def rallergies(list):
    all = set()
    for item in list:
        for i in p.get_allergylist():
            if item in i.get_symptoms():
                all.add(i.get_alname())
    return all

print rallergies(list)'''





