import heapq

def parse_input():
    input = dict()
    file = open("data.txt","r")
    for y, value in enumerate(file.readlines()):
        for x, v in enumerate(value.replace("\n","")):
            input.update({(x,y):int(v)})
    return input

def adjacent(u):
    yield (u[0], u[1] + 1)
    yield (u[0], u[1] - 1)
    yield (u[0] + 1, u[1])
    yield (u[0] - 1, u[1])

def create_risk(v, i, j):
    risk = (v + i + j)
    return risk if risk < 10 else risk % 10 + 1
   
def a_star(input, start, end):
    open_list = [] 
    closed_dict = {}
    open_dict = {start : 0}
    heapq.heappush(open_list, (0, start))

    while open_list:
        value, q = heapq.heappop(open_list)
        if q in closed_dict and closed_dict[q] < value:
            continue
        for x in adjacent(q):
            if x not in input.keys():
                continue
            v = value + input[x]
            if x == end:
                return v
            if x in closed_dict and closed_dict[x] <= v:
                continue
            if x in open_dict and open_dict[x] <= v:
                continue
            open_dict[x] = v
            heapq.heappush(open_list, (v, x))
        closed_dict.update({q:value})

def parse_input_2():
    input = dict()
    file = open("data.txt","r")
    matrix = file.readlines()
    height = len(matrix)
    for y, value in enumerate(matrix):
        for x, v in enumerate(value.replace("\n","")):
            for j in range(5):
                for i in range(5):
                    input.update({(x + i * height, y + j * height):create_risk(int(v),i,j)})
    return input

def main():
    input = parse_input()
    print(f"Part 1: {a_star(input, (0,0), max(input.keys()))}")
    input = parse_input_2()
    print(f"Part 2: {a_star(input, (0,0), max(input.keys()))}")

if __name__ == "__main__":
    main()