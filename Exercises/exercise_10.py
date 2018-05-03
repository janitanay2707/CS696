class Gens:
    def _init_(self, start=1):
        self.start = start

    def _str_(self):
        return "Start value for generators class is: {}".format(self.start)

    def doubles(self):
        i = self.start
        while True:
            yield i
            i = i * 2

    def fib(self):
        yield 1
        yield 1
        previous = 1
        current = 1
        while True:
            n = previous + current
            yield n
            previous = current
            current = n


    def linear(self, n):
        i = self.start
        while True:
            yield i
            i = i + n


    def exponential(self, n):
        i = self.start
        while True:
            yield i
            i = i * i

    def sequence(self, list):
        while True:
            for i in list:
                yield i


    def triple_half(self):
        i = self.start
        while True:
            yield i
            i = i * 3
            yield i
            i = i/2
