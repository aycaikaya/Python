# name=raw_input('Give me your name:')
# print 'Your name is',name
# age=int(raw_input('give me your age:'))
# print 'Your age is',age
# current_year=2018
# born=2018-age
# calculation=born+100
# print name,'You will 100 years by the year',calculation

# num=int(raw_input('give me a number:'))
# if num%2==0:
#     print num,'is and even number!'
#     if num%4==0:
#         print num,'can be divided by 4 perfectly!'
#
# else:
#     print num,'is an odd number!'
# num1=int(raw_input('give me another number:'))
# num2=int(raw_input('and another one:'))
# if num1%num2==0:
#     print num1,'can be divided by',num2,'evenly!'
#
# else:
#     print num1,'cannot be divided by',num2,'evenly!'

# a=[1,2,3,5,7,10,34,45,67,78,89]
# num=int(raw_input('choose a number please:'))
# b=[]
# for i in a:
#     if i<num:
#         b.append(i)
# print b

# for x in range(1,3):
#     print 'We are on the time %d'%x
# x=1
# while True:
#     print 'To infinity and beyond! We are getting close, on %d now!'%(x)
#     x +=1

# computer_brands=['Apple','Asus','Dell','Samsung']
# for brands in computer_brands:
#     print brands

# print type(6==6)
#
# def max_two(a,b):
#     while a>b:
#         print a
#         return a
#     while b>a:
#         print b
#         return b
# max_two(2,3)
#
# def max_three(a,b,c):
#     while a>b and a>c:
#         print a
#         return a
#     while b>a and b>c:
#         print b
#         return b
#     while c>a and c>b:
#         print c
#         return c
# max_three(2,3,4)

#############3333333333333333
# def square(x):
#     result=x*x
#     print result #when we change print to result there will not be nay error.
# print square(5)*square(5)

# def question2(a,b,c):
#     max_num=max(a,b,c)
#     if max_num % 3 ==0:
#         return max_num
# print question2(91,102,81)

# def division(a,b):
#     return a/b
# def remainder(a,b):
#     return a%b
# def function2(a,b):
#     if a%b==0:
#         return division(a,b)
#     else:
#         return remainder(a,b)
# print function
#
# def f():
#     x=10
#     y=2
#     x=x+1
#     print x,y
# f()
#
# def sum_up_two_num(a,b):
#     print a + b
# sum_up_two_num(8,16)
# sum_up_two_num(3,4)
#
# a=4
# b=5
# def sum(a,b):
#     print a + b
# sum(3,4)
#
# a=4
# b=5
# def sum_up(a,b):
#     a=2
#     b=3
#     print a + b
# sum_up(a,b)
# sum_up(3,1)
#
# def artit(a1,n,d):
#     print a1+(n-1)*d
# artit(3,99,2)
#
#
# def red_polygone_internal(n):
#     print (n-2)*180
# red_polygone_internal(3)
# red_polygone_internal(4)
# red_polygone_internal(5)
# red_polygone_internal(8)


fruit='banana'
for char in fruit:
    print char
def word_hist(a):#1
    print a + ':' + len(a)*'*'
word_hist('the')


def reverseit(word):#3
    f = word[0]
    l= word[len(word)-1]
    print l + word[1:len(word)-1] + f
reverseit('sehir')

def repat_letters(a,n):#4
    f=a[0]
    m = a[1:len(a)-1]
    l = a[len(a)-1]
    print f*n + m*n + l*n
repat_letters('ask',2)

import random
def random_pass_gen(a):
    alphabet='abcdefghijklmnopqrstuvwxyz'
   
random_pass_gen(3)




