class Order:

    def __init__(self, order_date, tracking_id, delivery_cost, status, address, order_items, user):
        self.order_date = order_date
        self.tracking_id = tracking_id
        self.delivery_cost = delivery_cost
        self.status = status
        self.address = address
        self.order_items = order_items
        self.user = user
