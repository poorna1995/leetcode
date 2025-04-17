arr = [1,1,4,5,7]

find = 7

# def FirstOccurrence(arr,find):
#     for i,num in enumerate(arr):
#         if num == find:
#             print(f'num = {num},i = {i}')
#             return i
    # return -1


index =0
def FirstOccurrenceRecursion(arr, find, index):
    if index== len(arr):
        return -1

    if arr[index] == find:
        # print(index)
        return index
    else:
        return FirstOccurrenceRecursion(arr, find, index+1)

        
    
print(FirstOccurrenceRecursion(arr, find, index = 0))
    

    
        

    
# print(FirstOccurrence(arr,find))
    