log_in_dict={'username':['ahmet','meryem'],'password':['sehir123','4444']}
UserName=raw_input('username: ')
while UserName!=log_in_dict['username'][0] and UserName!=log_in_dict['username'][1]:
    print 'Your username and/or password is not correct please try again.'
    UserName=raw_input('username: ')
while UserName==log_in_dict['username'][0]:
    Password=raw_input('password: ')
    if Password==log_in_dict['password'][0]:
        print 'Succesfully logged in !'
        print 'Welcome' + ' ' + log_in_dict['username'][0] +'!' + 'Please choose one of the options by entering corresponding menu number.'
        break
    else:
        print 'Your username and/or password is not correct. Please try again.'
while UserName==log_in_dict['username'][1]:
    Password=raw_input('password: ')
    if Password==log_in_dict['password'][1]:
        print 'Successfuly logged in !'
        print 'Welcome'  + ' ' + log_in_dict['username'][1] +  '!' + 'Please choose one of the options by entering correspondinmg menu number.'
        break
    else:
        print 'Your username and/or password is not correct. Please try again.'
