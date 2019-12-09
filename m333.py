inventory_dict = { 'asparagus' : [10, 5], 'broccoli': [15, 6], 'carrots': [18, 7], 'apples': [20, 5],
             'banana': [10, 8], 'berries': [30, 3], 'eggs': [50, 2], 'mixed fruit juice': [0, 8],
             'fish sticks': [25, 12], 'ice cream': [32, 6], 'apple juice': [40, 7], 'orange juice': [30, 8],
            'grape juice': [10,9]}
print '****Welcome to Sehir Online Market****'
print 'Please log in by proving your user credentials'
class log_in(object):
    def __init__(self,UserName,Password):
        self.UserName=UserName
        self.Password=Password
log_in_dict={'username':['ahmet','meryem'],'password':['sehir123','4444']}
UserName1=log_in(log_in_dict['username'][0],log_in_dict['password'][0])
UserName2=log_in(log_in_dict['username'][1],log_in_dict['password'][1])
UserName=raw_input('username: ')
while UserName1==Username:
    print 'Succesfulley logged in !'

basket_list=[ ]
def main_menu():
    basket_list=[ ]
    print '1.Search for product\n' '2.See basket\n' '3.Check out\n' '4.Log out\n' '5.Exit\n'

main_menu()
main_menu_choice = int(raw_input('Your choice: '))


if main_menu_choice==1:
    product_choice=raw_input('What are you searching for ? Please type it: ')
    amount1=inventory_dict[product_choice][0]
    if product_choice in inventory_dict.keys():
        print 'We only have' , amount1 , 'of them.'
        amount2=raw_input('Please type the amount you want: ')
        while amount2 > amount1:
            amount3=raw_input('We are out of stock. Please type a valid number. ')
            print int(amount3), 'is added to you basket!'
            break
        basket_list.append(product_choice*int(amount2))
        going_on=raw_input('Please type 0 to return the main menu: ')
        if going_on==0:
            main_menu()
            main_menu_choice=int(raw_input('Your choice: '))
    if product_choice == 'juice':
        print 'We have found 4 juices. Please choose the one you want'
        print '1.apple juice\n' '2.grape juice\n' '3.mixed fruit juice\n' '4.orange juice\n'
        juice_choice=int(raw_input('Your choice: '))
        if juice_choice==1:
            print 'We only have 40 apple juices.'
            apple_juice=raw_input('Please type the amount you want: ')
            while int(apple_juice) > 40:
                print 'We are out of stock. Please write a valid amount.'
                apple_juice2=raw_input('Please type the amount you want: ')
                basket_list.append(int(apple_juice2)*inventory_dict['apple juice'])
                print int(apple_juice2)*inventory_dict['apple juice']
                print 'added to you basket.'
                break
            else:
                basket_list.append(int(apple_juice)*inventory_dict['apple juice'])
                print int(apple_juice)*inventory_dict['apple juice']
                print 'added to your basket.'

        if juice_choice==2:
            print 'We only have 10 grape juices.'
            grape_juice=raw_input('Please type the amount you want: ')
            while int(grape_juice) > 10:
                print 'We are out of stock. Please type a valid amount.'
                grape_juice2=raw_input('Please type the amount you want: ')
                basket_list.append(int(grape_juice2)*inventory_dict['grape juice'])
                print int(grape_juice2)*inventory_dict['grape juice']
                print 'added to your basket.'
                break
            else:
                basket_list.append(int(grape_juice)*inventory_dict['grape juice'])
                print int(grape_juice)*inventory_dict['grape juice']
                print 'added to your basket.'







if main_menu_choice==2:
    print basket_list
if main_menu_choice==4:
    log_in()
if main_menu_choice==3:
    print 'Are you sure you want to exit ?'
    print '1.Return to the main menu\n' '2.Exit\n'
    exit=int(raw_input('Choose one of the options: '))
    if exit==1:
        main_menu()
        main_menu_choice=int(raw_input('Your choice: '))
    if exit==2:
        print 'You have succesfly exited !'
















class InventoryProduct(object):
    def __init__(self,name,price,amount):
        self.name=str(name)
        self.price=float(price)
        self.amount=float(amount)
product_typed=InventoryProduct(inventory_dict.keys(),inventory_dict.values()[1],inventory_dict.values()[0])

