# x = 10*1000
# t = (43*60.0) + 30
# v = x/t
# print v
#
# width=17  #int
# height=12.0  #float
# delimeter='.'  #str
# print width/2 #int
# print width/2.0  #float
# print height/3 #float
# print 1 + 2 * 5
# print delimeter*5
#
#
# import math
# r=5
# volume=4/3*(math.pi*(r**3))



print 'Welcome to the random math question game!'
def level_1():
    print 'Level 1:\n' 'Possible length of Numbers:1\n' 'Possible number of operators:1\n'
level_1()


import random
num1=random.randint(0,10)
num2=random.randint(0,10)
print '{} {} {}'.format(num1,'+',num2)
answer=num1+num2
typed_answer=raw_input('>>>')
while answer==typed_answer and type(typed_answer)==int:
    print 'Correct! You gained an additional star! Now you have 1 out 5 stars'
    import random
    num1 = random.randint(0, 10)
    num2 = random.randint(0, 10)
    print '{} {} {}'.format(num1, '+', num2)
    typed_answer = raw_input('>>>')
while type(typed_answer)!=int:
    print 'ERROR! Un-acceptable detected, try agin please!'
    typed_answer=raw_input('>>>')
while typed_answer!=int(answer):
    print 'Wrong you do not gain any stars for that question!'
    print 'You now have 0 out of 5 stars!'
    import random
    num1 = random.randint(0, 10)
    num2 = random.randint(0, 10)
    print '{} {} {}'.format(num1, '+', num2)
    typed_answer = raw_input('>>>')