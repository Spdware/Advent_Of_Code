depht = 0
hor = 0




with open('data.txt', 'r') as f:
        
    for i in f:

        mv, num = i.split()
        num = int(num)
        if mv == 'forward':
            hor += num
        elif mv == 'up':
            depht -= num
        else:
            depht += num
    print(depht*hor)
     




       

       


           