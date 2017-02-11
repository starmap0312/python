print("1) lambda expression:")
# 1) define a function object
# 1.1) conventional
#      def func(x, y):
#          function body
#          return value
# 1.2) lambda expression
#      func = lambda x, y: expression 
#
# examples:
def to_int_func(x):
    return int(x)
print(to_int_func("123"))

to_int_lambda = lambda x: int(x)
print(to_int_lambda("123"))

def add_func(x, y):
    return x + y
print("sum={}".format(add_func(1, 2)))

add_lambda = lambda x, y: x + y
print("sum={}".format(add_lambda(1, 2)))

print("2) map():")
# 2) map(function_object, iterable):
#    map a passed-in iterable to a new iterable by applying the passed-in function object

for i in map(to_int_func, ["1", "2", "3"]):
    print(i)
# note: in Python2, map() returns a list
#       i.e. [ to_int_func(i) for i in ["1", "2", "3"] ]

print("3) combination of lambda and map:")
# 3) combination of lambda and map:
alist = [1, 2, 3]
double_list = map(lambda x: x * 2, alist)
print(double_list)

alist = [1,2,3,4]
blist = [9,8,7,6]
sum_list = map(lambda x, y: x + y, alist, blist)
print(sum_list)

print("4) filter():")
# 4) filter(function, iterable):
#    filter out all elements of a passed-in iterable to a new iterable if the passed-in function object evaluates to True
fibonacci_list = [ 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55 ]
odd_fibonacci_list = list(filter(lambda x: x % 2, fibonacci_list))
print(odd_fibonacci_list)

