def even_number(num):
    for i in range(2,num+1,2):
        yield i


for limit in even_number(10):
    print(limit)    

