#Parsing the input
def parse_input():
    #Data is the file with your input
    file = open("data.txt","r")
    start = list()
    end = list()
    for line in file:
        start_data, end_data = tuple(line.split(" -> "))
        start.append(tuple(int(x) for x in start_data.strip().split(",")))
        end.append(tuple(int(x) for x in end_data.strip().split(",")))
        #Gives rows/columns with the starting point being the minimum in the pair
        if(start[len(start)-1][0]==end[len(end)-1][0] and start[len(start)-1][1]>end[len(end)-1][1]):
            end.append(start.pop())
            start.append(end.pop(len(end)-2))
        if(start[len(start)-1][1]==end[len(end)-1][1] and start[len(start)-1][0]>end[len(end)-1][0]):
            end.append(start.pop())
            start.append(end.pop(len(end)-2))
    return start, end

def check_cross(start1, end1,start2,end2):
    if(start1[0]<= start2[0] <= end1[0] and start2[1]<=start1[1]<=end2[1]):
        return True
    else:
        return False
#Determines if there is a collision between the two line of valves
def check_collision(isOrizontal, isVertical, isOrizontal_2, isVertical_2, start1, end1, start2,end2):
    if(isVertical == isVertical_2 == True):
        if(start1[0] == start2[0] and ((start1[1] <= start2[1] <= end1[1]) or (
            start2[1] <= start1[1] <= end2[1]))):
            return True 
        else: 
            return False
    elif (isOrizontal == isOrizontal_2 == True):
        if(start1[1] == start2[1] and ((start1[0] <= start2[0] <= end1[0]) or (
            start2[0] <= start1[0] <= end2[0]))):
            return True 
        else: 
            return False
    else:
        if(isOrizontal):
            return check_cross(start1,end1,start2,end2)
        else:
            return check_cross(start2,end2,start1,end1)
        
#Search and memorize the cells with a number of collision greater than 1
def add_crossed_cell(isOrizontal, isVertical, isOrizontal2, isVertical2, start1, end1, start2,end2):
    crossed_cell=set()
    if(isVertical == isVertical2 == True):
        for i in range(max(start1[1],start2[1]),min(end1[1],end2[1])+1):
            crossed_cell.add(tuple((start1[0],i)))
    elif(isOrizontal == isOrizontal2 == True):
        for i in range(max(start1[0],start2[0]),min(end1[0],end2[0])+1):
            crossed_cell.add(tuple((i,start1[1])))
    else:
        if(isOrizontal):
            crossed_cell.add(tuple((start2[0],start1[1])))
        else:
            crossed_cell.add(tuple((start1[0],start2[1])))
    return crossed_cell


#Resolve part 1
def part1(start,end):
    crossed_cell = set()
    for i in range(0,len(start)-1):
        isOrizontal = start[i][1] == end[i][1]
        isVertical = start[i][0] == end[i][0]
        if(isOrizontal or isVertical):
            for j in range(i+1,len(start)):
                isOrizontal_2 = start[j][1] == end[j][1]
                isVertical_2 = start[j][0] == end[j][0]
                if((isOrizontal_2 or isVertical_2)):
                     if check_collision(isOrizontal, isVertical, isOrizontal_2, isVertical_2, start[i],
                                         end[i], start[j],end[j]):
                        crossed_cell.update(add_crossed_cell(isOrizontal, isVertical, isOrizontal_2, 
                                                             isVertical_2, start[i], end[i], start[j],end[j]))
    print("Part 1: ",len(crossed_cell))
    return crossed_cell

def create_diagonal(start,end):
    path = set()
    y = start[1]
    if(start[0]<end[0] and start[1]<end[1]):
        for i in range(start[0],end[0]+1):
            path.add(tuple((i,y)))
            y+=1
    elif start[0]>end[0] and start[1]<end[1]:
        for i in range(start[0],end[0]-1,-1):
            path.add(tuple((i,y)))
            y+=1
    elif start[0]<end[0] and start[1]>end[1]:
        for i in range(start[0],end[0]+1):
            path.add(tuple((i,y)))
            y-=1
    elif start[0]>end[0] and start[1]>end[1]:
        for i in range(start[0],end[0]-1,-1):
            path.add(tuple((i,y)))
            y-=1
    return path
    
def create_row(start,end):
    path=set()
    for i in range(start[0],end[0]+1):
        path.add(tuple((i,start[1])))
    return path

def create_column(start,end):
    path=set()
    for i in range(start[1],end[1]+1):
        path.add(tuple((start[0],i)))
    return path

#Resolve part 2
def part2(crossed_cell,start,end):
    for i in range(0,len(start)):
        isOrizontal = start[i][1] == end[i][1]
        isVertical = start[i][0] == end[i][0]
        if(isOrizontal or isVertical == False):
            path = create_diagonal(start[i],end[i])
            for j in range(len(start)):
                if i == j:
                    continue
                if(start[j][1] == end[j][1]):
                    path2 = path.intersection(create_row(start[j],end[j]))
                elif start[j][0] == end[j][0]:
                    path2 = path.intersection(create_column(start[j],end[j]))
                else:
                    path2 = path.intersection(create_diagonal(start[j],end[j]))
                crossed_cell.update(path2)                  
    print("Part 2: ",len(crossed_cell))

def solver(start,end):
    crossed_cell = part1(start,end)
    part2(crossed_cell,start,end)

def main():
    start, end = parse_input()
    #print(start)
    #print(end)

#Implements the solution for the part 1
    solver(start,end)


#Resolve the problem
main()