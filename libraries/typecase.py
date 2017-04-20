# type-check
# 1) Python: isinstance([obj], [classname])
# 2) Scala : [obj].isInstanceOf[classname]
# 3) Java  : [obj] instanceof [classname]
assert(isinstance(str, object))
assert(not isinstance(str, int))

# type-casting
# 1) Python: [classname]([obj])
#    Python does not provide an equivalent of Scala's asInstanceOf[T] because it is useless
# 2) Scala : [obj].asInstanceOf[classname]
# 3) Java  : ([classname]) [obj]

