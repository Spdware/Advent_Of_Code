
def label():
    with open('data.txt', 'r') as f:
        elem = f.read().split('\n\n')
        num = len(elem) - 1
    draw = elem[0].split(',')
    elem = elem[1:]
    return draw, num, elem


def check(n):
    count = 0
    for j in range(0, num_lab):
        if n < 10:
            labels[j] = labels[j].replace(f' {n} ', ' X ')
            labels[j] = labels[j].replace(f' {n}\n', ' X\n')

        else:
            labels[j] = labels[j].replace(f'{n}', ' X')
            #labels[j] = labels[j].replace(str(n)+'\n', ' X\n')
    for i in labels:
        tmp = ''.join(i)
        rows = [tmp.split('\n')]
        for h in rows:
            colums = [[h[j].split()[i] for i in range(0,5)] for j in range(0,5)] 
        for i in rows:
            if i.count('X') == 5 :
                for j in rows:
                    for h in j:
                        if h == ' X':
                            pass
                        else:
                            count += int(h)
                return count
            
    
        for i in colums:
           if i.count('X') == 5 :
                for j in colums:
                    for h in j:
                        if h == 'X':
                            pass
                        else:
                            count += int(h)
                return count
    return 0 
    


    
               
def victory():
    for i in draw:
       # print(i)
        tmp = int(i)*check(int(i))
        if tmp:
            return tmp
    return -1



draw, num_lab, labels = label()
print(victory())


 
            






