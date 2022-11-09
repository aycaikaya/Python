print '-----FIRST HERO----'
name1=raw_input("Please enter your hero's name:")
while name1=="":
    print 'YOU NEED TO CHOOSE A NAME FOR YOUR HERO !'
    name1=raw_input("Please enter your hero's name:")

print '----SECOND HERO----'
name2=raw_input("Please enter your hero's name:")
while name2=="":
    print 'YOU NEED TO CHOOSE A NAME FOR YOUR HERO !'
    name2=raw_input("Please enter your hero's name:")
    while name2 == name1:
        print "This name is taken! Please enter another name:"
        name2 = raw_input("YOU NEED TO CHOOSE A NAME FOR YOUR HERO !")
import random

def coin():
    coin=random.randint(0 , 1)
if coin == 0:
    print "Flip coin result:" +"  " + name1 + " " + "attack first !"
    print name1 + " "*51 + name2
else:
    print "Flip coin result:" +"  " + name2 + " " +  "attack first !"
    print name2 +" "*51 + name1

health1 = 100
health2 = 100
def health_info(health1, health2):
    print "HP1" + ":" + health1/2 * "|" + " "*50 + "HP2" + ":" + health2/2 * "|"

health_info(100, 100)

def attack(M):
  M=input()
  if M>50:
    print "Error! Your attack magnitude must be between 1 and 50 ! "
    return attack(M)
  if M<=50 and M>0:
    missing_rate=random.randint(1,100)
    if missing_rate<100-M:
        print "Succesful !"
        return
    else:
        print "Attack has been missed !"
        return

M= raw_input('Choose a Magnitude between 1 and 50:')
A= int(M)
attack(A)
