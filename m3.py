class InventoryProduct(object):
    def __init__(self,name,price,amount):
        self.name=str(name)
        self.price=float(price)
        self.amount=float(amount)
product_typed=InventoryProduct()
