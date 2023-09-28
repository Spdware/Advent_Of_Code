def parse_input():
    file = open("data.txt", "r").readlines()
    ssdi = list()
    ssdo = list()
    for line in file:
        line = line.split(" | ")
        ssdi.append(line[0].split())
        ssdo.append(line[1].split())
    return ssdi, ssdo

def part1(output):
    unique_number = 0
    for elem in output:
        for seg in elem:
            match len(seg):
                case 2 | 3 | 4 | 7:
                    unique_number +=1
                case _:
                    pass
                
    print(f"Part 1: {unique_number}")

def string_contained(seg, unique):
    for i in unique:
        if seg.count(i) == 0:
            return False
    return True

def calculate_segment(seg,unique):
    match len(seg):
        case 5:
            if string_contained(seg,unique[0]):
                return "3"
            elif string_contained(unique[4],seg):
                return "5"
            else:
                return "2"
        case 6:
            if string_contained(seg,unique[0]):
                if string_contained(seg,unique[2]):
                    return "9"
                else:
                    return "0"
            else:
                return "6"

def create_ssd(elem,unique):
    num = ""
    for seg in elem:
        match len(seg):
            case 2:
                num+="1"
            case 3:
                num+="7"
            case 4:
                num+="4"
            case 7:
                num+="8"
            case 5 | 6:
                num+=calculate_segment(seg,unique)
            case _:
                pass   
    return num

def calculate_unique(input):
    unique = list(["","","",""])
    for elem in input:
        if len(elem) == 2:
            unique[0] = ("".join(elem))
        if len(elem) == 3:
            unique[1] = ("".join(elem))
        if len(elem) == 4:
            unique[2] = ("".join(elem))
        if len(elem) == 7:
            unique[3] = ("".join(elem))
    return unique

def search_six(input, unique):
    for elem in input:
        if len(elem) == 6 and not string_contained(elem, unique):
            return elem

def part2(input,output):
    sum_ssd = 0
    for i in range(len(input)):
        unique = calculate_unique(input[i])
        unique.append(search_six(input[i],unique[0]))
        sum_ssd += int(create_ssd(output[i], unique))
    print(f"Part 2: {sum_ssd}")

def main():
    input,output = parse_input()
    part1(output)
    part2(input,output)
main()