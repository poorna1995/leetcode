# print all the numbers
def all_num(n):
    if n==0:
        return 0
    print(f'before:{n}')
    all_num(n-1)
    print(n)
    return
print(all_num(7))



