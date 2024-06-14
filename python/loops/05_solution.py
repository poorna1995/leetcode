# string = 'hello'
# repeat_string = ''
# count = 0

# for s in string:
#     if s == repeat_string:
#         count += 1
#     repeat_string = s

# print(count)



string='PoornaPraneesha'
for char in string:
    print(char)
    if string.count(char)==1:
        print('char is ',char)
        break