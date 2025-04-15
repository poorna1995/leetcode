rooms = [[1],[2],[3],[]]
# rooms = [[1,3],[3,0,1],[2],[0]]

def canVisitAllRooms(rooms):
    visited = set()
    queue=[0] #start sfrom toom 0
    while queue:
        room = queue.pop(0)
        if room in visited:
            continue
        visited.add(room)
        for key in rooms[room]:
            if key in visited:
                continue
            queue.append(key)
    return len(visited) == len(rooms)


print(canVisitAllRooms(rooms))