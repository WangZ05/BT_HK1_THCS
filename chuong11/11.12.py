tuple_a = (3,1,2,4)
tuple_b = (5,7,6,8)
tuple_c=tuple_a+tuple_b
print(tuple_c)
tuple_d=tuple(sorted(tuple_c))
print(tuple_d)
print(tuple_d[3])
print(tuple_d[-3:])