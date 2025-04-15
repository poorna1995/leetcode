n=5

# def convert(n):


def countingBits(n):
    return [bin(x).count("1") for x in range(0, n)]
#     bits=[]
#     i=0
#     while i<n:
#         bits.append(bin(i))
#         i+=1
#     output =[]
#     for bit in bits:
#         length= len(bit)
#         output.append(length - 2)

#     return output
    
print(countingBits(n))