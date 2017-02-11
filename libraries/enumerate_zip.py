print("1) enumerate():")
# 1) enumerate(iterable):
#    return enumerate object that can be used to iterate both the indices and values of passed-in iterable 
for index, value in enumerate(["one", "two", "three"]):
    print(index, value)

# 2) zip(iterable1, iterable2):
#    return an iterator of tuples, where the i-th tuple contains the i-th element from each of the passed-in iterables
#    use zip() to iterate multiple lists simultaneously
print("2) zip(), iterating multiple lists simultaneously")
alist = ["a1", "a2", "a3"]
blist = ["b1", "b2", "b3"]
clist = ["c1", "c2", "c3"]
print(zip(alist, blist, clist))
for a, b, c in zip(alist, blist, clist):
    print(a, b, c)

print("use zip() with argument unpacking")
multilists = [["a1", "a2", "a3"], ["b1", "b2", "b3"], ["c1", "c2", "c3"]]
for a, b, c in zip(*multilists):
    print(a, b, c)
