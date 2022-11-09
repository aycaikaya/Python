print 'Welcome to the random math question game!'
def level_1():
    print 'Level 1:\n' 'Possible length of Numbers:1\n' 'Possible number of operators:1\n'
level_1()
import random
question_number=5
x= ['+','-','*','/','%']
user_stars=[]
answer=0
question=0


total_error=0



def level1_quest():
    global answer
    num1,num2=(random.randint(0,10),random.randint(0,10))
    print 'What is',num1,'+',num2,'?'
    answer=(num1+num2)
level1_quest()
typed_answer=input('>>>')
def questions1():
    global typed_answer

    global total_error
    global question_number
    for i in range(0,question_number+1):


        while True:
             while typed_answer==answer:
                 user_stars.append('*')
                 print 'Correct! You gained an additional star. Now you have', len(user_stars), 'out of 5 stars'
                 print user_stars
                 while total_error >= 3:
                     print 'You do not have enough starts to move on to the next level, this as far as you go!'
                     exit()

                 if len(user_stars) == 5:
                     print 'You have enough stars this level, time to move on!'
                     print 'Amazing! You beast tha game!You answered total of',total_error,'anweres wrong this attempt'
                     return
                 level1_quest()

                 typed_answer = input('>>>')
             while typed_answer!=answer:
                 print 'Wrong! You do not gain any stars from that question!'
                 print 'Now you have',len(user_stars),'out of 5 stars'
                 total_error=total_error + 1
                 print user_stars
                 while total_error >= 3:
                     print 'You do not have enough starts to move on to the next level, this as far as you go!'
                     exit()

                 if len(user_stars) == 5:
                     print 'You have enough stars this level, time to move on!'
                     print 'Amazing! You beat tha game!You answered total of',total_error,'answeres wrong this attempt'
                     return
                 level1_quest()

                 typed_answer=input('>>>')
questions1()





def level_2():
    print 'level:2\n' 'Possible length of numbers:1\n' 'Possible number of operators:2'
level_2()


x= ['+','-','*','/','%']
user_stars=[]
answer=0
total_error=0


def level2_quest():
    global answer
    num1,num2=(random.randint(0,10),random.randint(0,10))
    operators1=x[:2]
    print 'What is', num1, random.choice(operators1), num2, '?'
    while random.choice(operators1)==x[0]:
        answer=(num1 + num2)
    while random.choice(operators1)==x[1]:
        answer=(num1-num2)
level2_quest()
typed_answer=input('>>>')
def questions2():
    global typed_answer
    global total_error
    global question_number
    for i in range(1,question_number+1):


        while True:
            while typed_answer==answer:
                user_stars.append('*')
                print 'Correct! You gained an additional star. Now you have', len(user_stars), 'out of 5 stars'
                print user_stars
                while total_error >= 3:
                    print 'You do not have enough starts to move on to the next level, this as far as you go!'
                    exit()

                if len(user_stars) == 5:
                    print 'You have enough stars this level, time to move on!'
                    print 'Amazing! You beast tha game!You answered total of',total_error,'anweres wrong this attempt'
                    return
                level2_quest()

                typed_answer = input('>>>')
            while typed_answer!=answer:
                print 'Wrong! You do not gain any stars from that question!'
                print 'Now you have',len(user_stars),'out of 5 stars'
                total_error=total_error + 1
                print user_stars
                while total_error >= 3:
                    print 'You do not have enough starts to move on to the next level, this as far as you go!'
                    exit()

                if len(user_stars) == 5:
                    print 'You have enough stars this level, time to move on!'
                    print 'Amazing! You beat tha game!You answered total of',total_error,'answeres wrong this attempt'
                    return
                level2_quest()

                typed_answer=input('>>>')
questions2()

def level_3():
    print 'level:3\n' 'Possible length of numbers:1\n' 'Possible number of operators:3'
level_3()

x= ['+','-','*','/','%']
user_stars=[]
answer=0
question=0

total_error=0


def level3_quest():
    global answer
    num1,num2=(random.randint(0,10),random.randint(0,10))
    operators2=x[:3]
    print 'What is', num1, random.choice(operators2),num2,'?'
    while random.choice(operators2)==x[0]:
        answer=num1+num2
    while random.choice(operators2)==x[1]:
        answer=num1-num2
    while random.choice(operators2)==x[2]:
        answer=num1*num2
