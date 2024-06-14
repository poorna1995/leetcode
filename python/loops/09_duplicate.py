items =['apple','banana','apple','mango']

unique_items=set()

for item in items:
    if item in unique_items:
        print('Duplicate')
        break
    unique_items.add(item)


print(' ')