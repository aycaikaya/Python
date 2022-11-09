
import random
question_number=5
answer=0
total_error=0
user_stars=[]
x= ['+','-','*','/','%']

def level1():
    print 'level:1'
    print 'Possible length of numbers:1'
    print'Possible number of operators operators:1'
level1()

def level1_num():
    global answer
    for i in range(1,question_number+1):
        num1,num2=(random.randint(0,10),random.randint(0,10))
        answer = num1 + num2
    print 'what is',num1,'+',num2,'?'

level1_num()

typed_answer=input('>>>')

def questions1():
    global answer
    global total_error
    global typed_answer
    global question_number
    while True:
        while typed_answer==answer:
            user_stars.append('*')
            print 'Correct you gain an additional star! Now you have',len(user_stars),'out of 5 stars!'
            print user_stars
            while total_error>=3:
                print 'You don not have enough stars to go on to the next level, this is as far as you go!'
                exit()
            if len(user_stars)==5:
                print 'You have enough stars this level, time to move on!'
                print 'Amazing! You beat the game! You answered total of',total_error,'answers wrong this attempt.'
                return
            level1_num()
            typed_answer=input('>>>')
        while typed_answer!=answer:
            print 'Wrong! You do not gain any stars from that question!'
            print 'Now you have',len(user_stars),'out of 5 stars!'
            total_error=total_error+1
            print user_stars
            while total_error>=3:
                print 'You do not have enough stars to go on to the next level, this is as far as you go'
                exit()
            if len(user_stars)==5:
                print 'You have enough stars this level, time to move on! '
                print 'Amazing! You beat the game! You answered total of',total_error,'answers wrong this attempt. '
            level1_num()
            typed_answer=input('>>>')
questions1()

answer=0
total_error=0
user_stars=[]

def level2():
    print 'level:2'
    print 'Possible length of numbers:1'
    print 'Possible number of operators:1'
level2()

def level2_num():
    global answer
    for i in range(1,question_number+1):
        num1,num2=(random.randint(0,10),random.randint(0,10))
        operators2=x[:2]
        random_operator2=random.choice(operators2)
        if random_operator2==x[0]:
            answer=num1+num2
        elif random_operator2==x[1]:
           answer=num1-num2
    print 'What is', num1, random_operator2, num2, '?'
level2_num()

typed_answer=input('>>>')
def questions1():
    global answer
    global total_error
    global typed_answer
    while True:
        while typed_answer==answer:
            user_stars.append('*')
            print 'Correct you gain an additional star! Now you have',len(user_stars),'out of 5 stars!'
            print user_stars
            while total_error>=3:
                print 'You don not have enough stars to go on to the next level, this is as far as you go!'
                exit()
            if len(user_stars)==5:
                print 'You have enough stars this level, time to move on!'
                print 'Amazing! You beat the game! You answered total of',total_error,'answers wrong this attempt.'
                return
            level2_num()
            typed_answer=input('>>>')
        while typed_answer!=answer:
            print 'Wrong! You do not gain any stars from that question!'
            print 'Now you have',len(user_stars),'out of 5 stars!'
            total_error=total_error+1
            print user_stars
            while total_error>=3:
                print 'You do not have enough stars to go on to the next level, this is as far as you go'
                exit()
            if len(user_stars)==5:
                print 'You have enough stars this level, time to move on! '
                print 'Amazing! You beat the game! You answered total of',total_error,'answers wrong this attempt. '
            level2_num()
            typed_answer=input('>>>')
questions1()

answer=0
total_error=0
user_stars=[]

def level3():
    print 'level:3'
    print 'Possible length of numbers:1'
    print 'Possible number of operators:3'
level3()

def level3_num():
    global answer
    for i in range(1,question_number+1):
        num1,num2=(random.randint(0,10),random.randint(0,10))
        operators3=x[:3]
        random_operator3=random.choice(operators3)
        if random_operator3==x[0]:
            answer=num1+num2
        elif random_operator3==x[1]:
            answer=num1-num2
        if random_operator3==x[2]:
            answer=num1*num2
    print 'What is', num1, random_operator3, num2, '?'
level3_num()

