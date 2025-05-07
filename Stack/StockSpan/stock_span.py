class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        count = 1
        if not self.stack:
            self.stack.insert(0,(price, count))
        else:
            while self.stack and self.stack[0][0] <=  price:
                count += self.stack.pop(0)[1]
            self.stack.insert(0,(price, count))
        return count    