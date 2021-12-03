depht = 0
hor = 0


def moving(depht,hor):
   
    while True:
        while True:
            x = input('Insert the tipology of movement(\n1 : down \n2 : up \n 3: forward \n0 : exit\n)\n')
            if (x == '1' or x == '2' or x == '3' or x == '0') :
                break
        
        
        if x != '0':

            while True:
                y = input('Insert distance:')

                y = int(y)

                if y >= 0:
                    break

            x = int(x)
           
            if x == 1:
                depht += y   #down
            elif x == 2:
                 depht -= y   #up
            elif x == 3:
               hor += y     #forward
           
                
            print('Depht:',depht,'\nHorizontal :', hor,'\n')  
        else:
            break  
    print('Final depht:',depht,'\nFinal horizontal :', hor,'\nDepht*Horizontal :', depht*hor,'\n')   
        
          
moving(depht,hor)
                


       


           