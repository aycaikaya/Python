import random
print 'WELCOME TO SEHIR KOMBAT!'

opening1 = raw_input('Enter heroname1:')
opening2 = raw_input('Enter heroname2:')
while opening1 == opening2:
    print "This heroname is taken please try another one"
    opening2 = raw_input('Enter another heroname:')
    if opening1 != opening2:
        print "LET THE GAME BEGIN!"

herolist= [opening1,opening2]
print ' CONGRATS ' + random.choice(herolist) + ' ! , first move is yours ! '
result = random.choice(herolist)
totalhealth1=100
totalhealth2=100
def health_points(a):
    a = '[HP]' + str(totalhealth1) + ':' + '|' * (100 / 2)
    if result == opening1:
        print opening1 + a
    elif result == opening2:
        print opening2 + '[HP)' + str(totalhealth2) + ':' + '|' * (100/2)
health_points(result)
print result  + ' attacks!'

def move1():
    firstmove = raw_input(result + 'please choose your attack magnitude between 1 and 50:')
    if int(firstmove) > 50:
        print 'Your attack magnitude must be between 1 and 50!'
    elif int(firstmove) <= 50:
        print 'Now its second players turn!'
        secondmove = raw_input('please choose your attack magnitude between 1 nad 50:')
        if int(secondmove) > 50:
            print 'Your attack magnitude must be between 1 and 50!'
        elif int(secondmove) <= 50:
            print 'Now it is your turn again' + result
move1()
newhealth1 = totalhealth1-int(firstmove)
newhealth2 = totalhealth2-int(secondmove)

while newhealth1 == 0:
    print 'GAME IS OVER' + 'CONGRATS' + opening2 + 'YOU ARE THE WINNER!'
while newhealth2 == 0:
    print 'GAME IS OVER' + 'CONGRATS' + opening1 + 'YOU ARE THE WINNER!'

restart = raw_input('Do you wanna play again ?')



















#
# def health_points2(b):
#     print opening2
#     b = '[HP]' + str(totalhealth2) + ':' + '|' * (100/2)
#     print b
#     return health_points2(b)
#
# if result == opening1:
#     print health_points(a)
# else:
#     print health_points2(b)















