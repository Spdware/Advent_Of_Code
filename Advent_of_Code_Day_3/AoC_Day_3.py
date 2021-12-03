#count of the 0 and 1 in the data

with open('data.TXT', 'r') as f:
   
    zero = []
    one =  []
    

    for line in f:
        for i in range(0,len(line)-1):
            zero.insert(i,0)
            one.insert(i,0)
            if line[i] == '0':
                zero[i] += 1
            else:
                one[i] += 1
           

    
#creation of gamma
    gamma = []
    for i in range(0,len(line)-1):
        gamma.insert(i,'0')
   
  
    for i in range(0,len(gamma)-1):
        if zero[i] > one[i]:
            gamma[i] = '0'
        else:
            gamma[i] = '1'
    gamma = "".join(gamma)
    gamma = int(gamma, 2)


#creation of epsylon
    epsylon = []  
    
    for i in range(0,len(line)-1):
        epsylon.insert(i,'0')
    
    for i in range(0,len(epsylon)):
        if zero[i] < one[i]:
            epsylon[i] = '0'
        else:
            epsylon[i] = '1'
    epsylon = "".join(epsylon)
    epsylon = int(epsylon, 2)
    
 
#value of power consumption    
    
    power_consumption = gamma * epsylon

    print("Power consumption: ", power_consumption)

    
    
            