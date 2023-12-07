import Entity


class User(Entity):

    def __init__(self, addresses, cart, orders):
        self.addresses = addresses
        self.cart = cart
        self.orders = orders
