from IPython.display import clear_output as co


class Cart:
    def __init__(self):
        self.items = []

    def add_item(self, obj):
        self.items.append(obj)

    def remove_item(self, product_name):
        for obj in self.items:
            if obj.name == product_name:
                self.items.remove(obj)
                break

    def show_list(self):
        # resets the cart total so that if you add/remove items, the correct math with be performed when adding add values
        print("=" * 50)
        if not self.items:
            print("You have no items in your cart. ")
        else:
            display_cart = []
            # I want to add dictionary objets into display_cart
            for obj in self.items:
                if obj.name not in [i['name'] for i in display_cart]:
                    display_cart.append({
                        'name': obj.name,
                        'price': obj.price
                    })
                else:
                    for i in display_cart:
                        if i['name'] == obj.name:
                            i['price'] += obj.price
            for i in range(len(display_cart)):
                print(
                    f"{i+1}: {display_cart[i]['name']} @${display_cart[i]['price']} [{[i.name for i in self.items].count(display_cart[i]['name'])}]")
        print("=" * 50)

    def show_instructions():
        print("=" * 50)
        print("""Type 'add' to add item to cart.
    Type 'remove' to add item from cart.
    Type 'show' to view all items in your cart.
    Type 'quit' to exit program and show your list.""")
        print("=" * 50)


class CartItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __repr__(self):
        return f'<CartItem: {self.name} @{self.price}>'


class ShoppingCart:
    def show_instructions():
        print("=" * 50)
        print("""Type 'add' to add item to cart.
Type 'remove' to add item from cart.
Type 'show' to view all items in your cart.
Type 'clear' to remove all items from your cart.
Type 'quit' to exit program and show your list.""")
        print("=" * 50)

    @classmethod
    def run(self):
        cart = Cart()

        done = False
        while not done:
            self.show_instructions()
            cart.show_list()

            ask = input("Type the command you'd like to run ").lower()
            co()

            if ask == 'quit':
                cart.show_list()
                done = True
            elif ask == 'add':
                item_name = input('What item would you like to add? ')
                item_price = float(input('How much does this item cost? '))
                cart_item = CartItem(item_name, item_price)
                cart.add_item(cart_item)
            elif ask == 'clear':
                # cart.items = []
                cart.items.clear()
            elif ask == 'remove':
                item_name = input('What item would you like to remove? ')
                cart.remove_item(item_name)


# shopping_cart = ShoppCart()
# shopping_cart.run()
ShoppingCart.run()
