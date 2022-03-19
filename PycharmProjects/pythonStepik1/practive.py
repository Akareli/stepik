class MoneyBox:
    def __init__(self):
        self.capacity = 10


    def can_add(self, v):
        if v < self.capacity:
            return True
        return False


    def add(self, v):
        self.capacity += v


m = MoneyBox()
m.can_add(20)

