def sum_all(*args):

    for i in args:
        print(i*2)
    return sum(args)

print(sum_all(1,2,3,4))

#  args output = datatype is an tuple () - can use all operators +,*,for, while