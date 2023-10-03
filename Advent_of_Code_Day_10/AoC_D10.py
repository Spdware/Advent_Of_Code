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
    ob = str()
    cv = 0
    for e in elem:
        if e in "([{<":
            ob += e
        else:
            ch = ob[len(ob)-1]
            ob = ob[0:len(ob)-1:1]
            if ord(e) - ord(ch) !=  1 and ord(e) - ord(ch) !=  2:
                cv += assigned_corrupted_value(e)    
    if cv == 0:
        return cv, ob
    else:
        return cv, ""

def part1(input):
    open_brackets = list()
    corrupted_value = 0
    for elem in input:
        cv, ob = is_corrupted(elem)
        corrupted_value += cv
        if len(ob) > 0:
            open_brackets.append(ob)    
    print(f"Part 1: {corrupted_value}")
    return open_brackets

def autocomplete(elem):
    av = 0
    for e in elem[::-1]:
        match e:
            case "(":
                av = av*5 + 1
            case "[":
                av = av*5 + 2
            case "{":
                av = av*5 + 3
            case "<":
                av = av*5 + 4
    return av

def part2(input):
    autocompleted_value = list()
    for elem in input:
        autocompleted_value.append(autocomplete(elem))
    autocompleted_value.sort()
    print(f"Part 2: {autocompleted_value[len(autocompleted_value)//2]}")

def main():
    input = parse_input()
    ob = part1(input)
    part2(ob)

if __name__ == "__main__":
    main()