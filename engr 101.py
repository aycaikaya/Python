import math
# class Point:
#     def __init__(self,x,y):
#         self.x = x
#         self.y = y
#
#     def get_dist_from_origin(self):
#         return math.sqrt(self.x**2 + self.y**2)
#     def get_dist_from_another_point(self,p):
#         return math.sqrt(self.x-p.x)**2 + (self.y-p.y)**)
#
#
# point1 = Point(3,5)
# point2 = Point(0,0)
# print type(point1)
# print point1
#
# print point1.get_dist_from_origin()
# print point1.get_dis_from_another_point(point2)


# class Time:
#     def __init__(self,hour=0,min=0,sec=0):
#         self.hour = self
#         self.minute = min
#         self.second = sec
#     def print_time(self,10,30):
#         print str(self.hour) +':' + str(self.minute) + \
#             ':' + str(self.second)
#     def time_to_int(self):
#         total_seconds = self.hour * 3600
#         total_seconds += self.minute * 60
#         total_seconds += self.second
#         return total_seconds
# time1 = Time(10,30)
# time1.print_time()
# print time1.time_to_int()

#class Time:
 #   def print_time(self):

# class Person:
#     def __init__(self,first,last):
#         self.first=first
#         self.last=last
#     def __str__(self):
#         return self.first + ' ' + self.last
#     def print_fullName(self):
#         print self.first + ' ' + self.last
#
# class Employ(Person):
#     def __init__(self,f,l,id):
#         Person.__init__(self,f,l)
#         self.id=id
# emp=Employ('ayca idil','kaya','217550183')
# emp.print_fullName()
#
# class Car:
#     def __init__(self,max_speed):
#         self.max_speed=max_speed
#
#     def price(self,bmw,audi):
#         self.bmw=bmw
#         self.audi=audi

# class Car:
#     def __init__(self,mx_spd):
#         self.max_speed=mx_spd
# class BMW(Car):
#     def __init__(self,max_speed,price):
#         self.price = price
#         super(BMW,self).__init__(max_speed) #Car.__init__()
#     def display_price(self):
#         print self.price
# bmw1=BMW(240,140000)

# class Game:
#     def __init__(self,energy,money,no_of_castles):
#         self.energy=energy
#         self.money=money
#         self.no_of_castles=no_of_castles
#     def display_info(self):
#         print self.energy,self.money,self.no_of_castles
# game1=Game(100,50,3)
# class Player:
#     def __init__(self,energy,money,no_cast):
#         super(Player,self).__init__(energy,money,no_cast)
#         #self.energy=self
#         #self.money=money
#         #self.no_of_castles=no_cast
#     def create_castle(self):
#         if self.energy > 5 and self.money > 10:
#             self.no_of_castles += 1
#             self.energy -= 5
#             self.money -= 10
#             print 'castle olusturulduu'
#         else:
#             print 'para bittiii'
# Player1=Player2(30,51,2)
# for i in range (7):
#     Player1.create_castle()



#basic class example
class Circle(object):
    pi=3.14
    def __init__(self,radius=1):
        self.radius=radius
    def area(self):
        return(self.radius**2)*Circle.pi
c=Circle(radius=24)
print c.area()

#inhetritance example
# class Animal(object):
#     def __init__(self):
#         print 'ANIMAL CREATED'
#     def whoAmI(self):
#         print 'ANIMAL'
#     def eat(self):
#         print 'EATING...'
# class Dog(Animal):
#     def __init__(self):
#         Animal.__init__(self)
#         print 'DOG CREATED'
#     def whoAmI(self):
#         print 'DOG'
#     def bark(self):
#         print 'WOOF WOOF WOOF!!!!!!'
# D=Dog()
# D.eat()
# D.bark()
# D.whoAmtxt = 'but soft what light in yonder window breaks'
                     words = txt.split()
                     t = list()