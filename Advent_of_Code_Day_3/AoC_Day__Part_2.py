#count of the 0 and 1 in the data
def decider(lista, i):
    count_zero = 0
    count_one = 0
    for k in lista:
        if k[i] == '1':
            count_one += 1
        else:
            count_zero += 1
    if count_one >= count_zero:
        return 1
    else:
        return 0




with open('data.TXT', 'r') as f:
   
    zero = []
    one =  []
    count_ox = []
    count_co = []
   
    counter = 1

    line =f.readline()

    count_ox.insert(0,line)
    count_co.insert(0,line)
    
    for i in range(0,len(line)-1):
        zero.insert(i,0)
        one.insert(i,0)
       
       
        


        if line[i] == '0':
            zero[i] += 1
        elif line[i] == '1':
            one[i] += 1
    

    for line in f:
        count_ox.insert(counter,line)
        count_co.insert(counter,line)
        counter +=1
        for i in range(0,len(line)-1):
           # print(len(line))
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
   # print(gamma)
    gamma = "".join(gamma)
  #  print(gamma)
    gamma = int(gamma, 2)
  #  print(gamma)


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

 #   print(epsylon)
    epsylon = "".join(epsylon)
  #  print(epsylon)
    epsylon = int(epsylon, 2)
 #   print(epsylon)
    

  




    
 
#value of power consumption    
    
    power_consumption = gamma * epsylon
   

    print("Power consumption: ", power_consumption)
    
    
   # print(count_ox)
    for i in range(0,len(line)-1):
        decision = decider(count_ox, i)
      #  print(i)
        if decision:
            for k in count_ox:
                if k[i] != '1':
                    count_ox = [value for value in count_ox if value != k]
                 #   print(k)
                 #   print(count_ox)
        else:
            for k in count_ox:
                if k[i] !='0':
                    count_ox = [value for value in count_ox if value != k] 
                  #  print(k)
                  #  print(count_ox)
        if(len(set(count_ox)) == 1):
                break
        


    print(count_ox[0])
    oxigen = int(count_ox[0],2)
    print(oxigen)



   # print(count_co)
    for i in range(0,len(line)-1):
        decision = decider(count_co, i)
      #  print(i)
        if not decision:
            for k in count_co:
                if k[i] != '1':
                    count_co = [value for value in count_co if value != k]
                  #  print(k)
                  #  print(count_co)
        else:
            for k in count_co:
                if k[i] !='0':
                    count_co = [value for value in count_co if value != k] 
                   # print(k)
                   # print(count_co)
        if(len(set(count_co)) == 1):
                break
        

        


    print(count_co[0])
    carbon_dioxide = int(count_co[0],2)
    print(carbon_dioxide)

    print(oxigen * carbon_dioxide)