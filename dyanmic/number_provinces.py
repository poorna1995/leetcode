isConnected = [[1,1,0],[1,1,0],[0,0,1]]

def FindCircleNum( isConnected):
    # stack =[0]
    # count =0
    # for i in range(len(isConnected)):
    #     for j in range(len(isConnected[i])):
    #         if isConnected[i][j] == 1:
    #             count+=1
    #         if isConnected [i][i] ==1:
    #             count+=1
    #         print(f'i:{i} and j:{j}')
    # return count
    # print()
    def dfs(city):
        # Mark the current city as visited
        visited[city] = True
        # Explore all the cities connected to the current city
        for neighbor in range(len(isConnected)):
            if isConnected[city][neighbor] == 1 and not visited[neighbor]:
                dfs(neighbor)
    
    n = len(isConnected)
    visited = [False] * n  # To track visited cities
    province_count = 0
    
    for city in range(n):
        if not visited[city]:  # Found a new province
            dfs(city)
            province_count += 1
    
    return province_count
print(FindCircleNum(isConnected))

