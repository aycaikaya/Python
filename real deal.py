ch_dict={1:'Muharrem Ince',2:'Meral Aksener',3:'Recep Tayyip Erdogan'}
print 'FIGHTER CHOICES:\n' '1=Muharrem Ince\n' '2=Meral Aksener\n' '3=rte'
numbers=ch_dict.keys()
fighters=ch_dict.values()
user_choice=int(raw_input('PLEASE COOSE YOUR FIGHTER:'))
def ch_choice():
    global user_choice
    while user_choice not in ch_dict.keys():
        print 'INVALID CHRACHTER NUMBER. PLEASE TYPE A VALID NUMBER'
        user_choice=int(raw_input('PLEASE CHOOSE YOUR FIGHTER:'))
    while user_choice in ch_dict.keys():
        if user_choice==1:
            user_choice='muharrem ince'
            print 'CONGRATS ! YOU ARE MUHARREM INCE !!'
        elif user_choice==2:
            user_choice='meral aksener'
            print 'CONGRATS ! YOU ARE MERAL AKSENER'
        if user_choice==3:
            user_choice='recep'
            print 'SORRY YOU ARE RECEP :('
        break
ch_choice()
print 'NOW YOU HAVE TO CHOOSE YOUR OPPONENT'
print ch_dict.values()
opp_choice=int(raw_input('PLEASE CHOOSE YOUR OPPONENT:'))
def opponent():
    global opp_choice
    global user_choice
    while opp_choice == user_choice:
        print 'YOU CAN NOT BE YOUR OPPONENT ! THAT ONLY HAPPENS IN LIFE :( CHOOSE AGAIN !'
        opp_choice = int(raw_input('PLEASE CHOOSE YOUR OPPONENT:'))
    while opp_choice not in ch_dict.keys():
        print 'INVALID CHRACTER NUMBER. PLEASE TYPE A VALID NUMBER'
        opp_choice=int(raw_input('PLEASE CHOOSE YOUR OPPONENT:'))
    while opp_choice in ch_dict.keys():
        if opp_choice==1:
            opp_choice='muharrem ince'
            print 'YOUR OPPOENT IS MUHARREM INCE'
        elif opp_choice==2:
            opp_choice='meral aksener'
            print 'YOUR OPPONENT IS MERAL AKSENER'
        if opp_choice==3:
            opp_choice='recep'
            print 'YOUR OPPONENT IS RECEP AND YOU WILL NEVER WIN CAUSE HE IS A CHEATER :)))'
        break
opponent()
import random
player_list=[user_choice,opp_choice]
first_player=random.choice(player_list)
second_player=player_list.remove(first_player)
print 'Coin toss result shows that' + ' ' + first_player + ' ' + 'starts first !!!'
print 'ARE YOUUUU READY TO FIIIIGHTH!!!!!!!!'
hp1=100
hp2=100
def health_points():
    global first_player
    global second_player
    global hp1
    global hp2
    print 'hp[100]' + ' ' + user_choice + ':' + ' ' + '|'*int(hp1/2) + ' '*30 + 'hp[100]' + ' ' + opp_choice + ':' + ' ' + '|'*int(hp2/2)
health_points()
M=int(raw_input('Please type your attack magnitude:'))
def first_attack(current_hp):
    global hp1
    global hp2
    global M
    print first_player,'s turn'
    while M > 50:
        print 'Your attack magnitude must be between 1 and 50. Please type an invalid number.'
        M=int(raw_input('Please type your attack magnitude:'))
    while M<=50 and M>0:
        miss_rate=random.randint(1,100)
        while miss_rate<(100-M):
            print 'YOUR ATTACK IS SUCCESSFULL!'
            hp2=current_hp-M
            health_points()
            break
        else:
            print 'OOPPSSS ! ATTACK HAS BEEN MISSED !'
            health_points()
            break
        break

def second_attack(current_hp):
    global hp1
    global hp2
    global M
    print second_player,'s turn'
    while M > 50:
        print 'Your attack magnitude must be between 1 and 50. Please type an invalid number.'
        M = int(raw_input('Please type your attack magnitude:'))
    while M <= 50 and M > 0:
        miss_rate = random.randint(1, 100)
        while miss_rate < (100 - M):
            print 'YOUR ATTACK IS SUCCESSFULL!'
            hp1 = current_hp - M
            health_points()
            break
        else:
            print 'OOPPSSS ! ATTACK HAS BEEN MISSED !'
            health_points()
            break
        break
def main():
    global hp1
    global hp2
    while hp1>1 and hp2>1:
        first_attack(hp1)
        M=int(raw_input('Please type your attack magnitude:'))
        second_attack(hp2)
        continue
    while hp1<=1:
        print first_player, 'wins !!!'
        break
    while hp2<=1:
        print second_player, 'wins !!!'
        break

main()






