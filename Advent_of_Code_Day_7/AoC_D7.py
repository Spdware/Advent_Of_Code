def part1(input,keyset):
    fuel_calc = dict()
    for elem in range(max(keyset)):
        fuel_calc.update({elem:0})
    for elem in fuel_calc.keys():
        for elem2 in keyset:
            fuel_calc[elem] += abs(elem-elem2)*input[elem2]
    print(f"Part 1: {min(fuel_calc.values())}")
#Gauss' formula
def sum(x):
    return x*(x+1)//2

def part2(input, keyset):
    fuel_calc = dict()
    for elem in range(max(keyset)):
        fuel_calc.update({elem:0})
    for elem in fuel_calc.keys():
        for elem2 in keyset:
            fuel_calc[elem] += sum(abs(elem-elem2))*input[elem2]
    print(f"Part 1: {min(fuel_calc.values())}")

def main():
    input, keyset = parse_input()
    keyset = set(keyset)
    part1(input, keyset)
    part2(input, keyset)

def create_input(input):
    dic = dict()
    for elem in input:
        if dic.get(elem):
            dic[elem] += 1
        else:
            dic.update({elem:1})
    return dic

def parse_input():
    file = open("data.txt","r")
    input = [int(x) for x in file.read().split(",")]
    return create_input(input),input

main()