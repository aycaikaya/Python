user_account=0
UserName=''
Password=0




def log_in():
    global UserName
    global Password
    usernames=['Ahmet','Zeynep']
    passwords=['1234','4321']
    username = input('Username:')
    while username not in usernames:
        print('Username typed is not correct. Please try again')
        username=input('Username:')
    while username in usernames:
        if username==usernames[0]:
            UserName=username
            password=input('Password:')
            if password==passwords[0]:
                Password=password
                print('Welcome Ahmet !')
                break
            else:
                print('Password you typoed is not correct. Please try again')
                log_in()
                break
        elif username==usernames[1]:
            UserName=username
            password=input('Password:')
            if password==passwords[1]:
                Password=password
                print('Welcome Zeynep !')
                break
            else:
                print('Password you typed is not correct please try again')
                log_in()
                break
    else:
        print('Username you typed is not correct please try again.')
        log_in()




def first_menu():
    print('--- Welcome to SEHIR Bank V.0.1 --- ')
    print('1.Login\n2.exit')
    first_choice=int(input('Please choose what you want to do:'))
    if first_choice==1:
        log_in()
    elif first_choice==2:
        print('You are about to exit...')
        print('You have exitted')
        exit()
first_menu()



def main_menu():
    global UserName
    global Password
    global user_account
    print('1.Withdraw Money\n2.Deposit Money\n3.Transfer Money\n4.My Account Information\n5.Logout')
    second_choice=int(input('Please enter the number of the service:'))
    while second_choice<6 and second_choice>0:
        if second_choice==1:
            withdraw_amount=int(input('Please enter the amount you want to withdraw:'))
            if withdraw_amount>user_account:
                print("You don't have " + str(withdraw_amount) + ' TL in your account')
                main_menu()
            elif withdraw_amount<=user_account:
                print(str(withdraw_amount) + ' TL withdrawn from your account\nGoing back to the main menu...')
                user_account=user_account-withdraw_amount
                main_menu()
            break
        elif second_choice==2:
            deposit_amount=int(input('Please enter the amount you want to drop:'))
            user_account=user_account+deposit_amount
            print(str(deposit_amount) + 'TL added to your account')
            print('Going back to the main menu')
            main_menu()
            break
        if second_choice==3:
            transfer_amount=int(input('Please enter the amount you want to transfer:'))
            if transfer_amount>user_account:
                print("Sorry you don't have enough money to complete this transaction:")
                print('1.Go back to the main menu\n2.Transfer again')
                mini_menu=int(input('>>>'))
                if mini_menu==1:
                    main_menu()
                elif main_menu==2:
                    continue
            elif transfer_amount<=user_account:
                print('You have succesfully tranfered')
                user_account=user_account-transfer_amount
                main_menu()
        elif second_choice==4:
            print('------- SEHIR Bank ------- ')
            print('Current date do it later\n---------------------------- ')
            print('Your name:' + UserName)
            print('Your password:' + Password)
            print('Your amount(TL):' + str(user_account))
            break
        if second_choice==5:
            first_menu()
            break
    else:
        print('Invalid service number, Please try again.')
        main_menu()
main_menu()