typed_answer=input('>>>')
def questions1():
    global answer
    global total_error
    global typed_answer
    while True:
        while typed_answer==answer:
            user_stars.append('*')
            print 'Correct you gain an additional star! Now you have',len(user_stars),'out of 5 stars!'
            print user_stars
            while total_error>=3:
                print 'You don not have enough stars to go on to the next level, this is as far as you go!'
                exit()
            if len(user_stars)==5:
                print 'You have enough stars this level, time to move on!'
                print 'Amazing! You beat the game! You answered total of',total_error,'answers wrong this attempt.'
                return
            level3_num()
            typed_answer=input('>>>')
        while typed_answer!=answer:
            print 'Wrong! You do not gain any stars from that question!'
            print 'Now you have',len(user_stars),'out of 5 stars!'
            total_error=total_error+1
            print user_stars
            while total_error>=3:
                print 'You do not have enough stars to go on to the next level, this is as far as you go'
                exit()
            if len(user_stars)==5:
                print 'You have enough stars this level, time to move on! '
                print 'Amazing! You beat the game! You answered total of',total_error,'answers wrong this attempt. '
            level3_num()
            typed_answer=input('>>>')
questions1()

answer=0
total_error=0
user_stars=[]

def level4():
    print 'level:4'
    print 'Possible lengt of numbers:2'
    print 'Possible number of operators:4'
level4()

def level4_num():
    global answer
    for i in range(1,question_number+1):
        num1,num2=(random.randint(0,100),random.randint(0,100))
        operators4=x[:4]
        random_operator4=random.choice(operators4)
        if random_operator4==x[0]:
            answer=num1+num2
        elif random_operator4==x[1]:
            answer=num1-num2
        if random_operator4==x[2]:
            answer=num1*num2
        elif random_operator4==x[3]:
            answer=num1/num2
    print 'What is', num1, random_operator4, num2, '?'
level4_num()

typed_answer=input('>>>')
def questions1():
    global answer
    global total_error
    global typed_answer
    while True:

        while typed_answer==answer:
            user_stars.append('*')
            print 'Correct you gain an additional star! Now you have',len(user_stars),'out of 5 stars!'
            print user_stars
            while total_error>=3:
                print 'You don not have enough stars to go on to the next level, this is as far as you go!'
                exit()
            if len(user_stars)==5:
                print 'You have enough stars this level, time to move on!'
                print 'Amazing! You beat the game! You answered total of',total_error,'answers wrong this attempt.'
                return
            level4_num()
            typed_answer=input('>>>')
        while typed_answer!=answer:
            print 'Wrong! You do not gain any stars from that question!'
            print 'Now you have',len(user_stars),'out of 5 stars!'
            total_error=total_error+1
            print user_stars
            while total_error>=3:
                print 'You do not have enough stars to go on to the next level, this is as far as you go'
                exit()
            if len(user_stars)==5:
                print 'You have enough stars this level, time to move on! '
                print 'Amazing! You beat the game! You answered total of',total_error,'answers wrong this attempt. '
            level4_num()
            typed_answer=input('>>>')
questions1()

answer=0
total_error=0
user_stars=[]

def level5():
    print 'level:5'
    print 'Possible length of numbers:2'
    print 'Possible numbers of operators:5'
level5()

def level5_num():
    global answer
    for i in range(1,question_number+1):
        num1,num2=(random.randint(0,100),random.randint(0,100))
        operators5=x[:5]
        random_operator5=random.choice(operators5)
        if random_operator5==x[0]:
            answer=num1+num2
        elif random_operator5==x[1]:
            answer=num1-num2
        if random_operator5==x[2]:
            answer=num1*num2
        elif random_operator5==x[3]:
            answer=num1/num2
        if random_operator5==x[4]:
            answer=num1%num2
    print 'What is', num1, random_operator5, num2, '?'
level5_num()

typed_answer=input('>>>')
def questions1():
    global answer
    global total_error
    global typed_answer
    while True:
        while typed_answer==answer:
            user_stars.append('*')
            print 'Correct you gain an additional star! Now you have',len(user_stars),'out of 5 stars!'
            print user_stars
            while total_error>=3:
                print 'You don not have enough stars to go on to the next level, this is as far as you go!'
                exit()
            if len(user_stars)==5:
                print 'You have enough stars this level, time to move on!'
                print 'Amazing! You beat the game! You answered total of',total_error,'answers wrong this attempt.'
                return
            level5_num()
            typed_answer=input('>>>')
        while typed_answer!=answer:
            print 'Wrong! You do not gain any stars from that question!'
            print 'Now you have',len(user_stars),'out of 5 stars!'
            total_error=total_error+1
            print user_stars
            while total_error>=3:
                print 'You do not have enough stars to go on to the next level, this is as far as you go'
                exit()
            if len(user_stars)==5:
                print 'You have enough stars this level, time to move on! '
                print 'Amazing! You beat the game! You answered total of',total_error,'answers wrong this attempt. '
            level5_num()
            typed_answer=input('>>>')

questions1()




