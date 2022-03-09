
def label():
    with open('data1.txt', 'r') as f:
        elem = f.read().split('\n\n')
        num = len(elem) - 1
    draw = elem[0].split(',')
    elem = elem[1:]
    return draw, num, elem


def check(n):
   
    for j in range(0, len(labels)):
        count = 0
        if n < 10:
            labels[j] = labels[j].replace(f' {n} ', ' X ')
            labels[j] = labels[j].replace(f' {n}\n', ' X\n')

        else:
            labels[j] = labels[j].replace(f'{n}', ' X')
            #labels[j] = labels[j].replace(str(n)+'\n', ' X\n')
       # print(labels[j])
        tmp = ''.join(labels[j])
        rows = [tmp.split('\n')]
        for h in rows:
            colums = [[h[k].split()[i] for i in range(0,5)] for k in range(0,5)] 


        for i in colums:
            if i.count('X') == 5 :               
                del labels[j]
                for j in colums:
                    for h in j:
                        if h == 'X':
                            pass
                        else:
                            count += int(h)
                return count


        for i in rows:
            if i.count('X') == 5 :
                del labels[j]
                for j in rows:
                    for h in j:
                        if h == 'X':
                            pass
                        else:
                            count += int(h)
                return count
    
       
       
    return 0 
    


    
               
def victory():
    for i in draw:
        tmp = 0
       # print(i)
        tmp = int(i)*check(int(i))
        print(tmp)
       # print(labels)
        if len(labels) == 0:
            return tmp

    return -1



draw, num_lab, labels = label()
print(victory())
