# class RationalNum(object):
#     def __init__(self,numaretor,denominator):
#         self.num=numaretor
#         self.den=denominator
#     def add(self,second):
#         pay = self.num*second.den + second.num*self.den
#         payda = self.den*second.den
#         return RationalNum(num,den)
#     def subs(self,second):
#         pay = self.num*second.den-second.num*self.den
#         payda = self.den*second.den
#         return RationalNum(num,den)
# class Person(object):
#     def __init__(self,first,last):
#         self.name=first
#         self.surname=last
#     def full_name(self):
#         return str(self.name) + str(self.surname)
# class Emp(Person):
#     def __init__(self,first,last,id):
#         Person.__init__(self,first,last)
#         self.id_num=id
# emp1=Emp('ayca','kaya','217550183')
# print emp1.full_name()

class Car(object):
    def __init__(self,max_speed):
        self.max=max_speed
    def price(self):
        return 'price'
class Audi(Car):
    def price(self):
        return 'Audi is 200000 dollars'
class Bmw(Car):
    def price(self):
        return 'Bmw is 300000 dollars'
car1=Audi(210)
car2=Bmw(210)
print car1.price()
print car2.price()







