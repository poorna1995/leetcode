def FindOccurence(array, findme, index =0):
    if len(array) ==0:
        return -1
    if array[0] == findme:
        return index
    return FindOccurence(array[1:],findme,index+1)


array = [1, 6, 2, 9, 10, 5]
findme = 10


print(FindOccurence(array, findme, index =0))