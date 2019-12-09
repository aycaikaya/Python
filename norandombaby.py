print ("--- Welcome to Sehir Hadi :) ---")

data_personal= {'names':['Abbas','Betul','Omer'],'Others':[5.4,3.2,6.4],'telephones':['5557','5466','5551','**']}




def admin_menu():
    while(True):
        print(""" admin menu\n
        1 - Set prize for the next competition.\n
        2 - Display questions for the next competition.\n
        3 - Add new question to the next competition.\n
        4 - Delete a question from the next competition.\n  
        5 - See users data.\n
        6 - Log out.""")
        while True:
            option =int( input("Welcome Sehir Hadi Admin Section, please choose one of the following options:"))
            if option >=7:
                print ("the user enters an invalid menu entry,please try again")
                admin_menu()
            elif option == 1:
                prize = input("Please type the total prize of the next competition:")
                save_here = prize
                print ('Setting prize...\nGoing back to Admin Menu...')
                return admin_menu()
            #if option == 2:

def intro():
    code=str(input('Please type your phone number in order to sign in:'))
    while code in data_personal['telephones']:
        if code==data_personal['telephones'][0]:
            print ('Welcome ' + data_personal['names'][0])
        elif code==data_personal['telephones'][1]:
            print ('Welcome ' +  data_personal['names'][1])
        if code==data_personal['telephones'][2]:
            print ('Welcome ' + data_personal['names'][2])
        elif code==data_personal['telephones'][3]:
            print ('Welcome, you have signed in as admin')
            admin_menu()
        break
    else:
        print ('The number you have typed is invalid, please try again')
        intro()
intro()