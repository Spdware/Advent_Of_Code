def parse_input():
    file = open("data.txt","r")
    return [x.strip("\n") for x in file.readlines()]

def assigned_corrupted_value(e):
    match(e):
        case ")":
            return 3
        case "]":
            return 57
        case "}":
            return 1197
        case ">":
            return 25137

def is_corrupted(elem):
    ob = list()
    cv = 0
    for e in elem:
        if e in "([{<":
            ob.append(e)
        else:
            ch = ob.pop()
            if ord(e) - ord(ch) !=  1 and ord(e) - ord(ch) !=  2:
                cv += assigned_corrupted_value(e)    
    return cv

def part1(input):
    corrupted_value = 0
    for elem in input:
        corrupted_value += is_corrupted(elem)    
    print(f"Part 1: {corrupted_value}")

def autocomplete(elem):
    av = 0
    ob = list()
    for e in elem:
        if e in "([{<":
            ob.append(e)
        else:
            ob.pop()
    while ob:
        match ob.pop():
            case "(":
                av = av*5 + 1
            case "[":
                av = av*5 + 2
            case "{":
                av = av*5 + 3
            case "<":
                av = av*5 + 4
    return av

#Could be optimized taking ob in part 1 when cv is 0 in the is_corrupted function
def part2(input):
    autocompleted_value = list()
    for elem in input:
        if is_corrupted(elem) == 0:
            autocompleted_value.append(autocomplete(elem))
    autocompleted_value.sort()
    print(f"Part 2: {autocompleted_value[len(autocompleted_value)//2]}")

def main():
    input = parse_input()
    part1(input)
    part2(input)

if __name__ == "__main__":
    main()