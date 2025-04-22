class OrderTracker:
    def __init__(self, orders):
        self.orders = orders
        self.index = 0
    
    def __iter__(self):
        self.index = 0
        return self
    
    def __next__(self):
        if self.index < len(self.orders):
            order = self.orders[self.index]
            self.index += 1
            return order
        else:
            raise StopIteration

def notify_shipped(order_iteratorior):
    for order in order_iteratorior:
        if order["status"] == "shipped":
            yield f"Поръчка #{order['id']} е изпратена."

if __name__ == "__main__":
    orders = [
        {"id": 101, "status": "processing"},
        {"id": 102, "status": "shipped"},
        {"id": 103, "status": "shipped"}
    ]
    
    tracker = OrderTracker(orders)
    
    for notification in notify_shipped(tracker):
        print(notification)
