def parse_input():
    file = open("data.txt","r")
    input = dict()
    for line in file.readlines():
        data = line.replace("\n","").split("-")
        if input.get(data[0]) == None:
            input.update({data[0]:[data[1]]})
        else:
            input[data[0]].append(data[1])
        if input.get(data[1]) == None:
            input.update({data[1]:[data[0]]})
        else:
            input[data[1]].append(data[0])
    return input

def path_counter(visited, cave, input, paths):
    if cave == "end":
        return paths + 1
    if input.get(cave) == None:
        return paths
    visit = visited.copy()
    for elem in input.get(cave):
        if elem.islower() and elem in visited:
            continue
        visit.append(elem)
        paths = path_counter(visit, elem, input, paths)
        visit.remove(elem)
    return paths


def part1(input):
    start = "start"
    print(f"Part 1: {path_counter([start],start,input,0)}")
        
def path_counter_2(visited, cave, input, paths, small_cave):
    if cave == "end":
        return paths + 1
    if input.get(cave) == None:
        return paths
    visit = visited.copy()
    for elem in input.get(cave):
        if elem.islower() and small_cave == None and elem != "start" and visit.count(elem) == 1:
            small_cave = elem
        if (elem.islower() and elem != small_cave and elem in visit) or (elem == small_cave and visit.count(small_cave) == 2):
            continue
        visit.append(elem)
        paths = path_counter_2(visit, elem, input, paths, small_cave)
        visit.remove(elem)
        if elem == small_cave:
            small_cave = None
    return paths

def part2(input):
    start = "start"
    print(f"Part 2: {path_counter_2([start],start,input,0,None)}")

def main():
    input = parse_input()
    part1(input)
    part2(input)

if __name__ == "__main__":
    main()