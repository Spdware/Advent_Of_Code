import string

def parse_input():
    input = dict()
    file = open("data.txt", "r")
    lines = file.read().split("\n\n")
    char = lines[1].split("\n")
    for elem in char:
        el = elem.split(" -> ")
        input.update({el[0]: el[1]})
    return lines[0].replace("\n",""), input

def calculate_max_min(polymer):
    el_polymer = dict.fromkeys(set([x for x in polymer]), 0)
    for elem in el_polymer.keys():
        el_polymer.update({elem : polymer.count(elem)})
    return max(el_polymer.values()) - min(el_polymer.values())
#Unoptimized method
def part1(polymer, input):
    for cycle in range(10):
        new_polymer = polymer[0]
        for i in range(len(polymer)-1):
            new_polymer += input[polymer[i:i+2]] + polymer[i+1]
        polymer = new_polymer
    print(f"Part 1: {calculate_max_min(polymer)}") 

def create_elements(elements, polymer):
    for i in range(len(polymer)-1):
        elements[polymer[i:i+2]] += 1
    return elements

def define_difference(elements, input, polymer):
    alphabet = dict.fromkeys([x for x in string.ascii_uppercase], 0)
    for key in elements.keys():
        alphabet[key[0]] += elements[key]
        alphabet[input[key]] += elements[key]
    alphabet[polymer] += 1
    values = list(alphabet.values())
    while min(values) == 0:
        values.remove(0)
    return max(alphabet.values()) - min(values) 

#Optimized method
def part2(polymer, input):
    elements = dict.fromkeys(set([x for x in input.keys()]), 0)
    elements = create_elements(elements, polymer)
    for _ in range(39):
        new_elements = dict.fromkeys(set([x for x in input.keys()]), 0)
        for key in elements.keys():
            if elements[key] > 0:
                chain = input[key]
                new_elements[key[0]+chain] += elements[key]
                new_elements[chain+key[1]] += elements[key]
        elements = new_elements
    print(f"Part 2: {define_difference(elements, input, polymer[-1])}") 

def main():
    polymer, input = parse_input()
    part1(polymer, input)
    part2(polymer, input)

if __name__ == "__main__":
    main()