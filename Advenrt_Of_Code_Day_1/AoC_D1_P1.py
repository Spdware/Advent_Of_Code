
    
with open('data.txt', 'r') as f:
    inc = 0
    line = f.readline()
    
    a = int(line)
    print(a)
    for i in f:
        el = int(i)
        if(el > a):
            inc += 1
        a = el
    print(inc)
 
