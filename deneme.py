# try:
#     print "Hello World"
# except:
#     print "This is an error message!"
#
# while True:
#         try:
#             randOperation()
#             randOperation = random.choice(operation)
#             if question >= 10:
#                 break
#             userInput = int(input("Enter the answer: "))
#             if userInput == ans:
#                 print("Correct!" + "\n")
#                 user_score += 1
#                 question += 1
#             else:
#                 print("Incorrect!" + "\n")
#                 question += 1
#         except ValueError:
#             print("I'm sorry that's invalid")
# #             question += 1
#
# # list=[]
# # print len(list)
# import random
# a=random.randint(0,10)
# b=random.randint(0,10)
# answer=a-b
# print a,'-',b
# choice=raw_input(':'
#     print 'you made it')
# if choice==answer:


print 'Welcome to the random math question game!'

import random
question_number=5
x= ['+','-','*','/','%']
user_stars=[]
answer=0
question=0
total_error=0

def level2_quest():
    global answer
    num1,num2=(random.randint(0,10),random.randint(0,10))
    operators=['+','-']
    random_operator=random.choice(operators)
    print 'What is', num1,random_operator, num2, '?'
    while random_operator==operators[0]:
        answer=num1 + num2
    while random_operator==operators[1]:
        answer=num1-num2
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