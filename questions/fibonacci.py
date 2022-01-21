# Compute n-th fibonacci number

class Recursion(object):

    def fibonacci(self, n):
        assert(n >= 0)
        if n <= 1:
            return n
        return self.fibonacci(n - 2) + self.fibonacci(n - 1)

print(Recursion().fibonacci(0))
print(Recursion().fibonacci(1))
print(Recursion().fibonacci(7))


class Iterative(object):

    def fibonacci(self, n):
        assert(n >= 0)
        if n <= 1:
            return n
        f = [0, 1]
        for i in range(2, n + 1):
            f.append(f[i - 2] + f[i - 1])
        return f[n]

print(Iterative().fibonacci(0))
print(Iterative().fibonacci(1))
print(Iterative().fibonacci(7))

class SpaceSaved(object):

    def fibonacci(self, n):
        assert(n >= 0)
        if n <= 1:
            return n
        (a, b) = (0, 1)
        for i in range(2, n + 1): # iterate n - 1 times
            c = a + b
            a = b
            b = c
        return b

print(SpaceSaved().fibonacci(0))
print(SpaceSaved().fibonacci(1))
print(SpaceSaved().fibonacci(7))

class TailRecursion(object):

    def fibonacci(self, n):
        assert(n >= 0)
        if n <= 1:
            return n
        return self.fib(n, 0, 1)

    def fib(self, n, a, b):
        return b if n == 1 else self.fib(n - 1, b, a + b) # n -1 recursions

print(TailRecursion().fibonacci(0))
print(TailRecursion().fibonacci(1))
print(TailRecursion().fibonacci(7))
