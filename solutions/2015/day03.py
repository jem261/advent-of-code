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

houses1 = map_reader(s)

print(f"{houses1} houses recieved at least 1 present!")

def alternate_turns(map):
    directions = {"^": (0,1), "v": (0, -1), ">": (1,0), "<": (-1,0)}
    visited_santa = {(0, 0)}
    visited_robosanta = {(0, 0)}
    x1, y1 = 0, 0
    x2, y2 = 0, 0
    santa_map = map[::2]
    robosanta_map = map[1::2]
    for char in santa_map:
        dx1, dy1 = directions[char]
        x1, y1 = x1+dx1, y1+dy1
        visited_santa.add((x1,y1))
    for char in robosanta_map:
        dx2, dy2 = directions[char]
        x2, y2 = x2+dx2, y2+dy2
        visited_robosanta.add((x2,y2))
    return len(visited_robosanta | visited_santa)

houses2 = alternate_turns(s)

print(f"{houses2} houses recieved at least 1 present!")