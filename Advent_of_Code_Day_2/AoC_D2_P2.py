depht = 0
hor = 0
aim = 0



with open('data.txt', 'r') as f:
        
    for i in f:

        mv, num = i.split()
        num = int(num)
        if mv == 'forward':
            hor += num
            depht += num*aim
        elif mv == 'up':
            aim -= num
        else:
            aim += num
    print(depht*hor)
     