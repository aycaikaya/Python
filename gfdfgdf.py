# def linedot(linesayi):
#     for i in range(linesayi+1):
#         print i*'*'
#
# linedot(12)
#
# def sum():
#     sum=0
#     for i in range(1,11):
#         sum += i
#         print sum
# sum()

# def divide(a,b,c,d):
#     x=str(a)+ str(b)+ str(c)+str(d)
#     print int(x)/c
# divide(1,2,3,4)

# import math
#
# def findArea(radius):
#     area = math.pi * radius**2
#     print area
#     return area
# findArea(3)
#
# def findArea(radius):
#     area = math.pi * radius**2
#     return area
# print findArea(3)
#
# def is_divisible(x, y):
#     if x % y == 0:
#         return True
#     else:
#         return False
# print is_divisible(6,2)
#
#
# def sumNumbers(n):
#     if n == 1:
#         return 1
#     else:
#         return n + sumNumbers(n-1)
# print sumNumbers(5)
#
# def factodoit(n):
#     if n ==1 :
#         return 1
#     else:
#         return n * factodoit(n-1)
#
# print factodoit(7)
#
# def mylen(x):
#     c=0
#     for y in x:
#         c = c +1
#     return c
# print mylen('Hello')
# print mylen('This string is already too long')

x=abs(max([-2,-17-15],key=abs))
print x
