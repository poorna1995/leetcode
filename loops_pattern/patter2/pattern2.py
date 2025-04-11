def pattern2():
    for i in range(5):
        for j in range(i+1):
            print("*", end="")
        print()
    
print(pattern2())