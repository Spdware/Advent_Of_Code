def parse_input():
    file = open("data.txt", "r")
    input = file.read()
    input = input.split("\n")
    return input

def risk_points(one, two, three):
    return two < one and two < three

def search_risky_points_row(line, coord):
    risky_points = set()
    if line[0] < line[1]:
        risky_points.add(tuple((coord,0)))
    if line[len(line)-1] < line[len(line)-2]:
        risky_points.add(tuple((coord,len(line)-1)))
    for i in range(1,len(line)-1):
        if risk_points(line[i-1],line[i],line[i+1]):
            risky_points.add(tuple((coord,i)))
    return risky_points

def search_risky_points_column(line, coord):
    risky_points = set()
    if line[0] < line[1]:
        risky_points.add(tuple((0,coord)))
    if line[len(line)-1] < line[len(line)-2]:
        risky_points.add(tuple((len(line)-1,coord)))
    for i in range(1,len(line)-1):
        if risk_points(line[i-1],line[i],line[i+1]):
            risky_points.add(tuple((i,coord)))
    return risky_points

#Resolved searching on the rows and the colums the points surrounded by numbers greater or equals of the number in the position
#and then used only the points who resulted found in both of the researches
def part1(input):
    lenght = len(input)
    column = [[input[i][j] for i in range(lenght)] for j in range(len(input[0]))]
    risk_points = 0 
    row_risk_points = set()
    column_risk_points = set()
    for i in range(lenght):
        row_risk_points.update(search_risky_points_row(input[i],i))
    for i in range(len(input[0])):
        column_risk_points.update(search_risky_points_column(column[i],i))
    for elem in row_risk_points:
        if elem in column_risk_points:
            risk_points += int(input[elem[0]][elem[1]])+1
    print(f"Part 1: {risk_points}")
    return row_risk_points.intersection(column_risk_points)

def get_adjacent(control, input):
    adjacent = list()
    try:
        new = tuple((control[0],control[1]+1))
        s = input[new[0]][new[1]]
    except:
        pass
    else:
        if not (new[0] < 0 or new[1] < 0):
            adjacent.append(new)
    try:
        new = tuple((control[0],control[1]-1))
        s = input[new[0]][new[1]]
    except:
        pass
    else:
        if not (new[0] < 0 or new[1] < 0):
            adjacent.append(new)
    try:
        new = tuple((control[0]+1,control[1]))
        s = input[new[0]][new[1]]
    except:
        pass
    else:
        if not (new[0] < 0 or new[1] < 0):
            adjacent.append(new)
    try:
        new = tuple((control[0]-1,control[1]))
        s = input[new[0]][new[1]]
    except:
        pass
    else:
        if not (new[0] < 0 or new[1] < 0):
            adjacent.append(new)
    return adjacent


def search_basin_size(input, elem):
    seen = set()
    search = list()
    search.append(elem)
    while search:
        control = search.pop()
        if input[control[0]][control[1]] != "9" and control not in seen:
            seen.add(control)
            search.extend(get_adjacent(control,input))
    return len(seen) 

def part2(input, low_points):
    basin = list()
    for elem in low_points:
        basin.append(search_basin_size(input,elem))
    basin.sort()
    total = basin.pop()*basin.pop()*basin.pop()
    print(f"Part 2: {total}")

def main():
    input = parse_input()
    low_points = part1(input)
    part2(input, low_points)

main()