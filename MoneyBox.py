class MoneyBox:
    def __init__(self,capacity):
        self.money = 0
        self.capacity = capacity
        #print(self.capacity)

    def can_add(self, v):
        print(self.capacity, self.money)
        if self.money + v =< self.capacity:
            return True
        else:
            return False

    def add(self, v):
        if MoneyBox.can_add(self, v):

            self.money += v
            print(self.money)

m = MoneyBox(capacity=5)
#m(10)
m.add(v=2)
m.add(v=5)
