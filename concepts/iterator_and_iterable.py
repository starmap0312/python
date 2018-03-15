# iterator: a class implementing the following two public methods
#   has_next()
#   next()
# iterable: a class that provides its iterator with the following method
#   __iter__()
# we can use for loop to iterate the elements of an iterable
#   ex.
#   for e in Iterable():
#       print(e)
#
# example: a class that is both iterable and the itorator

class Iterator(object):

    def __init__(self, last=1, size=5):
        self.last = last
        self.size = size  #cutoff

    def has_next(self):
        return self.last <= self.size

    def next(self):
        num = self.last
        if not self.has_next():
            raise StopIteration()
        self.last += 1
        return num

class Iterable(object):

    def __init__(self, last=1, size=5):
        self.last = last
        self.size = size  #cutoff

    def __iter__(self):
        return Iterator(self.last, self.size)

# for-looping an iterable
print('use for-loop to traverse items of the iterable')
for item in Iterable():
    print(item)

# iterating its elements with its iterator
print('use iterator to traverse items of the iterable')
iterator = Iterable().__iter__()
print(iterator.next())
print(iterator.next())
print(iterator.next())
print(iterator.next())
print(iterator.next())
