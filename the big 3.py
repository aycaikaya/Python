print '---------- WELCOME TO MORAL KOMBAT TURKEY EDITION ----------'
import random
def ask_magnitude():
    M=int(raw_input('Please type your attack magnitude:'))
    while M>50 or M<1:
        print 'Your attack magnitude must be between 1 and 50. Please type an invalid number.'
        M=int(raw_input('please type your attack magnitude:'))
    else:
        return M
def attack(healt_point,fighter):
    missing_rate=random.randint(1,100)
    print '----------',fighter, 'attacks !!!','----------'
    magnitude=ask_magnitude()
    if missing_rate > magnitude:
        print fighter, 'attacks with', magnitude, 'damage !!!'
        healt_point=healt_point-magnitude
    else:
        print 'ooopsyy', fighter, 'missed the attack!!!'
    return healt_point
def chractrize(points1,points2,fighter1,fighter2):
    print 'hp[100]' + ' ' + fighter1 + ':' + ' ' + '|' * int(points1 / 2) + ' ' * 30 + 'hp[100]' + ' ' + fighter2 + ':' + ' ' + '|' * int(points2 / 2)
def fighter_name():
    ch_dict = {1: 'Muharrem Ince', 2: 'Meral Aksener', 3: 'Recep Tayyip Erdogan'}
    print 'FIGHTER CHOICES:\n' '1=Muharrem Ince\n' '2=Meral Aksener\n' '3=rte'
    numbers = ch_dict.keys()
    fighters = ch_dict.values()
    fighter1=int(raw_input('Please choose your fighter:'))
    while fighter1 not in ch_dict.keys():
        print 'Thats not a chrachter number, please type a valid one.'
        fighter1=int(raw_input('Please choose your fighter:'))
    while  fighter1 in ch_dict.keys():
        if fighter1==1:
            fighter1='Muharrem Ince'
            print 'Congrats ! You are Muharrem Ince !'
        elif fighter1==2:
            fighter1='Meral Aksener'
            print 'Congrats ! You are Meral Aksener !'
        if fighter1==3:
            fighter1='RTE'
            print 'Awwww :( You are RTE :((('
        break
    print 'Now you have to choose your opponents.'
    fighter2=int(raw_input('Please choose your opponent:'))
    while fighter2 not in ch_dict.keys():
        print 'Thats not a chrachter number, please type a valid one '
        fighter2=int(raw_input('Please choose your opponent:'))
        while fighter2==fighter1:
            print 'you cannot choose your fighter as your opponent, choose again !'
            fighter2=int(raw_input('Please choose your opponent:'))
        while fighter2 in ch_dict.keys():
            if fighter2==1:
                fighter2='Muharrem Ince'
                print 'Your opponent is Muharrem Ince'
            elif fighter2==2:
                fighter2='Meral Aksener'
                print 'Your opponent is Meral Aksener'
            if fighter2==3:
                fighter2='RTE'
                print 'Your opponent is RTE and you will never win cause he is a cheater :))'
            break
    return fighter1 and fighter2

def main():
    fighter_name()
    fighters_list=[fighter1,fighter2]
    first_player=random.choice(fighters_list)
    second_player=fighters_list.remove(first_player)
    while True:
        hp1,hp2=(100,100)
        while hp1>1 and hp2>1:
            hp1 = attack(hp1,first_player)
            chractrize(hp1,hp2,first_player,second_player)
            if hp1<1 or hp2<1:
                break
            hp2 = attack(hp2,second_player)
            chractrize(hp1,hp2,first_player,second_player)
        if hp1<1:
            print second_player, 'wins !'
            exit()
        elif hp2<1:
            print first_player, 'wins !'
            exit()
main()










