#count of the 0 and 1 in the data

with open('data.TXT', 'r') as f:
   
    zero = [0,0,0,0,0]
    one =  [0,0,0,0,0]
    

    for line in f:
        for i in range(0,len(line)-1):
            if line[i] == '0':
                zero[i] += 1
            else:
                one[i] += 1
           

    
#creation of gamma
    
    gamma = ['0','0','0','0','0']
   
  
    for i in range(0,len(zero)-1):
        if zero[i] > one[i]:
            gamma[i] = '0'
        else:
            gamma[i] = '1'
    gamma = "".join(gamma)
    gamma = int(gamma, 2)


#creation of epsylon
    epsylon = ['0','0','0','0','0']  
    
    
    for i in range(0,len(zero)):
        if zero[i] < one[i]:
            epsylon[i] = '0'
        else:
            epsylon[i] = '1'
    epsylon = "".join(epsylon)
    epsylon = int(epsylon, 2)
    
 
#value of power consumption    
    
    power_consumption = gamma * epsylon

    print("Power consumption: ", power_consumption)

    
    
            