level3_quest()
typed_answer=input('>>>')
def questions1():
    global typed_answer
    global total_error
    global question_number

    while True:
        while typed_answer==answer:
            user_stars.append('*')
            print 'Correct! You gained an additional star. Now you have', len(user_stars), 'out of 5 stars'
            print user_stars
            while total_error >= 3:
                print 'You do not have enough starts to move on to the next level, this as far as you go!'
                exit()

            if len(user_stars) == 5:
                print 'You have enough stars this level, time to move on!'
                print 'Amazing! You beast tha game!You answered total of',total_error,'anweres wrong this attempt'
                return
            level3_quest()

            typed_answer = input('>>>')
        while typed_answer!=answer:
            print 'Wrong! You do not gain any stars from that question!'
            print 'Now you have',len(user_stars),'out of 5 stars'
            total_error=total_error + 1
            print user_stars
            while total_error >= 3:
                print 'You do not have enough starts to move on to the next level, this as far as you go!'
                exit()

            if len(user_stars) == 5:
                print 'You have enough stars this level, time to move on!'
                print 'Amazing! You beat tha game!You answered total of',total_error,'answeres wrong this attempt'
                return
            level3_quest()

            typed_answer=input('>>>')
questions1()
def level4():
    print 'level:3\n' 'Possible length of numbers:2\n' 'Possible operators:4'
level4()

x= ['+','-','*','/','%']

user_stars=[]
answer=0
question=0

total_error=0

def level4_quest():
    global answer
    num1,num2=(random.randint(0,100),random.randint(0,100))
    operators3=x[:4]
    print 'What is',num1,random.choice(operators3),num2,'?'
    while random.choice(operators3)==x[0]:
        answer=num1+num2
    while random.choice(operators3)==x[1]:
        answer=num1-num2
    while random.choice(operators3)==x[2]:
        answer=num1*num2
    while random.choice(operators3)==x[3]:
        answer=num1/num2
level4_quest()
typed_answer=input('>>>')
def questions1():
    global typed_answer
    global total_error
    global question_number

    while True:
        while typed_answer==answer:
            user_stars.append('*')
            print 'Correct! You gained an additional star. Now you have', len(user_stars), 'out of 5 stars'
            print user_stars
            while total_error >= 3:
                print 'You do not have enough starts to move on to the next level, this as far as you go!'
                exit()

            if len(user_stars) == 5:
                print 'You have enough stars this level, time to move on!'
                print 'Amazing! You beast tha game!You answered total of',total_error,'anweres wrong this attempt'
                return
            level4_quest()

            typed_answer = input('>>>')
        while typed_answer!=answer:
            print 'Wrong! You do not gain any stars from that question!'
            print 'Now you have',len(user_stars),'out of 5 stars'
            total_error=total_error + 1
            print user_stars
            while total_error >= 3:
                print 'You do not have enough starts to move on to the next level, this as far as you go!'
                exit()

            if len(user_stars) == 5:
                print 'You have enough stars this level, time to move on!'
                print 'Amazing! You beat tha game!You answered total of',total_error,'answeres wrong this attempt'
                return
            level4_quest()

            typed_answer=input('>>>')
questions1()

def level5():
    print 'level:5\n' 'Possible length of numbers:2\n' 'Possible number of operators:5'
level5()


x= ['+','-','*','/','%']
user_stars=[]
answer=0
question=0

total_error=0

def level5_quest():
    global answer
    num1,num2=(random.randint(0,100),random.randint(0,100))
    operators4=x[:5]
    print 'What is',num1,random.choice(operators4),num2,'?'
    while random.choice(operators4)==x[0]:
        answer=num1+num2
    while random.choice(operators4)==x[1]:
        answer=num1-num2
    while random.choice(operators4)==x[2]:
        answer=num1*num2
    while random.choice(operators4)==x[3]:
        answer=num1/num2
    while random.choice(operators4)==x[4]:
        answer=num1%num2
level5_quest()
typed_answer=input('>>>')
def questions1():
    global typed_answer
    global total_error
    global question_number

    while True:
        while typed_answer==answer:
            user_stars.append('*')
            print 'Correct! You gained an additional star. Now you have', len(user_stars), 'out of 5 stars'
            print user_stars
            while total_error >= 3:
                print 'You do not have enough starts to move on to the next level, this as far as you go!'
                exit()

            if len(user_stars) == 5:
                print 'You have enough stars this level, time to move on!'
                print 'Amazing! You beast tha game!You answered total of',total_error,'anweres wrong this attempt'
                return
            level5_quest()

            typed_answer = input('>>>')
        while typed_answer!=answer:
            print 'Wrong! You do not gain any stars from that question!'
            print 'Now you have',len(user_stars),'out of 5 stars'
            total_error=total_error + 1
            print user_stars
            while total_error >= 3:
                print 'You do not have enough starts to move on to the next level, this as far as you go!'
                exit()

            if len(user_stars) == 5:
                print 'You have enough stars this level, time to move on!'
                print 'Amazing! You beat tha game!You answered total of',total_error,'answeres wrong this attempt'
                return
            level5_quest()

            typed_answer=input('>>>')
questions1()

























