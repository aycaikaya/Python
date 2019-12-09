inventory = { 'asparagus' : [10, 5], 'broccoli': [15, 6], 'carrots': [18, 7], 'apples': [20, 5],
             'banana': [10, 8], 'berries': [30, 3], 'eggs': [50, 2], 'mixed fruit juice': [0, 8],
             'fish sticks': [25, 12], 'ice cream': [32, 6], 'apple juice': [40, 7], 'orange juice': [30, 8],
            'grape juice': [10,9]}

print  'Welcome to Sehir Online Market! Please Log In By providing your user crediantals:'
username = 'izelcansin'
password = '123321'
user = raw_input('Write Username:')
pasw = raw_input('Enter Password: ')
def login():
    user = raw_input('Write Username:')
    pasw = raw_input('Enter Password: ')

basket= [ ]
while user != username or pasw != password:
    print '****INVALID INFORMATION*** Please Try Again'
    login()
    if user == username and pasw == password:
     print 'Successfully Loged In!'
    break

# untill this point   #we basically just asked for the username and password
def menu():
 basket = [ ]
 print 'Welcome to the SehirMarket Again!,' , username , 'Please select from the menu :'
 print '1.SEARCH FOR YOUR PRODUCT\n'  '2.SEE BASKET\n'  '3.CHECK OUT\n' '4.LOG OUT\n' '5.EXIT\n'

menu()

makingChoice = True
while makingChoice :
    mainmenuChoice = int(input())
    if mainmenuChoice > 5 or mainmenuChoice < 1 :
        print '**INVALID NUMBER** Please choose a number from the menu'
    else :
        makingChoice = False

if mainmenuChoice == 1 :
    while mainmenuChoice == 1:
        product_typed = str(raw_input('Please Write The Name Of The Product: '))
        keys_inventory = inventory.keys()
        if product_typed  in keys_inventory :
            print 'Good Choice!', product_typed , 'is a definetly a need!'
            break
        else :
            print 'We do NOT have that product.Maybe spelled it wrong? Try Again.'
            continue

product_choosen = inventory[product_typed]
price_of_product = inventory[product_typed][1]
amount_we_have = inventory[product_typed][0]
print product_typed , 'costs' , price_of_product, '$  for each.' , 'We Have:' , amount_we_have , 'of it in Stock,How many do you want?'
enteringAmount = True
while enteringAmount :
    amount_user_wants = float(input())
    if amount_user_wants > amount_we_have :
             print 'We are sorry, we do not have that amount of choosen product.Please enter an amount between 0 and stock number.'
    else :
            enteringAmount = False
            print 'Total Cost of : ', product_typed , 'is ' , amount_user_wants*price_of_product, '$ . Add to Basket? (1:yes 0:Return Main Menu)'
            basketadd = int(input())
            if basketadd == True :
                print 'Successfully Added to Basket, Anything Else Would You Like to Buy? (0:Yes, Return to Main Menu 1:No)'
                basket = [ ]
                basket = basket + [product_typed]
                basketadd2 = int(input())
                if basketadd2 == False :
                    menu()

                elif basketadd2 == True:
                    print '****Thank You For Shopping From Sehir Market!*****'
            if basketadd == False:
                menu()

