def parse_input():
    file = open("data.txt","r")
    points = set()
    folds = list()
    for line in file.readlines():
        line = line.replace("\n","").split(",")
        match len(line):
            case 2:
                points.add(tuple((int(line[0]),int(line[1]))))
            case 1:
                if line[0] != "":
                    line = line[0].replace("\n","").split()[2].split("=")
                    folds.append(tuple((line[0],int(line[1]))))
    return points, folds

def change_points(points, f, j):
    remove_points = set()
    add_points = set()
    for elem in points:
        if elem[j] >= f:
            remove_points.add(elem)
            if j == 0:
                add_points.add(tuple((2*f - elem[0], elem[1])))
            else:
                add_points.add(tuple((elem[0], 2*f - elem[1])))
    return points.difference(remove_points).union(add_points)

def part1(points, folds):
    match folds[0][0]:
        case "x":
            points = change_points(points, folds[0][1], 0)
        case "y":
            points = change_points(points, folds[0][1], 1)
    print(f"Part 1: {len(points)}")

#Print the points in the page in the correct order
def printer(points):
    x_max = max(x[0] for x in points)
    y_max = max(y[1] for y in points)
    for j in range(y_max+1):
        for i in range(x_max+1):
            if (i,j) in points:
                print("#", end="")
            else:
                print(" ",end="")
        print()

def part2(points, folds):
    for f in folds:
        match f[0]:
            case "x":
                points = change_points(points, f[1], 0)
            case "y":
                points = change_points(points, f[1], 1)
    print(f"Part 2: {printer(points)}")

def main():
    points, folds = parse_input()
    part1(points,folds)
    part2(points, folds)

if __name__ == "__main__":
    main()