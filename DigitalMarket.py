print '****Welcome to Sehir Online Market****'
print 'Please log in by proving your user credentials'
log_in_dict={'username':['ahmet','meryem'],'password':['sehir123','4444']}
UserName=raw_input('username: ')
while UserName != log_in_dict['username'][0] and UserName != log_in_dict['username'][1]:
    print 'Your username and/or password is not corrects.Please try again.'
    UserName=raw_input('username: ')
if UserName==log_in_dict['username'][0]:
    Password=raw_input('password: ')
    if Password==log_in_dict['password'][0]:
        print 'succesfully logged in!'
    else:
        print 'Your username and/or password is not correct.Please try again.'
        Password=raw_input('password: ')
if  UserName==log_in_dict['username'][1]:
    Password=raw_input('password: ')
    if Password==log_in_dict['password'][1]:
        print 'succesfully logged in!'
    else:
        print 'Your username and/or password is not correct. Please try again.'
        Password=raw_input('password: ')














