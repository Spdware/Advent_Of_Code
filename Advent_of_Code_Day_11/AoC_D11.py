def parse_input():
    file = open("data.txt", "r")
    input = {}
    for y, line in enumerate(file.read().splitlines()):
        for x, l in enumerate(line):
            input[x,y] = int(l)
    return input

def adjacent(x,y):
    for x_1 in (-1,0,1):
        for y_1 in (-1,0,1):
            if x_1 == y_1 == 0:
                continue
            yield tuple((x+x_1, y + y_1))     

def flash(input, i , fo):
    input[i] += 1
    if input[i] > 9:
        fo.append(i)

def flash_propagation(input, flashed_octopus):
    flashes = 0
    while flashed_octopus:
        fo = flashed_octopus.pop()
        if input[fo] == 0:
            continue
        input[fo] = 0
        flashes += 1
        for item in adjacent(fo[0], fo[1]):
            if item in input and input[item] != 0:
                flash(input, item, flashed_octopus)
    return flashes

def part1(input):
    flashes = 0
    flashed_octopus = list()
    for _ in range(100):
        for i, value in input.items():
            flash(input, i, flashed_octopus)
        flashes += flash_propagation(input, flashed_octopus)
    print(f"Part 1: {flashes}")

def part2(input):
    flashed_octopus = list()
    steps = 0
    while True:
        steps +=1
        for i, value in input.items():
            flash(input, i, flashed_octopus)
        tmp = flash_propagation(input, flashed_octopus)
        if sum(input.values()) == 0:
            print(f"Part 2: {steps}")
            return

def main(): 
    part1(parse_input())
    part2(parse_input())

if __name__ == "__main__":
    main()