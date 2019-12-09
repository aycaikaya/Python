import math
# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#     def move(self,new_x,new_y):
#         self.x=new_x
#         self.y=new_y
#
# newpoint = Point(0, 1)
# print newpoint.y
# print newpoint.x
# newpoint.move(1,2)
# print newpoint.x
# print newpoint.y
#
# class Circle:
#     def __init__(self,radius):
#         self.radius=radius
#     def area(self):
#         area = math.pi * (self.radius**2)
#         return area
#         #print 'Area is: ' + str(area)
#     def perimeter(self):
#         perimeter = 2*math.pi*self.radius
#         return perimeter
# newcircle = Circle(5)



# class Student:
#     def __init__(self,name,surname,department,semester,gpa):
#         self.name=name
#         self.surname=surname
#         self.department=department
#         self.semester= semester
#         self.gpa=gpa

# class Triangle:
#     def __init__(self,angle1,angle2,angle3):
#         self.angle1=angle1
#         self.angle2=angle2
#         self.angle3=angle3
#     def check_triangle(self):
#         if self.angle1+self.angle2+self.angle3 == 180:
#             return True
#         else:
#             return False
# equiltriangle = Triangle(40,40,95)
# print equiltriangle.check_triangle()
#
# def ekin_can(a):
#      if a==3:
#          print 'ekincan aycaya asik'
#      else:
#          print 'ekincan ayca ile evlenmek istiyor'
# ekin_can(3)

#b= 'emre sevuk'
#print b[3:6]

# a='dark'
# b='night'
# print a+b
# print a*3

# list=[1,True,'em
# print list[2][2]re',2.0,[1,3,5]]
# print list[3]
# print list[-2]
#
# list_s=[1,2,3]
# list_s.append(4)
# print list_s

# list_a=[4,5,6]
# list_a.insert(2,2)
# print list_a
#
# meyve_sebze=['elma','karpuz','marul','lahana','cilek','brokoli']
# print meyve_sebze[0],meyve_sebze[1],meyve_sebze[4]
#
# meyve_sebze_dict={'meyve':['cilek','karpuz','elma','armut'],'sebze':['marul','lahana','brokoli']}
# print meyve_sebze_dict['meyve']
# print meyve_sebze_dict['sebze']
#
# del meyve_sebze_dict['sebze']
# print meyve_sebze_dict
#
# a,b=(3,5)
# print a
# print b
#


# x=[(0,1),(2,3),(4,5)]
# for a,b in x:
#     print a,b

# class Araba:
#     armut=0 #basina self koymadigim halde global olur.
#     def __init__(self,isim1,kapil,teker1,fiyat1,hp1,renk1):
#         self.kapi=kapil
#         self.teker=teker1
#         self.fiyat=fiyat1
#         self.hp=hp1
#         self.renk=renk1
#         self.isim=isim1
#     def ilerle(self):
#         print 'ilerledi.'
#     def indirim(self,yuzde):
#         print 'eski fiyat', self.fiyat
#         self.fiyat=self.fiyat - (self.fiyat*(yuzde/100))
#         print 'yeni fiyat', self.fiyat
# toyota=Araba(4,4,100000,90,'mat siyah')
# bmw=Araba(4,4,150000,110, 'mat kirmizi')
# merso=Araba(4,4,200000,130, 'mat beyaz')
# merso.ilerle()
# bmw.indirim(5.0)
#
# class Galeri:
#     def __init__(self,cins1,arabalar1):
#         self.cins=cins1
#         self.arabalar=arabalar1
# ozkardesler=Galeri('taxi',[toyota,bmw,merso])
# print ozkardesler.arabalar[0].isim,ozkardesler.arabalar[1].isim,ozkardesler.arabalar[2].isim

class Employee:
    def __init__(self,first,last,monthly_pay):
        self.first=first
        self.last=last
        self.montly_pay=monthly_pay
        self.email=first + last + '@gmail.com'
emp_1=Employee('cerennaz','harmandar',10000)
emp_2=Employee('gizem','canko',11000)

print emp_1.email
print emp_2.email
print emp_1.first + emp_1.last

# print emp_1
# print emp_2
# emp_1.first='cerennaz'
# emp_1.last='harmandar'
# emp_1.email='cerennazharmandar@gmail.com'
# emp_1.monthly_pay=4500
# emp_2.first='gizem'
# emp_2.last='canko'
# emp_2.email='gizemcanko@gmail.com'