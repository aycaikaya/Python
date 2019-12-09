words = {'conside','minute','accord','evident','practice','intend','concern','commit','issue','approach','establish','utter'}
definitions = {'Deem to be','infinetlt or immersubaley small','concurrence of opinion','clearley revealed to the mind of the senses or the judgement',
               'a customary way of operation or behavior','have in mind as purpose','something that interests you because it is important','perform an act','some situation',
               'move torwards','set up or found','withount qualification'}
def dictionaries():
    print 'Building Dictionary...'
    print 'Dictionary Built !'
    return words hand definitions
dictionaries()
def main_menu():
    print '1.Add a new word\n' '2.Update an existing word\n' '3.Delete and existing word\n' '4.Dispaly a words definition'
main_menu()

main_menu_choice = int(raw_input('Please select one of these options:'))

def user_choice_1():
    global main_menu_choice
    while main_menu_choice == 1:
        new_word=raw_input('What word do you want to add ?')
        words=list()
        word.append(new_word)
        new_word_def=raw_input('Please add in a definition for this word:')
        definitions=list()
        definitions.apppend(new_word_def)
        print new_word + 'added correctly!'
        break
    main_menu()
user_choice_1()
def user_choice_2():
    global main_menu_choice
    while main_menu_choice== 2:
        new_update=raw_input('What word do you want to update ?')
        while new_update not in words:
            print 'Error the word is not in the dictionary!'
            print '1.Retry with another word\n' '3.Return to the main menu'
            second_menu=int(raw_input('You may perform these actions:'))
            while second_menu == 1:
                user_choice_2()
            while second_menu == 2:
                main_menu()
                main_menu_choice=int(raw_input('Please select one of these options'))
        while new_update in words:
            new_def=raw_input('Please write in a new definition:')
            print new_update + 'was updateded correctly !'
        else:
            print 'Error ! Please try this again'
            user_choice_2()
user_choice_2()



