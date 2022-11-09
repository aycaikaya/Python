inventory_dict = { 'asparagus' : [10, 5], 'broccoli': [15, 6], 'carrots': [18, 7], 'apples': [20, 5],
             'banana': [10, 8], 'berries': [30, 3], 'eggs': [50, 2], 'mixed fruit juice': [0, 8],
             'fish sticks': [25, 12], 'ice cream': [32, 6], 'apple juice': [40, 7], 'orange juice': [30, 8],
            'grape juice': [10,9]}


def main_menu():
    basket_list=[ ]
    print '1.Search for product\n' '2.See basket\n' '3.Check out\n' '4.Log out\n' '5.Exit\n'

main_menu()
main_menu_choice = int(raw_input('Your choice: '))

class InventoryProduct(object):
    def __init__(self,product_choice,price,stock_amount):
        self.product_choice=str(product_choice)
        self.price=float(price)
        self.stock_amount=float(stock_amount)


if main_menu_choice==1:
    product_choice=raw_input('Please type the product you want: ')
    stock_amount=inventory_dict[product_choice][0]
    if product_choice in inventory_dict.keys():
        print 'We only have', stock_amount , 'of them.'
            amount_typed = raw_input('Please type the amount you want: ')
            while amount_typed > stock_amount:
                amount3 = raw_input('We are out of stock. Please type a valid number. ')
                print int(amount3), 'is added to you basket!'
                break
            #basket te ekle
            going_on = raw_input('Please type 0 to return the main menu: ')
            if going_on == 0:
                main_menu()
                main_menu_choice = int(raw_input('Your choice: '))
    if product_choice == 'juice':
        print 'We have found 4 juices. Please choose the one you want'
        print '1.apple juice\n' '2.grape juice\n' '3.mixed fruit juice\n' '4.orange juice\n'
        juice_choice = int(raw_input('Your choice: '))
        if juice_choice == 1:
            print 'We only have 40 apple juices.'
            apple_juice = raw_input('Please type the amount you want: ')
            while int(apple_juice) > 40:
                print 'We are out of stock. Please write a valid amount.'
                apple_juice2 = raw_input('Please type the amount you want: ')
                basket_list.append(int(apple_juice2) * inventory_dict['apple juice'])
                print int(apple_juice2) * inventory_dict['apple juice']
                print 'added to you basket.'
                break
            else:
                basket_list.append(int(apple_juice) * inventory_dict['apple juice'])
                print int(apple_juice) * inventory_dict['apple juice']
                print 'added to your basket.'




