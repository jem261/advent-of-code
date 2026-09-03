def map_reader(map):
    directions = {"^": (0,1), "v": (0, -1), ">": (1,0), "<": (-1,0)}
    visited = {(0, 0)}
    x, y = 0, 0
    for char in map:
        dx, dy = directions[char]
        x, y = x+dx, y+dy
        visited.add((x,y))
    return len(visited)

with open("inputs/2015/day03.txt") as f:
    s = f.read()

houses = map_reader(s)

print(f"{houses} houses recieved at least 1 present!")