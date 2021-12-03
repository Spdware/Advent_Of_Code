#count of the 0 and 1 in the data

with open('data.TXT', 'r') as f:
   
    zero = []
    one =  []

    line =f.readline()

    
    for i in range(0,len(line)-1):
        zero.insert(i,0)
        one.insert(i,0)
        if line[i] == '0':
            zero[i] += 1
        elif line[i] == '1':
            one[i] += 1
    

    for line in f:
        for i in range(0,len(line)-1):
            print(len(line))
            if line[i] == '0':
                zero[i] += 1
            elif line[i] == '1':
                one[i] += 1
           

    
#creation of gamma
    print(zero)
    print(one)
    gamma = []
    for i in range(0,len(line)-1):
        gamma.insert(i,'0')
     #   print(gamma)
   
  
    for i in range(0,len(gamma)):
        
        if zero[i] > one[i]:
            gamma[i] = '0'
        else:
            gamma[i] = '1'
    print(gamma)
    gamma = "".join(gamma)
    print(gamma)
    gamma = int(gamma, 2)
    print(gamma)


#creation of epsylon
    epsylon = []  
    
    for i in range(0,len(line)-1):
        epsylon.insert(i,'0')
      #  print(epsylon)
    
    for i in range(0,len(epsylon)):
        
        
        if zero[i] < one[i]:
            epsylon[i] = '0'
        else:
            epsylon[i] = '1'

    print(epsylon)
    epsylon = "".join(epsylon)
    print(epsylon)
    epsylon = int(epsylon, 2)
    print(epsylon)
    
 
#value of power consumption    
    
    power_consumption = gamma * epsylon

    print("Power consumption: ", power_consumption)

    
    
            