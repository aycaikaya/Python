# def find(word,letter):
#     index=0
#     while index<len(word):
#         if word[index]==letter:
#             return index
#         index = index + 1
#     return -1
# find('calculus','l')
#
# word='banana'
# word.strip()#checks if whitespace
# val='a' in 'banana'
# print val
# val2='z' in word
# print val2
# #lists
# #lists are mutable
# numbers=[1,2,3]
# numbers[2]=4
# print numbers
# print 4 in numbers#output is true
# print 7 in numbers#output is false
# for i in range(len(numbers)):
#     numbers[i]=numbers[i]*2
# print numbers
# a=[1,2,3]
# b=[4,5,6]
# print a + b#mergs a and b lists
# print a*3#it writes the list a three times
# print a[1:2]#takes first and previos before the second
# a.append(11)#adds 11 to the end of the list
# print a
# a.insert(1,'spam')#adds spam to the index 1
# print a
# a.extend(b)
# print a#merges two lists
# alpha=['b','d','a','e','r']
# alpha.sort()#alfabetik siraya gore dizer
# print alpha
# value='sehir'
# print max(value)#alfabetik sirada en son gelen
# print min(value)#alfabetik sirada en once gelen
# s='ezhel'#turns it into a list
# t=list(s)
# print t
# s='izel cansin ehliyet alicak ama iki ay boyunca asagi yukari yapacak'
# t=s.split()
# print t
# x=['the','moon','looks','nice']#makea it a string, sentence
# delimeter=' '
# print delimeter.join(x)
# engr={'uno':'one','dos':'two','tres':'three'}
# print len(engr)
# print 'uno' in engr
# print 'one' in engr
# print 'one' in engr.values()#second part is the values first part is the keys
# my_tuple=(1,2,3,[4,5])
# print my_tuple[2]
# print my_tuple[3][0]
# z=tuple('harry potter')
# print z
# s='abc'
# t=[1,2,3]
# print zip(s,t)
# x=(1,2,3)
# print zip(t,x)

#week 3
# def question_5(a,b):
#     print a*(b**2)
# question_5('python',2)
#
# import math
# def question_6(x1,y1,x2,y2):
#     print ((x1-x2)**2 + (y1-y2)**2)**1/2
# question_6(1,2,3,4)
#
# def magic():
#     print str(1) + str(9) + str(8)*3 + str(5)
# magic()
#
# def rectangele(a,b):
#     print 'area = '
#     print a*b
#     print 'perimeter = '
#     print 2*(a+b)
# rectangele(3,4)
#
# #week 4
# def dot():
#     for i in range(0,20):
#         print i*'.'
# dot()
#
# def multi():
#     for i in range(0,90,9):
#         print i
# multi()


# def right_justify(s):
#     print len(s)*' ' + s
# right_justify('evren')
#
# def num(a,b,c,d):
#     x = str(a) + str(b) + str(c) + str(d)
#     print int(x)/c
# num(1,2,3,4)

#week 7
# for char in 'banana':
#     print char
#
# fruit='banana'
# index=0
# while index < len(fruit):
#     letter = fruit[index]
#     print letter
#     index = index + 1

def quest(str_1,str_2):
    for char in str_1 and str_2:
        if char not in str_2:
            print char
            return True
        if char not in str_1:
            return False
    print char
quest('hello','world')
