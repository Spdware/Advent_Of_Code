with open('data.txt', 'r') as f:
    count = 0
    number = []
    for i in f:
        tmp = int(i)
        number.insert(len(number),tmp)

for i in range(3, len(number)):
    if number[i] > number[i-3]:
        count += 1

print(count)

         
        

