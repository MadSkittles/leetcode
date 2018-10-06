class StockSpanner:
    def __init__(self):
        self.prices = []
        self.spans = []

    def next(self, price):
        self.prices.append(price)
        if not self.spans or price < self.prices[-2]:
            self.spans.append(1)
        else:
            self.spans.append(self.spans[-1] + 1)
            n = len(self.prices) - 1 - self.spans[-1]
            while n >= 0 and price >= self.prices[n]:
                n -= 1
                self.spans[-1] += 1
        return self.spans[-1]


if __name__ == "__main__":
    stockSpanner = StockSpanner()
    print(stockSpanner.next(100))
    print(stockSpanner.next(80))
    print(stockSpanner.next(60))
    print(stockSpanner.next(70))
    print(stockSpanner.next(60))
    print(stockSpanner.next(75))
    print(stockSpanner.next(85))
