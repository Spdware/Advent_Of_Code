import numpy as np
#Unoptimized method
def part1(input, days):
    for i in range(days):
        input = input - 1
        new_lanternfish = np.count_nonzero(input == 0)
        input[input==0]=7
        input = np.concatenate((input,[9 for  i in range(new_lanternfish)]))
    return input.size
#Optimized method
def part2(input, days):
    data = {i:np.count_nonzero(input == i) for i in range(10)}
    for d in range(days):
        new_lanternfish = data[0]
        for i in range(9):
            data[i]=data[i+1]
        data[6] += new_lanternfish
        data[9] = data[0]
    x = 0
    for i in range(len(data)-1):
        x += data[i]
    return x 

def main():
    input = open("data.txt","r")
    input = np.array([int(x) for x in input.readline().split(",")])
    print(f"Part 1: {part1(input,79)}")
    print(f"Part 2: {part2(input,256)}")

main()